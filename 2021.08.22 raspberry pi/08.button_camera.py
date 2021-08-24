from gpiozero import Button, LED
from picamera import PiCamera
from datetime import datetime
from signal import pause

led = LED(17)
button = Button(27)
camera = PiCamera()

def capture():
    led.on()
    timestamp = datetime.now().isoformat()
    camera.capture("/home/pi/%s.jpg" % timestamp)
    #camera.capture(f"/home/pi/{timestamp}.jpg")
    #camera.capture("/home/pi/{}.jpg".format(timestamp))
    led.off()
    
button.when_released = capture

pause()
