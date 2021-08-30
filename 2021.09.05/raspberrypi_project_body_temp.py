import board
import adafruit_mlx90614
from rpi_lcd import LCD

from gpiozero import DistanceSensor
from gpiozero import LED
from gpiozero import Buzzer

from time import sleep

i2c = board.I2C()
distance_sensor = DistanceSensor(echo=21, trigger=20, max_distance=2.0)
mlx = adafruit_mlx90614.MLX90614(i2c)

lcd = LCD()
buzzer = Buzzer(23)
red_led = LED(17)
green_led = LED(27)
blue_led = LED(22)

while True:
    distance = distance_sensor.distance * 100
    sleep(1)
    if distance <= 10:
        my_temperature = mlx.object_temperature
        if my_temperature >= 35.0:
            red_led.on()
            green_led.off()
            blue_led.off()
            
            buzzer.on()
        
            lcd.text("    non-pass", 1)
            lcd.text(f'  Temp : {my_temperature:.1f}', 2)
        else:
            red_led.off()
            green_led.on()
            blue_led.off()
            
            buzzer.off()
                    
            lcd.text("      pass", 1)
            lcd.text(f'  Temp : {my_temperature:.1f}', 2)
    else:
        red_led.off()
        green_led.off()
        blue_led.on()           
        buzzer.off()

        lcd.text("      wait", 1)
        lcd.text(f'Distance : {distance:.1f}', 2)