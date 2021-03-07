from pycom import *
from network import WLAN
from time import *
import urequests as requests
wlan = WLAN(mode=WLAN.STA)
def Wifi(ssid,passwd):
    global wlan
    heartbeat(False)
    wlan.connect(ssid, auth=(WLAN.WPA2,passwd))
    endt = time() + 30
    while time() < endt and not wlan.isconnected():
        rgbled(0xFF00000)
        sleep(0.5)
        rgbled(0xFFFF00)
        sleep(0.5)
    if wlan.isconnected():
        rgbled(0x00FF00)
        print(wlan.ifconfig())
    else:
        print("not connected")

def connectWifi(wifis):
    while not wificonnected():
        for i in wifis:
            if not wificonnected():
                print(i[0])
                print(i[1])
                try:
                    Wifi(i[0],i[1])
                except OSError:
                    print('not connected')

def wifi_send(url,string):
    requests.post(url, data=string)

def wificonnected():
    return wlan.isconnected()