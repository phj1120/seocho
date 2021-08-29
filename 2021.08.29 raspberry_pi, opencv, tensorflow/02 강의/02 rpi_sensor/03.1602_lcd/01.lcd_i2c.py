# sudo pip3 install rpi_lcd

from rpi_lcd import LCD


lcd = LCD()
lcd.text("How are you?", 1)
lcd.text("Nice to meet you", 2)