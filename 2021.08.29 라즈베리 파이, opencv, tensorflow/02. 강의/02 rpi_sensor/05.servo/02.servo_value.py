from gpiozero import Servo
from time import sleep

servo = Servo(16)

while True:
	servo.value = -1
	sleep(2)
	servo.value = 0
	sleep(2)
	servo.value = 1
	sleep(2)
