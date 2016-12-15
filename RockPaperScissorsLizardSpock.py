#Rock, Paper, Scissors, Lizard, Spock

import random
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
sense.show_message("Ready, set, shake!", scroll_speed=0.08, text_colour = (150, 0, 150))
#wait while the user shakes to select an answer
time.sleep(1)

# set variables for LED block colours
r = (155, 100, 69)  # rock colour
p = (255,255,255) # paper colour
sh = (255,0,0) # scissors handle colour
sb = (192,192,192) # scissors blade colour
l = (0,255,0) #lizard colour
sp = (0,0,255) #spock colour
b = (0, 0, 0)  # background colour

# define the shape of the possible responses
rock = [[b,b,b,b,b,b,b,b],
        [b,b,b,r,r,b,b,b],
        [b,b,r,r,r,b,b,b],
        [b,r,r,r,r,r,b,b],
        [b,r,r,r,r,r,r,b],
        [b,b,b,r,r,r,r,b],
        [b,b,b,r,r,r,b,b],
        [b,b,b,b,b,b,b,b]]

print("rock")

paper = [[b,p,p,p,p,p,p,b],
        [b,p,p,p,p,p,p,b],
        [b,p,p,p,p,p,p,b],
        [b,p,p,p,p,p,p,b],
        [b,p,p,p,p,p,p,b],
        [b,p,p,p,p,p,p,b],
        [b,p,p,p,p,p,p,b],
        [b,p,p,p,p,p,p,b]]

print("paper")

scissors = [[b,b,b,b,b,b,b,b],
        [sh,sh,sh,b,b,b,b,sb],
        [sh,b,sh,b,b,b,sb,b],
        [sh,sh,sh,sb,b,sb,b,b],
        [b,b,b,b,sb,sb,b,b],
        [sh,sh,sh,sb,b,sb,b,b],
        [sh,b,sh,b,b,b,sb,b],
        [sh,sh,sh,b,b,b,b,sb]]

print("scissors")

lizard = [[l,b,b,b,l,b,b,l],
        [l,b,b,b,l,b,b,l],
        [l,b,b,b,b,l,l,b],
        [b,l,b,b,b,l,l,l],
        [b,l,l,l,l,l,b,b],
        [l,l,l,l,l,l,b,b],
        [l,b,l,b,l,b,l,b],
        [l,b,l,b,l,b,l,b]]

print("lizard")

spock = [[b,b,b,b,b,sp,b,b],
        [b,b,b,b,sp,sp,b,b],
        [b,b,b,sp,b,sp,b,b],
        [b,b,sp,b,b,sp,b,b],
        [b,b,sp,sp,b,sp,b,b],
        [b,b,sp,b,b,sp,b,b],
        [b,b,sp,sp,sp,b,b,b],
        [b,b,b,sp,sp,b,b,b]]

print("spock")

shake = [rock,
          paper,
          scissors,
          lizard,
          spock]
AI = random.choice(shake)

#show a message when shaken
while True:
    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 2 or y > 2 or z > 2:
        sense.set_pixels(sum(AI,[]))
        time.sleep(5)
    else:
        sense.clear()
