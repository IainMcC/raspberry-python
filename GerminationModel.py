# import all the necessary modules
from mcpi.minecraft import Minecraft
from mcpi import block
from gpiozero import Button, LED
from time import sleep

#initialise physical components connected to GPIO
red = LED(17)
amber = LED(18)
green = LED(23)
blue = LED(24)
button1 = Button(5)
button2 = Button(6)
button3 = Button(12)
button4 = Button(13)

# connect with the Minecraft world
mc=Minecraft.create()

while True:
    #turn off the LEDs
    red.off()
    amber.off()
    green.off()
    blue.off()
    #poll for input from the buttons
    if button1.is_pressed:
        # get the player's position
        pos=mc.player.getTilePos()
        for i in range(0,1):
            blue.on()
            sleep(0.2)
            blue.off()
            print(i)
            sleep(0.2)
        print("Planted seed. Watered 1 litre.")
        #plant the seed - dig up the ground
        mc.setBlock(pos.x, pos.y-1, pos.z+1,block.DIRT.id)
        #water the seed
        for j in range(0,1):
            mc.setBlock(pos.x, pos.y+j, pos.z+1,block.WATER.id)
        mc.postToChat("Planted seed. Watered 1 litre.")
        sleep(3)
        print("Seed germinating!")
        mc.postToChat("Seed germinating!")
        sleep(2)
        #loop for plant growth
        for k in range (0,3):
            red.on()
            sleep(0.5)
            #grow the stalk (green wool)
            mc.setBlock(pos.x,pos.y+k,pos.z+1,block.WOOL.id, 13)
            red.off()
            sleep(0.5)
        print("Plant failed to grow leaves and ran out of food! Try more water next time!")
        mc.postToChat("Plant failed to grow leaves and ran out of food!")
        mc.postToChat("Try more water next time!")
    elif button2.is_pressed:
        # get the player's position
        pos=mc.player.getTilePos()
        for i in range(0,2):
            blue.on()
            sleep(0.2)
            blue.off()
            print(i)
            sleep(0.2)
        print("Planted seed. Watered 2 litres.")
        #plant the seed - dig up the ground
        mc.setBlock(pos.x, pos.y-1, pos.z+1,block.DIRT.id)
        #water the seed
        for j in range(0,2):
            mc.setBlock(pos.x, pos.y+j, pos.z+1,block.WATER.id)
        mc.postToChat("Planted seed. Watered 2 litres.")
        sleep(3)
        print("Seed germinating!")
        mc.postToChat("Seed germinating!")
        sleep(2)
        #loop for plant growth
        for k in range (0,5):
            amber.on()
            sleep(0.5)
            #grow the stalk (green wool)
            mc.setBlock(pos.x,pos.y+k,pos.z+1,block.WOOL.id, 13)
            amber.off()
            sleep(0.5)
        #add leaves to the stalk
        mc.setBlock(pos.x+1, pos.y+2, pos.z+1, block.LEAVES.id)
        mc.setBlock(pos.x, pos.y+3, pos.z+2, block.LEAVES.id)
        mc.setBlock(pos.x, pos.y+3, pos.z, block.LEAVES.id)
        mc.setBlock(pos.x, pos.y+3, pos.z-1, block.LEAVES.id)
        mc.setBlock(pos.x-1, pos.y+4, pos.z, block.LEAVES.id)
        print("Plant growing, but not well enough to flower. Try a bit more water next time!")
        mc.postToChat("Plant growing, but not well enough to flower.")
        mc.postToChat("Try a bit more water next time!")
    elif button3.is_pressed:
        # get the player's position
        pos=mc.player.getTilePos()
        for i in range(0,3):
            blue.on()
            sleep(0.2)
            blue.off()
            print(i)
            sleep(0.2)
        print("Planted seed. Watered 3 litres.")
        #plant the seed - dig up the ground
        mc.setBlock(pos.x, pos.y-1, pos.z+1,block.DIRT.id)
        #water the seed
        for j in range(0,3):
            mc.setBlock(pos.x, pos.y+j, pos.z+1,block.WATER.id)
        mc.postToChat("Planted seed. Watered 3 litres.")
        sleep(3)
        print("Seed germinating!")
        mc.postToChat("Seed germinating!")
        sleep(2)
        for k in range (0,10):
            green.on()
            sleep(0.5)
            #grow the stalk (green wool)
            mc.setBlock(pos.x,pos.y+k,pos.z+1,block.WOOL.id, 13)
            green.off()
            sleep(0.5)
        #add leaves to the stalk
        mc.setBlock(pos.x+1, pos.y+2, pos.z+1, block.LEAVES.id)
        mc.setBlock(pos.x, pos.y+3, pos.z+2, block.LEAVES.id)
        mc.setBlock(pos.x, pos.y+4, pos.z, block.LEAVES.id)
        mc.setBlock(pos.x, pos.y+5, pos.z-1, block.LEAVES.id)
        mc.setBlock(pos.x-1, pos.y+4, pos.z, block.LEAVES.id)
        mc.setBlock(pos.x, pos.y+8, pos.z+2, block.LEAVES.id)
        mc.setBlock(pos.x+1, pos.y+7, pos.z, block.LEAVES.id)
        #add the TNT flower  
        for m in range(-1,2,1):
            for n in range (-2,2,1):
                for o in range (-1, 2, 1):
                    mc.setBlock(pos.x+m, (pos.y+n)+12, (pos.z+o)+1, block.TNT.id, 1)
        print("Congratulations! You grew a perfect TNT flower plant!")
        mc.postToChat("Congratulations! You grew a perfect TNT flower plant!")
    elif button4.is_pressed:
        # get the player's position
        pos=mc.player.getTilePos()
        for i in range(0,4):
            blue.on()
            sleep(0.2)
            blue.off()
            print(i)
            sleep(0.2)
        print("Planted seed. Watered 4 litres.")
        #plant the seed - dig up the ground
        mc.setBlock(pos.x, pos.y-1, pos.z+1,block.DIRT.id)
        #water the seed
        for j in range(0,4):
            mc.setBlock(pos.x, pos.y+j, pos.z+1,block.WATER.id)
        mc.postToChat("Planted seed. Watered 4 litres.")
        sleep(3)
        print("Seed germinating!")
        mc.postToChat("Seed germinating!")
        sleep(2)
        for k in range (0,1):
            red.on()
            sleep(0.5)
            #grow the stalk (green wool)
            mc.setBlock(pos.x, pos.y+k, pos.z+1, block.WOOL.id, 13)
            red.off()
            sleep(0.5)
        print("Plant too waterlogged to grow! Try less water next time!")
        mc.postToChat("Plant too waterlogged to grow!")
        mc.postToChat("Try less water next time!")
