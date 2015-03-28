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
	if sys.argv[1] == "X":
	    command = "#AC0000\r\n"
	elif sys.argv[1] == "Y":
	    command = "#AC0001\r\n"
	elif sys.argv[1] == "Z":
            command = "#AC0002\r\n"
        elif sys.argv[1] == "--h":
            print "Antes de utilizar: forneca o endereco MAC Bluetooth Low Energy (BLE) do dispositivo wearable no arquivo bltAddrWearable.\n"
            print "Script getAcel: Dado um argumento valido (X, Y ou Z) imprime a resposta do dispositivo para a aceleracao"
            print "no eixo solicitado."
            print "Exemplo: python getAcel.py X"
            return
        else:
            print "Argumento invalido. Forneca X, Y, Z ou --h para obter ajuda"
            return
    except:
	print "Erro: Falta de argumento para chamada. Use python getAcel.py --h para exibir ajuda."
        return

    
    bleBluetoothAddress = readAddr.main()

    if bleBluetoothAddress == 0:
        return
    
    reset_bluetooth_controller()
    time.sleep(0.1)
    bleDevice = BluetoothLeDevice(bleBluetoothAddress)
    bleHandler = 0x11
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
