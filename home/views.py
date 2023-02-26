import asyncio
import os
from django.shortcuts import render
from tplinkcloud import TPLinkDeviceManager
from dotenv import load_dotenv


def home(request):
    load_dotenv()

    device_manager = TPLinkDeviceManager(
        os.getenv("email"), os.getenv("password"))

    devices = {}

    all_devices = asyncio.run(device_manager.get_devices())

    for device in all_devices:
        devices[device.get_alias()] = device

    return render(request, 'home.html', {'devices': devices})
