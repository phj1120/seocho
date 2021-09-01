from gpiozero import Button, LED
from subprocess import check_call
from signal import pause

led = LED(17)

def call():
    led.on()
    check_call(["raspistill", "-o", "test.jpg"])
    led.off()
    
button = Button(27, hold_time=2)
button.when_held = call

pause