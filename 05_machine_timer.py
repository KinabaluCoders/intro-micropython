# 05 : machine library, and timer

from machine import Pin
import time

led = Pin("LED", Pin.OUT)

while True:
    led.toggle()
    time.sleep(0.4)  # 1 / 2.5 Hz = 0.4 seconds
