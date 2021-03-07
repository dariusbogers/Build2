from network import LoRa
import socket
from time import sleep
import binascii
from pycom import *

s = None

def connect_LoRa():
    global s
    heartbeat(False)
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

    appeui = binascii.unhexlify("70B3D57ED003E4DE")
    appkey = binascii.unhexlify("1A91C6E322D56238F014D27026E00930")

    lora.join(activation=LoRa.OTAA, auth=(appeui,appkey))

    while not lora.has_joined():
        sleep(2.5)
        print("not connected")

    print("connected")

    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(True)


def lora_send(string):
    s.send(bytes(string.encode('ascii')))