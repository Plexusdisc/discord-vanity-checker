import requests
from colorama import Fore, init
init(autoreset=True)

while True:
    print(Fore.BLUE+"Enter the vanity url you want to check")
    vanity = input("https://discord.gg/")
    r = requests.get(f"https://discord.com/api/v8/invites/{vanity}?with_counts=true")
    if r.status_code == 404:
        print(Fore.GREEN+"Vanity is available\n")
    else:
        print(Fore.RED+"Vanity is taken taken/termed\n")