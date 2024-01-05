from objc import managers
from PyObjCTools import AppHelper

def main():
    # 创建一个中心设备管理器
    mgr = managers.CBCentralManager.alloc().initWithDelegate_queue_(None, None)

    def centralManagerDidUpdateState_(self, cm):
        # 蓝牙状态更新回调
        state = cm.state()

        if state == managers.CBManagerStatePoweredOn:
            # 蓝牙已开启，可以开始扫描设备
            cm.scanForPeripheralsWithServices_options_([], None)

    def centralManager_didDiscoverPeripheral_advertisementData_RSSI_(self, cm, peripheral, adv_data, rssi):
        # 发现附近蓝牙设备的回调
        print('Discovered:', peripheral.name())

    # 设置回调函数
    managers.CentralManagerDelegate = type(
        'CentralManagerDelegate',
        (managers.NSObject,),
        {
            'centralManagerDidUpdateState:': centralManagerDidUpdateState_,
            'centralManager:didDiscoverPeripheral:advertisementData:RSSI:': centralManager_didDiscoverPeripheral_advertisementData_RSSI_,
        })

    # 运行主循环
    AppHelper.runConsoleEventLoop(installInterrupt=True)

if __name__ == '__main__':
    main()
