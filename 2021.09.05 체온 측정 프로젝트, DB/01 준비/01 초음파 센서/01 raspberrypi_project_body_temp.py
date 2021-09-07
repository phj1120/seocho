import board
import adafruit_mlx90614
from rpi_lcd import LCD

from gpiozero import DistanceSensor
from gpiozero import LED
from gpiozero import Buzzer

from time import sleep

i2c = board.I2C()
mlx = adafruit_mlx90614.MLX90614(i2c)
lcd = LCD()

distance_sensor = DistanceSensor(echo=21, trigger=20, max_distance=2.0)
buzzer = Buzzer(23)
red_led = LED(17)
green_led = LED(27)
blue_led = LED(22)

while True:
    # 거리 측정
    distance = distance_sensor.distance * 100
    # 1ms 대기
    sleep(1)
    # 물체가 일정 거리 안에 들어 올 경우
    if distance <= 10:
        # 온도 체크 시작
        temp = mlx.object_temperature

        # 일정 온도 이상인 경우
        if temp >= 35.0:

            red_led.on()
            green_led.off()
            blue_led.off()
            
            buzzer.on()
        
            lcd.text("    non-pass", 1)
            lcd.text(f'  Temp : {temp:.1f}', 2)
        # 일정 온도 이하인 경우
        else:
            red_led.off()
            green_led.on()
            blue_led.off()
            
            buzzer.off()
                    
            lcd.text("      pass", 1)
            lcd.text(f'  Temp : {temp:.1f}', 2)
    # 일정 거리 안에 물체가 없을 경우
    else:
        red_led.off()
        green_led.off()
        blue_led.on()

        buzzer.off()

        lcd.text("      wait", 1)
        lcd.text(f'Distance : {distance:.1f}', 2)