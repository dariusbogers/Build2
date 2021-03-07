from lora import connect_LoRa
from wifi import *
from pycom import *
from time import sleep

#wifis = [["Bogers's Apple Airport",'Pass'],["IoT",'KdGIoT92!']]
#
#connectWifi(wifis)
heartbeat(False)
for i in range(10):
    print(i)
    sleep(1)
connect_LoRa()
