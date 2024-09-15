from jikko.jikko import *
jk= Pyjikko()

PORT='COM9'
NEO=7
RX=10
TX=11
CDS=A0

jk.serial_connect(PORT)
jk.start()

jk.lcd_set(0x27,16,2)
jk.neopixel_set(NEO,4)
jk.neopixel_bright(NEO,20)
jk.mp3_set(RX,TX)
jk.mp3_volume(30)

while True:
    light=jk.cds_read(CDS)
    
    if light>=500 :
        jk.neopixel_display_all(NEO,255,0,0)
        jk.mp3_play(2)
        time.sleep(1)
        jk.neopixel_display_all(NEO,0,0,255)
        time.sleep(1)
    else :
        jk.neopixel_clear(NEO)
