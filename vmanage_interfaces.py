import requests
import os
import json

VMANAGE_URL = "https://sandbox-sdwan-2.cisco.com:443"
USERNAME = "devnetuser"
PASSWORD = "RG!_Yw919_83"
requests.packages.urllib3.disable_warnings()

def get_auth_token():
    url = f"{VMANAGE_URL}/j_security_check"
    payload = {"j_username": USERNAME, "j_password": PASSWORD}
    session = requests.session()
    response = session.post(url, data=payload, verify=False)
    if response.status_code != 200 or "html" in response.text:
        raise Exception("Authentication failed")
    return session

def get_cedges(session):
    url = f"{VMANAGE_URL}/dataservice/device"
    response = session.get(url, verify=False)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve devices: {response.text}")
    devices = response.json()["data"]
    cedges = [device for device in devices if device["device-type"] == "vedge"] #cedge? vedge?
    return cedges

def make_system_ip_request(session, system_ip, hostname, output_file):
    url = f"{VMANAGE_URL}/dataservice/device/interface?deviceId={system_ip}"
    response = session.get(url, verify=False)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve data for system-ip {system_ip}: {response.text}")
    interfaces = response.json()
    for interface in interfaces.get("data", []):
        if interface.get("ifname") == "loopback400":
            output = {
                "hostname": hostname,
                "System-IP": system_ip,
                "Interface": interface.get("ifname"),
                "IP": interface.get("ip-address")
            }
            print(output)
            with open(output_file, "a") as f:
                f.write(json.dumps(output) + "\n")

def main():
    session = get_auth_token()
    cedges = get_cedges(session)
    print(f"Found {len(cedges)} cEdges")
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_file = os.path.join(desktop_path, "cedge_output.json")
    if os.path.exists(output_file):
        os.remove(output_file)
    for cedge in cedges:
        system_ip = cedge.get("system-ip")
        hostname = cedge.get("host-name")
        if system_ip and hostname:
            make_system_ip_request(session, system_ip, hostname, output_file)
        else:
            print("Missing system-ip or hostname for device")

if __name__ == "__main__":
    main()