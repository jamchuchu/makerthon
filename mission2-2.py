from jikko.jikko import *
jk = Pyjikko()

PORT = 'COM9'
LED = 5
BUZZER = 6

jk.serial_connect(PORT)
jk.start()

while True:
    distance = jk.sonic_read(TRIG, ECHO)
    jk.lcd_display(0,0,str(distance))
    time.sleep(1)
    
    if distance < 20