from jikko.jikko import *
jk= Pyjikko()

PORT='COM9'
NEO=7
CDS=A0

jk.serial_connect(PORT)
jk.start()

jk.neopixel_set(NEO,4)

while True:
    light=jk.cds_read(CDS)
    print(light)
    
    if light < 200:
        jk.neopixel_display_all(NEO,0,255,0)
        time.sleep(1)
    elif 200<= light < 400 :
        jk.neopixel_display(NEO,0,255,255,255)
        jk.neopixel_display(NEO,1,255,255,255)
        time.sleep(1)
    else:
        jk.neopixel_display_all(NEO,0,255,0)
        time.sleep(1)
        jk.neopixel_clear(NEO)