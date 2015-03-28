"""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ Biblioteca Python para manipulacao do Kit Wearable da Telefonica @
@ Renan Yuri Lino - renan.lino@gmail.com                           @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Script auxilixar para leitura do endereco BLE do dispositivo Wearable
"""

def main():
    try:
        addrFile = open("bltAddrWearable","r")
    except IOError:
        print("Leitura do endereco BLE falhou!")
        return 0
    bleBluetoothAddress = addrFile.readline()
    addrFile.close()
    bleBluetoothAddress = bleBluetoothAddress.split()[0]

    return bleBluetoothAddress
