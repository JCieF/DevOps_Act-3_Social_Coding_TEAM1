import requests

def get_ip_info():
    # Make a request to the ipify API to get the user's public IPv4 address
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        # If the request is successful, return the IP address from the response
        return response.json()["ip"]
    else:
        # If the request fails, return None
        return None

def get_ip_loc(ip_add):
    # Check if an IP address was provided
    if ip_add:
        # Make a request to the ipapi API to get geolocation information based on the IP address
        loc_response = requests.get(f'https://ipapi.co/{ip_add}/json/')
        if loc_response.status_code == 200:
            # If the request is successful, parse the JSON response
            ip_info = loc_response.json()
            # Print the IP address and its associated location information
            print(f"IPv4 Address: {ip_info.get('ip')}")
            print(f"City: {ip_info.get('city')}")
            print(f"Region: {ip_info.get('region')}")
            print(f"Country: {ip_info.get('country_name')}")
            print(f"ASN: {ip_info.get('asn')}")
        else:
            # If the location request fails, print an error message
            print("Error: Failed to retrieve location information.")
    else:
        # If no IP address was retrieved, print an error message
        print("Error: Failed to retrieve IP address.")

# Get the user's public IPv4 address
ip_address = get_ip_info()
print("The user's IPv4 address and current location is as follows:")

# Get and print the geolocation information for the retrieved IP address
get_ip_loc(ip_address)
