from gpiozero import AngularServo
from time import sleep

servo = AngularServo(16, min_angle=-40, max_angle=40)

while True:
	servo.angle = -30
	sleep(2)
	servo.angle = 0
	sleep(2)
	servo.angle = 30
	sleep(2)
