import requests

def get_public_ip():return requests.get('https://ipinfo.io/ip').text.strip()

print(f"{get_public_ip()}")