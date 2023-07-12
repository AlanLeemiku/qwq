from time import sleep_us
from machine import time_pulse_us
from microbit import *

class HCSR04():

    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo

    def getDistance(self):
        distance = 0
        self.echo.read_digital()
        self.trig.write_digital(1)
        sleep_us(10)
        self.trig.write_digital(0)
        distance = time_pulse_us(self.echo, 1, 5000)
        if distance > 0: 
            distance=distance * 17 // 1000
        return distance


# 这一句很重要
uart.init(115200)
display.off()
#pin10.write_digital(0)
#pin6.write_digital(1)
HC = HCSR04(pin10, pin6)

while True:
    distance = HC.getDistance()
