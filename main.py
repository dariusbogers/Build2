import ultrasonic
from wifi import *
from time import sleep

connectWifi("Bogers's Apple Airport",'$passwd')

ultrasonic.defuart()

while True:
    ultrasonic.checkheader()
    ultrasonic.distanceString()
    sleep(0.01)