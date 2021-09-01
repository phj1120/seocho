from gpiozero import TonalBuzzer
from time import sleep

bz = TonalBuzzer(16)
bz.play(220.0)
sleep(5)
bz.stop()
