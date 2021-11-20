import os
import platform
import getpass
import colorama
from colorama import Fore,Back,Style 
colorama.init()
def printlogo():
        print("""                .--.          .--.            .;'  ,;'             `;,  `;,        """, Fore.MAGENTA)
        print("""        _     _ |__|     _.._ |__|          .;'  ,;'  ,;'     `;,  `;,  `;,        """, Fore.GREEN)
        print("""   /\   \\\   //.--.   .' .._|.--.           ::   ::   :   ( )   :   ::   ::  automated wireless auditor """, Fore.RED)
        print("""   `\\\  //\\ // |  |   | '    |  |           ':.  ':.  ':. /_\ ,:'  ,:'  ,:'       """, Fore.WHITE)
        print("""     \`//  \'/  |  | __| |__  |  | 	       ':.  ':.  /___\    ,:'  ,:'   designed for windows      """,Fore.YELLOW)
        print("""      \\|  |/   |  ||__   __| |  |             ':.       /_____\      ,:'          by @peiris""", Fore.BLUE)
        print("""       '       |  |   | |    |  |                      /       \                 """, Fore.MAGENTA)
        print("""               |__|   | |    |__|                                              """, Fore.RED)
        print("""                      | |                                                      """, Fore.WHITE)
        print("""                      | |                                                     """, Fore.YELLOW)
        print("""                      |_|                                                      """, Fore.GREEN)                                                                         
        print('\n')
printlogo()
y = "y"
Y = "Y"
n = "n"
N = "N"
def createNewConnection(name, SSID, key):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>"""+name+"""</name>
    <SSIDConfig>
        <SSID>
            <name>"""+SSID+"""</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>"""+key+"""</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
    if platform.system() == "Windows":
        command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
        with open(name+".xml", 'w') as file:
            file.write(config)
    elif platform.system() == "Linux":
        command = "nmcli dev wifi connect '"+SSID+"' password '"+key+"'"
    os.system(command)
    if platform.system() == "Windows":
        os.remove(name+".xml")

def connect(name, SSID):
    if platform.system() == "Windows":
        command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
    elif platform.system() == "Linux":
        command = "nmcli con up "+SSID
    os.system(command)

def displayAvailableNetworks():
    if platform.system() == "Windows":
        command = "netsh wlan show networks interface=Wi-Fi"
    elif platform.system() == "Linux":
        command = "nmcli dev wifi list"
    os.system(command)

try:
    displayAvailableNetworks()
    option = input("New connection (y/N)? ")
    if option == n or option == N:
        name = input("Name: ")
        connect(name, name)
        print("If you aren't connected to this network, try connecting with correct credentials")
    elif option == y or option == Y:
        name = input("Name: ")
        f=open('pass.txt','r')
        #record=f.readline()
        #while record:
        try:
            key = f.read()
            createNewConnection(name, name, key)
            connect(name, name)
            print("If you aren't connected to this network, try connecting with correct credentials")
        except:
            print("password rong")
        f.close()
        #key = getpass.getpass("Password: ")
        #createNewConnection(name, name, key)
        #connect(name, name)
        #print("If you aren't connected to this network, try connecting with correct credentials")
except KeyboardInterrupt as e:
    print("\nExiting...")
