#!/bin/python

from pygatt.pygatt import *
import bluetooth
import sys
import time
import readAddr

def wait4Button(bleDevice, bleHandler):
    time.sleep(0.5)
    command = ""
    try:
        reply = bleDevice.char_write(bleHandler, bytearray(command), get_response = True)
        reply = str(reply)
        reply = reply.split()
        reply = reply[0].split("#B")
        reply = reply[1]
    except:
        reply = 0
    return reply

def main():
    try:
        if sys.argv[1] == "--h":
            print "Antes de utilizar: forneca o endereco MAC Bluetooth Low Energy (BLE) do dispositivo wearable no arquivo bltAddrWearable.\n"
            print "Script waitButton: Aguarda o pressionamento de um botao no kit wearable e imprime o numero do botao pressionado. Caso nenhum botao seja pressionado apos o timeout o programa imprime o numero 0."
            print "Exemplo: python waitButton.py"
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

    print wait4Button(bleDevice, bleHandler)

main()
