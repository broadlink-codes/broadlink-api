import os
from typing import Optional

import broadlink
from dotenv import dotenv_values


config = dotenv_values(".env")

def __get_env(key, default=None):
  return config.get(key, os.environ.get(key, default))

## TODO: add support for more devices
DEVICE:Optional[broadlink.rm4mini] = None

def is_device_active(device: broadlink.rm4mini):
  try:
    device.hello()
    return True
  except:
    return False

DEVICE_NAME = __get_env("DEVICE_NAME")
DEVICE_MAC = __get_env("DEVICE_MAC")
DEVICE_IP = __get_env("DEVICE_IP")
DEVICE_PORT = int(__get_env("DEVICE_PORT", 80))
DEVICE_DEVTYPE = int(__get_env("DEVICE_DEVTYPE", 1122))
DISCOVERY_TYPE = __get_env("DISCOVERY_TYPE")

def get_device()-> broadlink.rm4mini:
  global DEVICE
  if (not DEVICE) or (not is_device_active(DEVICE)):
    if DISCOVERY_TYPE == "device-name":
      all_devices = broadlink.discover()
      for device in all_devices:
        if device.name == DEVICE_NAME:
          DEVICE = device
          break
      if not DEVICE:
        raise Exception(
          f"Device with name {DEVICE_NAME} not found in active devices, please recheck the power. If running on docker use '--network host'"
        )
    else:
      try:
        DEVICE = broadlink.remote.rm4mini((DEVICE_IP, DEVICE_PORT), mac=bytearray.fromhex(DEVICE_MAC), devtype=DEVICE_DEVTYPE)
      except Exception as e:
        raise Exception(
          f"Unable to get device with ip: {DEVICE_IP} error: {e}"
        )

    try:
      DEVICE.auth()
    except:
      raise Exception(
        "Unable to authenticate the device"
      )
  return DEVICE


LEARN_TIMEOUT_SEC = 30
