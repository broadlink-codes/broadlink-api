import broadlink
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    ssid = parser.add_argument('--ssid', type=str, required=True, help='SSID of the network')
    parser.add_argument('--password', type=str, required=True, help='Password of the network')
    parser.add_argument("--security", type=int, required=True, help='Security mode of the network (0 = none, 1 = WEP, 2 = WPA1, 3 = WPA2, 4 = WPA1/2)')
    args = parser.parse_args()
    ssid = args.ssid
    password = args.password
    security = args.security

    broadlink.setup(ssid, password, security)