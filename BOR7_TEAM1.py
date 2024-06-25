import requests

def get_ip_info():
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        return response.json()["ip"]
    else:
        return None

def get_ip_loc(ip_add):
    if ip_add:
        loc_response = requests.get(f'https://ipapi.co/{ip_add}/json/')
        if loc_response.status_code == 200:
            ip_info = loc_response.json()
            print(f"IPv4 Address: {ip_info.get('ip')}")
            print(f"City: {ip_info.get('city')}")
            print(f"Region: {ip_info.get('region')}")
            print(f"Country: {ip_info.get('country_name')}")
            print(f"ASN: {ip_info.get('asn')}")
        else:
            print("Error: Failed to retrieve location information.")
    else:
        print("Error: Failed to retrieve IP address.")

ip_address = get_ip_info()
print("The user's IPv4 address and current location is as follows:")
get_ip_loc(ip_address)