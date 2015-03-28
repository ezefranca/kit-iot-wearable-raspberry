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

def setBuzzer(bleDevice, bleHandler, freq):
    command = "#BZ%d\r\n" %freq
    bleDevice.char_write(bleHandler, bytearray(command))

    return

def main():
    try:
        if sys.argv[1] == "--h":
            print "Antes de utilizar: forneca o endereco MAC Bluetooth Low Energy (BLE) do dispositivo wearable no arquivo bltAddrWearable.\n"
            print "Script setBuzzer: Aciona o buzzer com a frequencia desejada. Utilize com frequencia 0 para desligar."
            print "Exemplo: python setBuzzer.py 10000"
	    return
    except:
        print "Argumento inexistente. Use --h para obter ajuda."
	return

    bleBluetoothAddress = readAddr.main()

    if bleBluetoothAddress == 0:
        return
    
    freq = int(sys.argv[1])
    reset_bluetooth_controller()
    time.sleep(0.1)
    bleDevice = BluetoothLeDevice(bleBluetoothAddress)
    bleHandler = 0x11

    setBuzzer(bleDevice, bleHandler, freq)

main()
