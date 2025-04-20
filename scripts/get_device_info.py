import broadlink
import json


if __name__ == '__main__':
    devices = broadlink.discover()

    device_data = []
    for device in devices:
        device_data.append(
            {
                "NAME": device.name,
                "DEVICE_IP": device.host[0],
                "DEVICE_PORT": device.host[1],
                "DEVICE_MAC": device.mac.hex(),
                "DEVICE_DEVTYPE": device.devtype
            }
        )

    print(json.dumps(device_data, indent=4))