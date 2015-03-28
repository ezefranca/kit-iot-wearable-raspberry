#!/bin/python
"""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ Biblioteca Python para manipulacao do Kit Wearable da Telefonica @
@ Renan Yuri Lino - renan.lino@gmail.com                           @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
from pygatt.pygatt import *
import bluetooth
import sys
import time
import readAddr

def main():
    
    try:
        if sys.argv[1] == "--h":
            print "Antes de utilizar: forneca o endereco MAC Bluetooth Low Energy (BLE) do dispositivo wearable no arquivo bltAddrWearable.\n"
            print "Script sendCommand: Envia um comando qualquer para o dispositivo wearable. Digite apenas o comando, o programa ja envia os caracteres '#' e '/r/n' automaticamente."
            print "Exemplo: python sendCommand.py LR255"
            return         
    except:
        print "Argumento inexistente. Use --h para obter ajuda."
	return

    bleBluetoothAddress = readAddr.main()

    if bleBluetoothAddress == 0:
        return
    
    command = "#" + sys.argv[1] + "\r\n"
    reset_bluetooth_controller()
    time.sleep(0.1)
    bleDevice = BluetoothLeDevice(bleBluetoothAddress)
    bleHandler = 0x11
    bleDevice.char_write(bleHandler, bytearray(command))

main()
