import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value #get the volume from the microphone
    num_leds_on = int((volume / 48813) * len(leds)) #the number of LEDs to turn on based on the volume level from the microphone
    #num_leds_on max is 11 (0 to 10) 
    for i, led in enumerate(leds): #index of each LED (i) and the LED (led) 
        if i < num_leds_on: #turns on the leds given the volume
            led.value = True #for example: led1 is on 
        else: #stops when we've reached the number of LEDs 
            led.value = False
    print(volume) 
    sleep(0.1)  

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?

