#Minecraft Controller with SenseHat functions
#import needed functions
from mcpi.minecraft import Minecraft
from mcpi import block
from sense_hat import SenseHat
import time, random, math

#instance the connection to Minecraft
mc=Minecraft.create()
#instance the SenseHAT
sense = SenseHat()
#reset the LED array
#sense.clear()


#functions to vertically move player based on joystick input
def moveup(event):
    mc.player.setPos(pos.x,pos.y+1,pos.z)
    mc.postToChat("TO INFINITY AND BEYOND!")
    #print(event)

def movedown(event):
    mc.player.setPos(pos.x,pos.y-1,pos.z)
    mc.postToChat("Dive!")
    #print(event)
    
while True:
    #find the position of the player to set your coordinate reference system
    pos = mc.player.getTilePos()    
    # poll the pitch and roll values to move the player
    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']
    #function to move Steve forward - using pitch axis
    #use player setting statuses?
    if 50 < pitch < 179:
        # move forward
        #sense.show_message('Moving Forward', text_colour=(100,0,150))
        print("Moving forward")
        mc.player.setPos(pos.x,pos.y,pos.z+1)
        #wait for a little while to let the player position update
        time.sleep(0.02)
    elif 300 > pitch > 179:
        #function to move Steve backward - using pitch axis
        # move backward
        #sense.show_message('Moving Backward', text_colour=(100,0,150))
        print("Moving backward")
        mc.player.setPos(pos.x,pos.y,pos.z-1)
        #wait for a little while to let the player position update
        time.sleep(0.02)
    #function to turn Steve - using roll axis
    if 50 < roll < 179:
        # turn left
        #sense.show_message('Moving Left', text_colour=(100,0,150))
        print("Moving Left")
        mc.player.setPos(pos.x-1,pos.y,pos.z)
        #wait for a little while to let the player position update
        time.sleep(0.02)
    elif 300 > roll > 179:
        #turn right
        #sense.show_message('Moving Right', text_colour=(100,0,150))
        print("Moving Right")
        mc.player.setPos(pos.x+1,pos.y,pos.z)
        #wait for a little while to let the player position update
        time.sleep(0.02)
    #function to jump/fly - using joystick button
    sense.stick.direction_up = moveup 
    sense.stick.direction_down = movedown
        

    # code to simulate firebreath - turn Steve into a dragon with the humidity sensor
    #get the humidity from the SenseHAT
    humidity = sense.get_humidity()
    #print("Humidity: %s %%rH" % humidity)
    time.sleep(0.1)
    #set the trigger for the humidity level - >70%
    #this will need to be tweaked according to the weather!
    if humidity >= 50:
        #turn Steve into a dragon
        mc.postToChat("HADOOOOUKEN!")
        for i in range(20):
            #spawn lava blocks in front of Steve, adding 1 to the z value on each loop
            mc.setBlock(pos.x, pos.y, pos.z+i, block.LAVA.id)
            #pause before placing the next block to give the breath time to spread
            time.sleep(0.05)
          

    #code to change the SenseHAT LED array to be a minimap
    block_underfoot = mc.getBlock(pos.x,pos.y-2,pos.z)
    #check the block colour and post to the SenseHAT LED array
    if block_underfoot == 2: #grass
        #make the LED green
        mc.postToChat(block_underfoot)
        sense.set_pixel(4,4,0,255,0)
        sense.set_pixel(4,3,0,255,0)
        sense.set_pixel(3,3,0,255,0)
        sense.set_pixel(3,4,0,255,0)
    elif block_underfoot == 10:
        #lavaaaaarrrrggghhhh! - red
        mc.postToChat(block_underfoot)
        sense.set_pixel(4,4,255,0,0)
        sense.set_pixel(3,3,255,0,0)
        sense.set_pixel(4,3,255,0,0)
        sense.set_pixel(3,4,255,0,0)
    elif block_underfoot == 8:
        #water - light blue
        mc.postToChat(block_underfoot)
        sense.set_pixel(4,4,100,100,255)
        sense.set_pixel(4,3,100,100,255)
        sense.set_pixel(3,3,100,100,255)
        sense.set_pixel(3,4,100,100,255)
    elif block_underfoot == 12:
        #sand - yellow
        mc.postToChat(block_underfoot)
        sense.set_pixel(4,4,0,105,100)
        sense.set_pixel(3,3,0,105,100)
        sense.set_pixel(4,3,0,105,100)
        sense.set_pixel(3,4,0,105,100)
    elif block_underfoot == 247:
        #reactor core - dark blue
        mc.postToChat(block_underfoot)
        sense.set_pixel(4,4,0,255,255)
        sense.set_pixel(3,3,0,255,255)
        sense.set_pixel(4,3,0,255,255)
        sense.set_pixel(3,4,0,255,255)
    elif block_underfoot == 79:
        #ice - white
        mc.postToChat(block_underfoot)
        sense.set_pixel(4,4,255,255,255)
        sense.set_pixel(3,3,255,255,255)
        sense.set_pixel(4,3,255,255,255)
        sense.set_pixel(3,4,255,255,255)
    elif block_underfoot == 78:
        #ice - blue white
        mc.postToChat(block_underfoot)
        sense.set_pixel(4,4,150,150,255)
        sense.set_pixel(3,4,150,150,255)
        sense.set_pixel(4,3,150,150,255)
        sense.set_pixel(3,3,150,150,255)
