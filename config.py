import os
from typing import Optional

import broadlink
from dotenv import dotenv_values


config = dotenv_values(".env")

__get_env = lambda key: config.get(key, os.environ.get(key))

## TODO: add support for more devices
DEVICE:Optional[broadlink.rm4mini] = None

def is_device_active(device: broadlink.rm4mini):
  try:
    device.hello()
    return True
  except:
    return False

def get_device(device_name)-> broadlink.rm4mini:
  global DEVICE
  if (not DEVICE) or (not is_device_active(DEVICE)):
    all_devices = broadlink.discover()
    for device in all_devices:
      if device.name == device_name:
        try:
          device.auth()
          DEVICE = device
        except:
          raise Exception(
            "Unable to authenticate the device"
          )
    if not DEVICE:
      raise Exception(
        f"Device with name {device_name} not found in active devices, please recheck the power"
      )
  return DEVICE


DEVICE_NAME = __get_env("DEVICE_NAME")
LEARN_TIMEOUT_SEC = 30
