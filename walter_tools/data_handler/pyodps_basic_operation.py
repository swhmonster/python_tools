import os
from odps import ODPS
from odps import options
from multiprocessing import Pool
from odps.tunnel import TableTunnel
import random

# 确保 ALIBABA_CLOUD_ACCESS_KEY_ID 环境变量设置为用户 Access Key ID，
# ALIBABA_CLOUD_ACCESS_KEY_SECRET 环境变量设置为用户 Access Key Secret，
o = ODPS(
    access_id=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'),
    secret_access_key=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
    project='******',
    endpoint='http://******',
)

options.sql.settings = {"odps.sql.submit.mode": "script", "odps.sql.hive.compatible": "true"}


def write_records(tunnel, table, session_id, block_id):
    # 对使用指定的ID创建Session。
    local_session = tunnel.create_upload_session(table.name, upload_id=session_id)
    # 创建Writer时指定Block_ID。
    with local_session.open_record_writer(block_id) as writer:
        for i in range(5):
            # 生成数据并写入对应Block。
            record = table.new_record([random.randint(1, 100), random.random()])
            writer.write(record)


def multi_write_to_common_table(table):
    N_WORKERS = 3

    tunnel = TableTunnel(o)
    upload_session = tunnel.create_upload_session(table.name)

    # 每个进程使用同一个Session_ID。
    session_id = upload_session.id

    pool = Pool(processes=N_WORKERS)
    futures = []
    block_ids = []
    for i in range(N_WORKERS):
        futures.append(pool.apply_async(write_records, (tunnel, table, session_id, i)))
        block_ids.append(i)
    [f.get() for f in futures]

    # 最后执行Commit，并指定所有Block。
    upload_session.commit(block_ids)


if __name__ == '__main__':
    print('当前项目空间' + str(o.get_project()))
    partion_table = 'my_new_table'
    non_partion_table = 'my_new_table02'
    table_tuple = (partion_table, non_partion_table)

    # 创建分区表my_new_table，可传入（表字段列表，分区字段列表）
    pt_table = o.create_table(partion_table, ('num bigint, num2 double', 'ds string'), if_not_exists=True)
    # 同步表更新
    pt_table.reload()

    # 创建非分区表my_new_table02
    non_pt_table = o.create_table(non_partion_table, 'num bigint, num2 double', if_not_exists=True)
    # 同步表更新
    non_pt_table.reload()

    # 写入分区表数据
    # 创建20231215分区，并写入数据
    with pt_table.open_writer(partition='ds=20231215', create_partition=True) as writer:
        # 此处可以是List。
        records = [[1, 1.0],
                   [2, 2.0],
                   [3, 3.0],
                   [4, 4.0]]
        # 这里Records可以是可迭代对象。
        writer.write(records)

    validate_flag = False
    for tup in table_tuple:
        if o.exist_table(tup):
            print('校验通过：表{}存在'.format(tup))
            validate_flag = True
        else:
            print('校验不通过：表{}不存在'.format(tup))

    # 多线程写入普通表
    multi_write_to_common_table(non_pt_table)

    # 基础查询校验数据
    if validate_flag:
        print('查询sql执行，读取表数据：')
        for tup in table_tuple:
            print(tup)
            sql = 'SELECT * FROM {} LIMIT 3'
            result = o.execute_sql(sql.format(tup))
            with result.open_reader() as reader:
                for record in reader:
                    print(record)

        print('使用入口对象的read_table()方法，读取数据：')
        for record in o.read_table(pt_table, partition='ds = 20231215'):
            print(records)

        print('调用open_reader()方法读取数据，读取数据：')

        print("使用with表达式写法")
        with pt_table.open_reader(partition='ds = 20231215') as reader:
            count = reader.count
            # 可以执行多次，直到将Count数量的Record读完，此处可以改造成并行操作。
            for record in reader[5:10]:
                print(record)

        # print("不使用with表达式写法")
        # reader = pt_table.open_reader(partition='pt=20231215')
        # count = reader.count
        # # 可以执行多次，直到将Count数量的Record读完，此处可以改造成并行操作。
        # for record in reader[5:10]:
        #     print(record)

        # 删除表
        # 只有表存在时，才删除表
        o.delete_table(partion_table, if_exists=True)
        # Table对象存在时，直接调用Drop方法删除
        non_pt_table.drop()
