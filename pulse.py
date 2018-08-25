import RPi.GPIO as gpio
import time

SleepTime=2

gpio.cleanup()

gpio.setmode(gpio.BCM)
gpio.setup(4,gpio.OUT)

gpio.output(4,True)
time.sleep(SleepTime)
gpio.output(4,False)

gpio.cleanup()