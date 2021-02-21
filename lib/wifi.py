from pycom import *
from network import WLAN
from time import sleep
def connectWifi(ssid,passwd):
    heartbeat(False)
    wlan = WLAN(mode=WLAN.STA)
    wlan.connect(ssid, auth=(WLAN.WPA2,passwd))
    while not wlan.isconnected():
        rgbled(0xFF00000)
        sleep(0.5)
        rgbled(0xFFFF00)
        sleep(0.5)

    rgbled(0x00FF00)
    print(wlan.ifconfig())
