from gpiozero import LED
from gpiozero import Button
from signal import pause

led = LED(17)
button = Button(27)

button.when_pressed = led.on
button.when_released = led.off

pause
