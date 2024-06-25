from django.shortcuts import render
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
            return ip_info 
        else:
            return None
    else:
        return None

def index(request):
    ip_address = get_ip_info()
    ip_info = get_ip_loc(ip_address)
    
    context = {
        'ip_address': ip_address,
        'ip_info': ip_info
    }
    return render(request, 'ip_locator/index.html', context)
