from gpiozero import LED
from time import sleep
from signal import pause

led = LED(17)

led.blink()

pause()
