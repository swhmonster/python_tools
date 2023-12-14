"""PyODPS 3
请确保不要使用从 MaxCompute下载数据来处理。下载数据操作常包括Table/Instance的open_reader以及 DataFrame的to_pandas方法。
推荐使用 PyODPS DataFrame（从 MaxCompute 表创建）和MaxCompute SQL来处理数据。
更详细的内容可以参考：https://help.aliyun.com/document_detail/90481.html
"""
from odps import options
from datetime import datetime
import calendar

options.sql.settings = {"odps.sql.submit.mode": "script", "odps.sql.hive.compatible": "true"}
print('ds=' + args['bizdate'])

config_table = "config_table"
result_table = "result_table"

def handle(i, row):
    print("===start===规则id:" + row['rule_id'] + "===指标:" + row['indicator'] + "===")
    headSql = " insert into table "
    if i == 0:
        print("第一次，需清理分区...自动处理中...")
        headSql = " INSERT OVERWRITE TABLE "

    # 聚合维度为空，即数据源维度聚合
    dimension = row['aggregation_dimension']
    if dimension is None:
        dimension = "'源数据维度',"
    else:
        dimension = "\"" + row['aggregation_dimension'] + "\","

    select_sql = "'" + row['audit_group'] + "','" + row['audit_segment'] + "','" + row['indicator'] + "','" + row[
        'rule_id'] + "'," + dimension
    default_sql = "'" + row['audit_group'] + "','" + row['audit_segment'] + "','" + row['indicator'] + "','" + row[
        'rule_id'] + "'," + dimension
    selectSqlList = []
    defaultSqlList = []

    validate_flag = True
    if row['aggregation_target'] is None:
        print("加工目标缺失！")
        validate_flag = False
    elif row['aggregation_type'] is None:
        print("加工目标聚合类型缺失！")
        validate_flag = False
    else:
        selectSqlList.append(row['aggregation_type'] + "(" + row['aggregation_target'] + ")")

    defaultSqlList.append('sum(0)')

    # 配置-币种校验
    if row['currency'] is None:
        print("币种缺失（弱校验）！")
        selectSqlList.append("'USD'")
        defaultSqlList.append("'USD'")
    else:
        selectSqlList.append(row['currency'])
        defaultSqlList.append(row['currency'])

    # 配置-租户校验
    if row['merchant_code'] is None:
        print("租户缺失！")
        validate_flag = False
    else:
        selectSqlList.append(row['merchant_code'])
        defaultSqlList.append(row['merchant_code'])

    # 配置-看板项目列校验
    if row['row_head'] is None:
        print("看板项目列缺失！默认统一维度")
        selectSqlList.append("'源数据统一维度'")
        defaultSqlList.append("'源数据统一维度'")
    else:
        selectSqlList.append(row['row_head'])
        defaultSqlList.append(row['row_head'])

    # 配置-排序字段校验
    if row['order_asc'] is None:
        print("稽核段排序未配置！")
        validate_flag = False
    else:
        selectSqlList.append(row['order_asc'])
        defaultSqlList.append(row['order_asc'])

    # 配置-业务日期字段校验
    if row['bizdate'] is None:
        print("业务日期未配置！")
        validate_flag = False
    else:
        selectSqlList.append(row['bizdate'])

    select_sql = select_sql + ','.join(selectSqlList)
    default_sql = default_sql + ','.join(defaultSqlList)

    # 校验from_sql
    if row['datasource'] is None:
        print("数据源配置缺失！")
        validate_flag = False

    if validate_flag:
        print("校验通过！")
    else:
        print("校验不通过！")
        return None

    where_sql = " 1=1 "
    if row['filter_condition'] is not None and len(row['filter_condition']) > 0:
        filter_condition = row['filter_condition'].replace("${bizdate}", args['bizdate'])
        # 回刷数据，默认加工当天的
        where_sql = where_sql + " and " + filter_condition

    groupby_sql = ""
    if row['aggregation_dimension'] is not None:
        groupby_sql = " group by " + row['aggregation_dimension']

    sql = """
    {} {} PARTITION (ds = '{}') 
    select {} 
    from {} 
    where {} 
    {} ;
    """.format(headSql, result_table, args['bizdate'], select_sql, row['datasource'], where_sql, groupby_sql)

    if i > 0 and row['needsetdefault'] is not None:
        today = datetime.strptime(args['bizdate'], '%Y%m%d')
        current_year = today.year
        current_month = today.month
        for yyyy in range(2023, current_year + 1):
            for mm in range(1, current_month + 1):
                defaultSqlResList = []
                last_day = calendar.monthrange(yyyy, mm)[1]
                month = str(mm)
                if (mm < 10):
                    month = '0' + month
                for dd in range(1, last_day):
                    day = str(dd)
                    if (dd < 10):
                        day = '0' + day
                    tempSql = default_sql + "," + str(yyyy) + str(month) + str(day)
                    defaultSqlResList.append("""
                    {} {} PARTITION (ds = '{}') 
                    select {} 
                    from {} 
                    where {} 
                    {} limit 1;
                    """.format(" insert into table ", result_table, args['bizdate'], tempSql, row['datasource'],
                               where_sql, groupby_sql))
                execSql('\n'.join(defaultSqlResList))

    print("===end===规则id:" + row['rule_id'] + "===指标:" + row['indicator'] + "===")
    return sql


def execSql(execute_sql):
    print("===start excuting sql===")
    print(execute_sql)
    instance = o.run_sql(execute_sql)
    print(instance.get_logview_address())  # 获取logview地址
    instance.wait_for_success()
    print("===end excuting sql===")


config_sql = """
SELECT  *
FROM    {} ;""".format(config_table)
print("config_sql:" + config_sql)
with o.execute_sql(config_sql).open_reader(tunnel=True, limit=False) as reader:
    sqlList = []
    for i, row in enumerate(reader):
        print(i, row)
        if i == 0:
            execSql(handle(i, row))
        else:
            sqlList.append(handle(i, row))
    execute_sql = '\n'.join(sqlList)
    execSql(execute_sql)
