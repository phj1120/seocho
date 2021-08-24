from gpiozero import LED
from gpiozero import Button
from signal import pause

led = LED(17)
button = Button(27)
status = False

def on_off():
    global status
    
    if status:
        led.off()
    else:
        led.on()
    status = not status

button.when_released = on_off

pause()
