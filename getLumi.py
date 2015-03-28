#!/bin/python
"""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ Biblioteca Python para manipulacao do Kit Wearable da Telefonica @
@ Renan Yuri Lino - renan.lino@gmail.com                           @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
from pygatt.pygatt import *
import bluetooth
import time
import sys
import readAddr

def main():

    try:
        if sys.argv[1] == "--h":
            print "Antes de utilizar: forneca o endereco MAC Bluetooth Low Energy (BLE) do dispositivo wearable no arquivo bltAddrWearable.\n"
            print "Script getLumi: Imprime a resposta do sensor de luminosidade do kit wearable."
            print "Exemplo: python getLumi.py"
        else:
            print "Argumento invalido. Use --h para obter ajuda."
	return
    except:
        pass

    bleBluetoothAddress = readAddr.main()

    if bleBluetoothAddress == 0:
        return

    reset_bluetooth_controller()
    time.sleep(0.1)
    bleDevice = BluetoothLeDevice(bleBluetoothAddress)
    bleHandler = 0x11
    command = "#LI0000\r\n"
    bleDevice.char_write(bleHandler, bytearray(command), wait_for_response = True)
    try:
        reply = bleDevice.char_write(bleHandler, bytearray(command), get_response = True)
        reply = str(reply)
    except:
        reply = ""
    if len(reply) > 0:
        reply = reply.split()
        print reply[1]
    else:
        print "Erro: sem resposta do dispositivo."

main()
