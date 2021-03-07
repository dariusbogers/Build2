from lib.wifi import wifi_send
from lib.lora import lora_send
import ultrasonic
from wifi import *
from lora import *
from time import *


# --- Connecting To Wifi Is Requered In The Main If In Boot |wifi_send| Doesn't Work --- #
wifis = [["Bogers's Apple Airport",'Pass'],["IoT",'KdGIoT92!']]

connectWifi(wifis)

ultrasonic.defuart()

endt = time() + 5
while time() < endt:
    ultrasonic.checkheader()

sendstr = ultrasonic.distanceString()
lora_send(sendstr)
wifi_send("https://4b23011d715a9203be6718bde016c900.m.pipedream.net", sendstr)


#while True:
#    sleep(0.01)
#    ultrasonic.checkheader()
#    print(ultrasonic.distanceString())