from tplinkcloud import TPLinkDeviceManager
import asyncio
import os


def get_bulbs():
    device_manager = TPLinkDeviceManager(
        os.getenv("email"), os.getenv("password"))

    devices = {}

    all_devices = asyncio.run(device_manager.get_devices())

    for device in all_devices:
        devices[device.get_alias()] = device

    return devices
