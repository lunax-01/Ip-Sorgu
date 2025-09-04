
# Modules importation
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """
SwarlecX Serverı SUNAR
 made by lunax_01
""" + Fore.LIGHTCYAN_EX)
print(banner)
import requests

def ip_lookup(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'success':
        print(f"IP Address: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"ISP: {data['isp']}")
        print(f"ZIP Code: {data['zip']}")
    else:
        print("❌ IP Hatalı.")

ip_address = input("İP Adresi Gir :): ")
ip_lookup(ip_address)
input()
