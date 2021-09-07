import board, adafruit_mlx90614
from gpiozero import DistanceSensor, LED, Buzzer
from rpi_lcd import LCD
from time import sleep


def my_status(buzzer_state=False, red_led_state=False, green_led_state=False, blue_led_state=False, lcd_text=['','']):
    buzzer.on() if buzzer_state else buzzer.off()
    red_led.on() if red_led_state else red_led.off()
    green_led.on() if green_led_state else green_led.off()
    blue_led.on() if blue_led_state else blue_led.off()
    lcd.text(lcd_text[0], 1)
    lcd.text(lcd_text[1], 2)

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
    if distance <= 30 and distance >= 20:
        # 온도 측정
        temp = mlx.object_temperature
        # 일정 온도 이상인 경우
        if temp >= 33.0:
            my_status(buzzer_state=True, red_led_state=True, lcd_text=['    non-pass', f'  Temp : {temp:.1f}'])
       # 일정 온도 이하인 경우
        else:
            my_status(green_led_state=True, lcd_text=['      pass', f'  Temp : {temp:.1f}'])
            my_temp = 0
    # 일정 거리 안에 물체가 없을 경우
    else:
        my_status(blue_led_state=True, lcd_text=['      wait', f'Distance : {distance:.1f}'])