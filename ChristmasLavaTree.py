# import all the necessary modules
from mcpi.minecraft import Minecraft
from mcpi import block
import time, math, random

# connect with the Minecraft world
mc=Minecraft.create()

# get the player's position
pos=mc.player.getTilePos()

#set the maximum height of the tree
treeHeight = 30
#use the tree height to get a well-proportioned stump/tree trunk
stumpRad = math.floor(treeHeight / 6)

#teleport the player out of harm's way so they don't get swallowed by the tree during construction
mc.player.setPos(pos.x + treeHeight, pos.y + 10, pos.z)

#print("Player x y z: " + str(pos.x) + " " + str(pos.y) + " " + str(pos.z))

#build the tree in layers from the ground up 
for i in range(treeHeight):
    yCoord = pos.y + i
    radius = math.ceil((treeHeight - i) * 0.5)
    #print("Layer: " + str(i))
    #print("Minimum X: " + str(math.floor(pos.x - radius - 1)))
    #print("Maximum X: " + str(math.ceil(pos.x + radius + 1)))
    #print("Minimum Z: " + str(math.floor(pos.z - radius - 1)))
    #print("Maximum Z: " + str(math.ceil(pos.z + radius + 1)))
    #print("----------------")
    
    for j in range(int(math.floor(pos.x - radius - 1)), int(math.ceil(pos.x + radius + 1))):
        for k in range(int(math.floor(pos.z - radius - 1)), int(math.ceil(pos.z + radius + 1))):
            if ((j - pos.x) * (j - pos.x)) + ((k - pos.z) * (k - pos.z)) <= (radius * radius):
                if math.floor(random.randint(0, 10)) == 0:
                    #add decorative blocks
                    mc.setBlock(j, yCoord, k, block.NETHER_REACTOR_CORE.id)
                elif math.floor(random.randint(0,10)) == 1:
                    #add decorative blocks
                    mc.setBlock(j, yCoord, k, block.LAVA.id)
                elif math.floor(random.randint(0,10)) == 2:
                    #add decorative blocks
                    mc.setBlock(j, yCoord, k, block.TNT.id, 1)
                else:
                    #use green wool to simulate the tree
                    mc.setBlock(j, yCoord, k, block.WOOL.id, 13)
            #print(str(j) + " " + str(yCoord) + " " + str(k) + " Radius: " + str(radius))

#create the tree stump
for i in range(int(math.floor(treeHeight / 5))):
    yCoord = pos.y - math.floor(treeHeight / 5) + i
    #print("Stump layer: " + str(i))

    for j in range(int(math.floor(pos.x - stumpRad - 1)), int(math.ceil(pos.x + stumpRad + 1))):
        for k in range(int(math.floor(pos.z - stumpRad - 1)), int(math.ceil(pos.z + stumpRad + 1))):
            if ((j - pos.x) * (j - pos.x)) + ((k - pos.z) * (k - pos.z)) <= (stumpRad * stumpRad):
                mc.setBlock(j, yCoord, k, block.WOOD.id, 13)

#teleport the player above the finished tree to get a good view
#mc.player.setPos(pos.x, pos.y + treeHeight + 5, pos.z)
