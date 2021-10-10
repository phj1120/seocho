from gpiozero import LED
from time import sleep

r = LED(17)
y = LED(27)
g = LED(22)

while True:
    r.on()
    y.off()
    g.off()
    sleep(5)
    
    r.off()
    y.on()
    g.off()
    sleep(1)
    
    r.off()
    y.off()
    g.on()
    sleep(5)
    
    g_on = True
    for i in range(0, 5):
        r.off()
        y.off()
        if g_on:
            g.off()
            g_on = False
        else:
            g.on()
            g_on = True
        sleel(1)
        
        