import asyncio
from bleak import BleakClient

# 00002a00-0000-1000-8000-00805f9b34fb：设备名称
# 00002a19-0000-1000-8000-00805f9b34fb：电池电量
# 00002a29-0000-1000-8000-00805f9b34fb：设备制造商名称
# 00002a37-0000-1000-8000-00805f9b34fb：心率测量
# 00002a42-0000-1000-8000-00805f9b34fb：测量间隔
# 0000180d-0000-1000-8000-00805f9b34fb：心率服务
# 0000180a-0000-1000-8000-00805f9b34fb：设备信息服务
# 00002a25-0000-1000-8000-00805f9b34fb：序列号字符串
# 00002a26-0000-1000-8000-00805f9b34fb：固件版本字符串
# 00002a27-0000-1000-8000-00805f9b34fb：硬件版本字符串
# 00002a28-0000-1000-8000-00805f9b34fb：软件版本字符串
# 00002a38-0000-1000-8000-00805f9b34fb：身体传感器位置
# 00002a39-0000-1000-8000-00805f9b34fb：血压测量
# 00002a4d-0000-1000-8000-00805f9b34fb：脂肪百分比特性
# 00002a50-0000-1000-8000-00805f9b34fb：血氧饱和度特性
# 00002a53-0000-1000-8000-00805f9b34fb：光感应特性
# 00002a5b-0000-1000-8000-00805f9b34fb：描述符
# 0000180f-0000-1000-8000-00805f9b34fb：电池服务
# 00001810-0000-1000-8000-00805f9b34fb：时间服务
# 00002a24-0000-1000-8000-00805f9b34fb：一个标准的GATT（通用属性）特征，用于表示设备的模型号。它并不特定于某种类型的设备，而是通用于许多设备，包括智能手表、健康追踪器、蓝牙耳机等。
MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"
address = "42221DE4-297D-A6E9-15C0-472AAFDC836B"

async def main(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

asyncio.run(main(address))