print('''\033[1;31m \n
    _                                    ____         
   (_)___        _________  ____  ____  / __/__  _____
  / / __ \______/ ___/ __ \/ __ \/ __ \/ /_/ _ \/ ___/
 / / /_/ /_____(__  ) /_/ / /_/ / /_/ / __/  __/ /    
/_/ .___/     /____/ .___/\____/\____/_/  \___/_/     
 /_/              /_/                                     
    Automatically Change Ip Address And Spoof Your Location #DEADSEC-HACKER
''')

def install_lib(lib_name):
    try:
        subprocess.check_output(['pip', 'show', lib_name])
        print('[+]', lib_name, 'is already installed')
    except subprocess.CalledProcessError:
        print('[+]', lib_name, 'is not installed')
        subprocess.check_output(['sudo', 'apt', 'update'])
        subprocess.check_output(['sudo', 'pip', 'install', lib_name, '-y'])
        print('[!]', lib_name, 'installed successfully')

# Rest of your code...

def install_package(package_name):
    try:
        subprocess.check_output(['dpkg', '-s', package_name])
        print('[+]', package_name, 'is already installed')
    except subprocess.CalledProcessError:
        print('[+]', package_name, 'is not installed')
        subprocess.check_output(['sudo', 'apt', 'update'])
        subprocess.check_output(['sudo', 'apt', 'install', package_name, '-y'])
        print('[!]', package_name, 'installed successfully')

def main():
   
    install_package('python3-pip')
    install_package('tor')
    interface = input("Enter Your Wireless Interface Name: ")
    os.system("clear")
    banner = "DEADSEC-HACKER"
    print(Box.Lines(banner))
    os.system("service tor start")
    time.sleep(3)
    print("\033[1;32;40m Change your SOCKS to 127.0.0.1:9050\n")
    os.system("service tor start")
    x = input("[+] Time to change IP in seconds [type=60] >> ")
    lin = input("[+] How many times do you want to change your IP [type=1000] For infinite IP change, type [0] >> ")
    os.system('clear')
    print(Box.Lines(banner))
    print("\033[1;32;40m Change your SOCKS to 127.0.0.1:9050\n")
    if int(lin) == 0:
        while True:
            try:
                change_ip()
                time.sleep(int(x))
            except KeyboardInterrupt:
                print('\nAuto TOR is closed.')
                quit()
    else:
        for i in range(int(lin)):
            change_ip()
            time.sleep(int(x))

def change_ip():
    os.system("service tor reload")
    print('[+] Your IP has been changed to: ' + str(get_ip()))
import subprocess

def install_packages(package_name):
    try:
        subprocess.check_output(['pip', 'show', package_name])
        print('[+]',package_name,'is already installed')
    except subprocess.CalledProcessError:
        print('[+]',package_name,'is not installed')
        subprocess.check_output(['pip', 'install', package_name])
        print('[!]',package_name,'installed successfully')


def get_ip():
    url = 'https://api.ipify.org'
    response = requests.get(url, proxies={'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'})
    return response.text

if __name__ == '__main__':
    packages_to_install = ['pystyle', 'colorama','requests']

    for package in packages_to_install:
        install_packages(package)
    
    import time
    import os
    import subprocess
    import requests
    import random
    from pystyle import *
    from colorama import Fore, Back, Style
    from colorama import init
    init(autoreset=True)
    main()
