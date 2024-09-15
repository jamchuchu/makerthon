from jikko.jikko import *
jk = Pyjikko()

PORT = 'COM9'
SOIL = A1
SERVO = 8
CDS = A0
NEO = 7
TEM_HUM = 4

jk.serial_connect(PORT)
jk.start()

jk.lcd_set(0x27, 16, 2)
jk.neopixel_set(NEO, 4)
jk.neopixel_bright(NEO, 30)

while True:
    temp = jk.temp_read(TEM_HUM)
    humi = jk.humi_read(TEM_HUM)
    water = jk.soil_read(SOIL)
    light = jk.cds_read(CDS)
    
    jk.lcd_display(0,0,str(light))
    jk.lcd_display(0,1,str(water))

    if light > 500:
        jk.neopixel_display_all(NEO, 255, 255, 0)
    else :
        jk.neopixel_clear(NEO)

    if water > 800:
        jk.servo_degree(SERVO, 90)
        time.sleep(1)
    else:
        jk.servo_degree(SERVO, 0)
        time.sleep(1)

    jk.lcd_clear()