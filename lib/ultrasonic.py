from machine import UART

header = None
high = None
low = None
checksum = None
uart = None

def defuart():
    global uart
    uart = UART(1)
    uart.init(baudrate=9600, bits=8, parity=None, stop=1, timeout_chars=100, pins=('P3','P4'))

    

def getread():
    global header, high, low, checksum
    for i in range(4):
        if i == 0:
            header = int(uart.read(1)[0])
        if i == 1:
            high = int(uart.read(1)[0]*256)
        if i == 2:
            low = int(uart.read(1)[0])
        if i == 3:
            checksum = int(uart.read(1)[0])

def getDistance(dHigh, dLow):
    return dHigh+dLow

def getLogicInfo():
    print('Header value is: ' + str(header))
    print('Data high value is: ' + str(high))
    print('Data low value is: ' + str(low))
    print('Data checksum value is: ' + str(checksum))
    print('Distance is: ' + str(getDistance(high, low)) + 'mm')

def distanceString():
    distance = getDistance(high, low)
    if distance < 1000:
        return('The distance is ' + str(distance/10) + 'cm')
    else:
        return('The distance is ' + str(distance/1000) + 'm')

def checkheader():
    getread()
    while header != 255:
        getread()