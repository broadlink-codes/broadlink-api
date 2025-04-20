# 📡 Broadlink Universal Remote API

A lightweight API server for controlling Broadlink universal remote devices via your local network.

## 📦 Features

- **Send IR Packets** to devices
- **Learn IR Commands** from remotes
- **Device Discovery & Configuration**
- **Dockerized Deployment**

---

## 🔧 API Endpoints

### `POST /api/send-packet`

**Broadcast instruction packets to the Broadlink device.**

- **Body:**
  ```json
  {
    "packets": [<pulse_array>]
  }
  ```

---

### `GET /api/learn`

**Put the device into learning mode.**

---

## 📶 Device Configuration

### 1. **Reset Device**
If the device is already connected to the Broadlink app, reset it:
- **Long press** the reset button until the **blue LED blinks quickly**
- **Long press again** until it **blinks slowly** (AP Mode)

### 2. **Connect to BroadlinkProv**
- Manually connect your system to the **Wi-Fi SSID**

### 3. **Install broadlink**
```bash
pip install broadlink
cd scripts
```

### 4. **Connect device to Wi-Fi**
```bash
python setup_device.py --ssid=<your_wifi_name> --password=<your_wifi_password> --security=<usually 3>
```

### 5. **Retrieve Device Info**
```bash
python get_device_info.py
```
This script will output required environment variables to run the API.

---

## 🔐 Required Environment Variables

| Variable         | Description                                  |
|------------------|----------------------------------------------|
| `DEVICE_NAME`    | (Only for discovery via device name)         |
| `DEVICE_MAC`     | MAC address of the device (from `get_device_info.py`)                   |
| `DEVICE_IP`      | Local IP address of the device (from `get_device_info.py`)              |
| `DEVICE_PORT`    | Port (usually `80` or auto-discovered) (from `get_device_info.py`)      |
| `DEVICE_DEVTYPE` | Device type code (from `get_device_info.py`) |
| `DISCOVERY_TYPE` | `"ip-address"` or `"device-name"`            |

---

## 🚀 Running the API

### 1. **Build Docker Image**
```bash
docker build -t broadlink-api .
```

### 2. **Run Container**

#### 📍 IP Address Discovery (Recommended for Windows/Linux)
```bash
docker run \
  -e DISCOVERY_TYPE="ip-address" \
  -e DEVICE_MAC=<your_mac> \
  -e DEVICE_IP=<your_ip> \
  -e DEVICE_PORT=<your_port> \
  -e DEVICE_DEVTYPE=<your_devtype> \
  -p 8000:8000 \
  broadlink-api
```

#### 📍 Device Name Discovery (Linux only)
```bash
docker run \
  --network host \
  -e DISCOVERY_TYPE="device-name" \
  -e DEVICE_NAME=<your_device_name> \
  -p 8000:8000 \
  broadlink-api
```

---

## ✅ Notes

- If your device is locked by the Broadlink app, **reset it first** before configuration.
- For Linux users using `device-name` discovery, make sure to use `--network host`.
- `get_device_info.py` provides all required environment variable values.

---

## 🚧 Troubleshooting

- **Device not responding?** Ensure it is on the same network and not paired with the mobile app.
- **Invalid device info?** Re-run `get_device_info.py` and verify MAC, IP, and Device Type.

---

## 🌐 License

MIT License

