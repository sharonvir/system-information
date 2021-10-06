# Creator : MRD3F417
# BlackGuard Team - Discord : discord.gg/4DbuQRg6YX
# Python 3 - Windows / Linux

import socket
import os 
import sys
import platform
import multiprocessing
import time
import urllib.request, urllib.parse, urllib.error
from colorama import Fore
def sus():
    print("[+] Public IP Address:",urllib.request.urlopen("http://ip.42.pl/raw").read())
    print("[+] Local IP Address:",socket.gethostbyname(socket.gethostname()))
    print("[+] Name: " +socket.gethostname()) 
    print("[+] FQDN: " +socket.getfqdn())
    print("[+] System Platform: "+sys.platform)
    print("[+] Machine: " +platform.machine())
    print("[+] Node: " +platform.node())
    print("[+] Platform: "+platform.platform())
    print("[+] Pocessor: " +platform.processor())
    print("[+] System OS: "+platform.system())
    print("[+] Release: " +platform.release())
    print("[+] Version: " +platform.version())
    print("[+] Number of CPU Core: " ,multiprocessing.cpu_count())
    print("[+] Date-Time: ",time.ctime())
    print("")
    print("")
    print("[!] Dont Copy Kid - I See You - Discord : MƦ.Ɗ3Ƒ417#8277")
    print("""
    
███╗░░░███╗██████╗░░░░██████╗░██████╗░███████╗░░██╗██╗░░███╗░░███████╗
████╗░████║██╔══██╗░░░██╔══██╗╚════██╗██╔════╝░██╔╝██║░████║░░╚════██║
██╔████╔██║██████╔╝░░░██║░░██║░█████╔╝█████╗░░██╔╝░██║██╔██║░░░░░░██╔╝
██║╚██╔╝██║██╔══██╗░░░██║░░██║░╚═══██╗██╔══╝░░███████║╚═╝██║░░░░░██╔╝░
██║░╚═╝░██║██║░░██║██╗██████╔╝██████╔╝██║░░░░░╚════██║███████╗░░██╔╝░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═════╝░╚═╝░░░░░░░░░░╚═╝╚══════╝░░╚═╝░░░  """)
    input('')

def passwords():
    data0 = platform.uname()[0]
    if data0 == 'Linux':
        os.system('clear')
    else:
        os.system('cls')
    p = input("Sir ! Enter the Password:")
    if p == 'blackguard':
        print(Fore.GREEN + '[+]' + Fore.WHITE + 'Wellcome Back ...')
        time.sleep(2)
        sus()
    else:
        print()
        print('Ops! This is not password')
        print()
        time.sleep(1)
        passwords()

passwords()
