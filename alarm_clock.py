from microbit import *
import music

ORIGIN = 0
ALARM_ORIGIN = 0
MODE = 'run'

def time(milliseconds):
    seconds = milliseconds // 1000
    return (
        seconds // 3600 % 24,
        (seconds // 60) % 60,
        seconds % 60
    )

def show(num, y_offset, num_pixels, max_value):
    brightness_levels = max_value // num_pixels
    whole = num // brightness_levels
    part = int((num / brightness_levels - whole) * 9)
    for index in range(max_value // brightness_levels):
        x, y = index % 5, y_offset + index // 5
        if index < whole:
            display.set_pixel(x, y, 9)
        elif index == whole:
            display.set_pixel(x, y, part)
        else:
            display.set_pixel(x, y, 0)

def show_time(h, m, s):
    show(s, 0, 5, 60)
    show(m, 1, 10, 60)
    h = '{:05b}'.format(h)
    for i in range(5):
        if h[i] == '0':
            display.set_pixel(i, 4, 0)
        else:
            display.set_pixel(i, 4, 9)

def play_alarm():
    tempo = 120
    for _ in range(4):
        music.set_tempo(bpm=500)
        music.pitch(262, 1 * 60000 // tempo)
        music.pitch(220, 1 * 60000 // tempo)
        music.pitch(262, 1 * 60000 // tempo)
        music.pitch(220, 1 * 60000 // tempo)
        music.play('C5 B A C5 B C5 C5 C5 '.split())
        for _ in range(2):
            tempo += 100
            music.pitch(262, 1 * 60000 // tempo)
            music.pitch(220, 1 * 60000 // tempo)
            music.pitch(262, 1 * 60000 // tempo)
            music.pitch(220, 1 * 60000 // tempo)
            music.set_tempo(bpm=400)
            music.play('C5 B A C5 B C5 C5 C5 '.split())
            music.pitch(523, 4 * 60000 // tempo)
        for _ in range(4):
            music.pitch(880, 2 * 60000 // tempo)
            music.pitch(262, 1 * 60000 // tempo)
            music.pitch(220, 1 * 60000 // tempo)
            music.pitch(262, 1 * 60000 // tempo)
            music.pitch(220, 1 * 60000 // tempo)
            music.set_tempo(bpm=500)
            music.play('C5 B A C5 B C5 C5 C5 '.split())
        if button_a.is_pressed() or button_b.is_pressed():
            break
    
alarm_armed = False
last_alarm = running_time()

while True:
    H, M, S = time(ORIGIN)
    if pin_logo.is_touched():
        if MODE == 'run':
            MODE = 'adjust'
        elif MODE == 'adjust':
            MODE = 'adjust-alarm'
        else:
            MODE = 'run'
        display.scroll(MODE, delay=50)
    if MODE == 'adjust':
        if button_a.is_pressed():
            ORIGIN += 60000
        elif button_b.is_pressed():
            ORIGIN -= 60000
        sleep(100)
    if MODE == 'adjust-alarm':
        alarm_armed = True
        if accelerometer.was_gesture('shake'):
            display.scroll('ALARM CLEARED')
            alarm_armed = False
            MODE = 'run'
        if button_a.is_pressed():
            ALARM_ORIGIN += 60000
        elif button_b.is_pressed():
            ALARM_ORIGIN -= 60000
        show_time(*time(ALARM_ORIGIN))
        sleep(100)
        continue
    h, m, s = time(running_time())
    h += H
    m += M
    print(alarm_armed)
    print(h, m, *time(ALARM_ORIGIN)[:2])
    if (h, m) == time(ALARM_ORIGIN)[:2] and alarm_armed:
        if -60000 < running_time() - last_alarm <  60000:
            pass
        else:
            print('ALARM')
            play_alarm()
            last_alarm = running_time()
    show_time(h, m, s)