#import all the necessary modules
from mcpi.minecraft import Minecraft
from mcpi import block
import time, random, math

#connect with the Minecraft world
mc=Minecraft.create()

#get the player's position
pos=mc.player.getTilePos()

e = 1.6 * math.pow(10, -19)
radius = 25
fieldType = block.GLASS.id ## Block that will fill in the field

def absolute(value): ## Returns the absolute value of the parameter
    if value < 0:
        return value * -1
    else:
        return value

def getPotentialHeight(Q, r): ## Returns the height of the tower at the radius passed to it
    try:
        E = (1 / (4 * math.pi * (8.85 * math.pow(10, -12))) * (Q / r))
    except ZeroDivisionError: ## If the radius is zero
        E = math.pow(10, -10)
    
    return int(round(E * math.pow(10, 8.75)))

def mapPotentialWellGold(rad): ## Maps the potential well of a gold nucleus
    for x in range(int(round(pos.x - rad)), int(round(pos.x + rad + 1))):
        for z in range(int(round(pos.z - rad)), int(round(pos.z + rad + 1))):
            for y in range(int(round(pos.y)), int(round(pos.y + getPotentialHeight(e * 79, absolute(math.sqrt(math.pow(pos.x - x, 2) + math.pow(pos.z - z, 2))))))):
                mc.setBlock(x, y, z, fieldType)

    mc.setBlock(pos.x, pos.y, pos.z, block.GOLD_BLOCK.id)

def mapPotentialWellCoal(rad): ## Maps the potential well of a carbon nucleus
    pos2 = pos;
    pos2.x = pos2.x + 15
    pos2.z = pos2.z + 15
    
    for x in range(int(round(pos2.x - rad)), int(round(pos2.x + rad + 1))):
        for z in range(int(round(pos2.z - rad)), int(round(pos2.z + rad + 1))):
            for y in range(int(round(pos2.y)), int(round(pos2.y + getPotentialHeight(e * 79, absolute(math.sqrt(math.pow(pos.x - x - 15, 2) + math.pow(pos.z - z - 15, 2)))) + getPotentialHeight(e * 12, absolute(math.sqrt(math.pow(pos2.x - x, 2) + math.pow(pos2.z - z, 2))))))):
                mc.setBlock(x, y, z, fieldType)

    mc.setBlock(pos2.x, pos2.y, pos2.z, block.OBSIDIAN.id)

mapPotentialWellGold(radius)
mapPotentialWellCoal(radius)
