# https://github.com/hbldh/bleak
import asyncio
from bleak import BleakScanner

async def main():
    # 发现附近设备
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(main())