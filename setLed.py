#!/bin/python

from pygatt.pygatt import *
import bluetooth
import time
import sys
import readAddr

def RGBLed(bleDevice, bleHandler, intR, intG, intB):

    #Define a intensidade do LED Red
    command = "#LR%d\r\n" % (intR)
    bleDevice.char_write(bleHandler, bytearray(command))

    #Define a intensidade do LED Blue
    command = "#LG%d\r\n" % (intG)
    bleDevice.char_write(bleHandler, bytearray(command))

    #Define a intensidade do LED Green
    command = "#LB%d\r\n" % (intB)
    bleDevice.char_write(bleHandler, bytearray(command))

    return

def main():
    try:
        if sys.argv[1] == "--h":
            print "Antes de utilizar: forneca o endereco MAC Bluetooth Low Energy (BLE) do dispositivo wearable no arquivo bltAddrWearable.\n"
            print "Script setLed: Configura a intensidade dos LEDs RGB na sequencia R G B. Utilize um numero no intervalo 0 a 255 para cada cor"
            print "Exemplo: python setLed.py 255 0 0 (LED vermelho com intensidade maxima e os outros apagados)"
	    return          
    except:
        print "Argumento inexistente. Use --h para obter ajuda."
	return

    bleBluetoothAddress = readAddr.main()

    if bleBluetoothAddress == 0:
        return
    
    intR = int(sys.argv[1])
    intG = int(sys.argv[2])
    intB = int(sys.argv[3])
    reset_bluetooth_controller()
    time.sleep(0.1)
    bleDevice = BluetoothLeDevice(bleBluetoothAddress)
    bleHandler = 0x11

    RGBLed(bleDevice, bleHandler, intR, intG, intB)

main()
