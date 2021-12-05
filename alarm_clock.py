def binary_minutes():
    pass
def tick():
    global seconds, minutes, hours
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if hours == 24:
        hours = 0
def display_time():
    if display_mode == 0:
        display_binary()
    else:
        display_decimal()
def display_binary():
    binary_hours()
    binary_minutes()
    binary_seconds()

def on_logo_long_pressed():
    global mode
    mode = 1
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def get_brightness():
    if brightness_mode == 0:
        return input.light_level()
    else:
        return 255

def on_button_pressed_a():
    global display_mode
    if mode == 0:
        if display_mode == 0:
            display_mode = 1
        else:
            display_mode = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def binary_seconds():
    for index in range(11):
        led.plot_brightness(index % 5,
            index / 5,
            Math.map(Math.constrain(seconds - index * 6, 0, 0),
                0,
                6,
                0,
                get_brightness()))
def play_alarm():
    for index2 in range(4):
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(220, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(220, music.beat(BeatFraction.WHOLE))
        music.play_melody("C5 B A C5 B C5 C5 C5 ", 500)
        for index3 in range(2):
            music.change_tempo_by(100)
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
            music.play_tone(220, music.beat(BeatFraction.WHOLE))
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
            music.play_tone(220, music.beat(BeatFraction.WHOLE))
            music.play_melody("C5 B A C5 B C5 C5 C5 ", 400)
            music.play_tone(523, music.beat(BeatFraction.BREVE))
        for index4 in range(4):
            music.play_tone(880, music.beat(BeatFraction.DOUBLE))
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
            music.play_tone(220, music.beat(BeatFraction.WHOLE))
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
            music.play_tone(220, music.beat(BeatFraction.WHOLE))
            music.play_melody("C5 B A C5 B C5 C5 C5 ", 500)

def on_button_pressed_ab():
    global mode
    mode = 2
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_shake():
    global brightness_mode
    if brightness_mode == 0:
        brightness_mode = 1
    else:
        brightness_mode = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def binary_hours():
    pass
def display_decimal():
    pass
brightness_mode = 0
display_mode = 0
mode = 0
hours = 0
minutes = 0
seconds = 0
seconds = 0
minutes = 0
hours = 0
mode = 0
play_alarm()

def on_forever():
    if mode == 0:
        basic.pause(1000)
        tick()
    display_time()
basic.forever(on_forever)
