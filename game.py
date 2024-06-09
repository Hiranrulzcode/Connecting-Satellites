import random
import pgzrun
from time import time


WIDTH=800
HEIGHT=600


satellites=[]
lines=[]

next_satellite=0

start_time=0
total_time=0
end_time=0

number_of_satellite=8

def create_satellites():
    global start_time
    
    for count in range(0,number_of_satellite):
        satellite=Actor("satellite")
        satellite.pos=random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40)
        satellites.append(satellite)
    start_time=time()


def draw():
    global total_time
    screen.blit("bg",(0,0))
    number=1

    for satellite in satellites:
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+20))
        satellite.draw()
        number=number+1

create_satellites()









































pgzrun.go()