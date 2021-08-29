from gpiozero import Buzzer
from time import sleep

bz = Buzzer(16)
bz.on()
sleep(5)
bz.off()
bz.close()
