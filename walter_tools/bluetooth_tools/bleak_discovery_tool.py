# https://github.com/hbldh/bleak
import asyncio
from bleak import BleakScanner


async def main():
    # 发现附近设备
    devices = await BleakScanner.discover()
    count = 0
    for d in devices:
        print(d)
        count += 1
    print("附近设备数:{}".format(count))


asyncio.run(main())
