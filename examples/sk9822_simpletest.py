import time
import random
import board
import adafruit_sk9822 as sk9822


# With an SK9822 Strip with 30 lights
dots = sk9822.SK9822(board.SCK, board.MOSI, 30, brightness=1.0)

######################### HELPERS ##############################

# a random color 0 -> 224
def random_color():
    return random.randrange(0, 7) * 32


######################### MAIN LOOP ##############################
n_dots = len(dots)
while True:
    # fill each dot with a random color
    for dot in range(n_dots):
        dots[dot] = (random_color(), random_color(), random_color())

    # show all dots in strip
    dots.show()

    time.sleep(.25)
