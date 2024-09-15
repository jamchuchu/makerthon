from jikko.jikko import *
jk = Pyjikko()

#포트 번호 알맞게 바꾸기
PORT = 'COM7'
TEM_HUM = 4
NEO = 7

jk.serial_connect(PORT)
jk.start()

jk.lcd_set(0x27, 16, 2)
jk.neopixel_set(NEO, 4)

while True:
    T = jk.temp_read(TEM_HUM)
    H = jk.humi_read(TEM_HUM)
    jk.lcd_display(0,0,str(T))
    jk.lcd_display(0,1,str(H))

    if 40 < H < 60:
        jk.neopixel_display(NEO, 0,0,0,255)
    elif 60 < H < 80:
        jk.neopixel_display(NEO, 0,0,0,255)
        jk.neopixel_display(NEO, 1,0,0,255)
    elif 80 < H < 90:
        jk.neopixel_display(NEO, 0,0,0,255)
        jk.neopixel_display(NEO, 1,0,0,255)
        jk.neopixel_display(NEO, 2,0,0,255)
    elif 90 < H < 96:
        jk.neopixel_display_all(NEO, 0,0,0,255)

    time.sleep(1)
    jk.neopixel_clear(NEO)
    jk.lcd_clear()