# import all the necessary modules
from mcpi.minecraft import Minecraft
from mcpi import block
import time, math

# connect with the Minecraft world
mc=Minecraft.create()

# get the player's position
pos=mc.player.getTilePos()

#render a model of the starship Enterprise using TNT blocks
#we are building in sections:
#section A - the main habitation disk
diskHeight = 3
diskBottom = 26
diskTop = 31
diskRadius = 25
for i in range(int(math.floor(diskHeight))):
    yCoord = pos.y + math.floor(diskTop) + i
    print("Disk layer (Saucer): " + str(i))

    for j in range(int(math.floor(pos.x - diskRadius - 1)), int(math.ceil(pos.x + diskRadius + 1))):
        for k in range(int(math.floor(pos.z - diskRadius - 1)), int(math.ceil(pos.z + diskRadius + 1))):
            if ((j - pos.x) * (j - pos.x)) + ((k - pos.z) * (k - pos.z)) <= (diskRadius * diskRadius):
                mc.setBlock(j, yCoord, k, block.TNT.id,1)
#section B - the spine to the engineering section
mc.setBlocks(pos.x-2, pos.y+18, pos.z-25, pos.x+1, pos.y+30, pos.z-15, block.TNT.id,1)
#section C - the engineering hull
diskHeight = 53
diskBottom = -12
diskTop = -65
diskRadius = 10
for i in range(int(math.floor(diskHeight))):
    zCoord = pos.z + math.floor(diskTop) + i
    print(zCoord)
    print("Disk layer (Engineering): " + str(i))

    for j in range(int(math.floor(pos.y - diskRadius - 1)), int(math.ceil(pos.y + diskRadius + 1))):
        for k in range(int(math.floor(pos.x - diskRadius - 1)), int(math.ceil(pos.x + diskRadius + 1))):
            if ((j - pos.y) * (j - pos.y)) + ((k - pos.x) * (k - pos.x)) <= (diskRadius * diskRadius):
                mc.setBlock(k, j+8, zCoord, block.TNT.id,1)
                
#section D - a dome cut with a negative space to form the shuttlebay at the tail of the hull
domeRadius = 9    
for i in range(pos.x - (domeRadius), pos.x + (domeRadius), 1):
    for j in range(pos.y - (domeRadius), pos.y + (domeRadius), 1):
        for k in range(pos.z - (domeRadius), pos.z + (domeRadius), 1):
            if math.pow(i - pos.x, 2) + math.pow(j - pos.y, 2) + math.pow(k - pos.z, 2) <= math.pow(diskRadius - 1, 2):
                mc.setBlock(i, j+8, k-64, block.TNT.id, 1)
#section E - the warp drive nacelles
diskHeight = 60
diskBottom = -35
diskTop = -95
diskRadius = 4
domeRadius = 5
for i in range(int(math.floor(diskHeight))):
    zCoord = pos.z + math.floor(diskTop) + i
    print(zCoord)
    print("Disk layer (Left Nacelle): " + str(i))

    for j in range(int(math.floor(pos.y - diskRadius - 1)), int(math.ceil(pos.y + diskRadius + 1))):
        for k in range(int(math.floor(pos.x - diskRadius - 1)), int(math.ceil(pos.x + diskRadius + 1))):
            if ((j - pos.y) * (j - pos.y)) + ((k - pos.x) * (k - pos.x)) <= (diskRadius * diskRadius):
                mc.setBlock(k-17, j+35, zCoord, block.TNT.id,1)
#now add the hemisphere at the front of the nacelle
for i in range(pos.x - (domeRadius), pos.x + (domeRadius), 1):
    for j in range(pos.y - (domeRadius), pos.y + (domeRadius), 1):
        for k in range(pos.z - (domeRadius), pos.z + (domeRadius), 1):
            if math.pow(i - pos.x, 2) + math.pow(j - pos.y, 2) + math.pow(k - pos.z, 2) <= math.pow(diskRadius - 1, 2):
                mc.setBlock(i-17, j+35, k-35, block.TNT.id, 1)
diskHeight = 60
diskBottom = -35
diskTop = -95
diskRadius = 4
domeRadius = 5
for i in range(int(math.floor(diskHeight))):
    zCoord = pos.z + math.floor(diskTop) + i
    print(zCoord)
    print("Disk layer (Right Nacelle): " + str(i))

    for j in range(int(math.floor(pos.y - diskRadius - 1)), int(math.ceil(pos.y + diskRadius + 1))):
        for k in range(int(math.floor(pos.x - diskRadius - 1)), int(math.ceil(pos.x + diskRadius + 1))):
            if ((j - pos.y) * (j - pos.y)) + ((k - pos.x) * (k - pos.x)) <= (diskRadius * diskRadius):
                mc.setBlock(k+17, j+35, zCoord, block.TNT.id,1)
#now add the hemisphere at the front of the nacelle
for i in range(pos.x - (domeRadius), pos.x + (domeRadius), 1):
    for j in range(pos.y - (domeRadius), pos.y + (domeRadius), 1):
        for k in range(pos.z - (domeRadius), pos.z + (domeRadius), 1):
            if math.pow(i - pos.x, 2) + math.pow(j - pos.y, 2) + math.pow(k - pos.z, 2) <= math.pow(diskRadius - 1, 2):
                mc.setBlock(i+17, j+35, k-35, block.TNT.id, 1)

#and finally take out the half-cylinder at the rear of the nacelle for the warp drive emitter
#using an air block cylinder to intersect the nacelles at a right angle, to take out a tasty TNT bite!
diskHeight = 60
diskBottom = -30
diskTop = 30 #this is on the x axis
diskRadius = 4
#for i in range(int(math.floor(diskHeight))):
 #   xCoord = pos.x + math.floor(diskTop) + i
  #  print(xCoord)
   # print("Disk layer (Right Nacelle): " + str(i))

    #for j in range(int(math.floor(pos.y - diskRadius - 1)), int(math.ceil(pos.y + diskRadius + 1))):
     #   for k in range(int(math.floor(pos.x - diskRadius - 1)), int(math.ceil(pos.x + diskRadius + 1))):
      #      if ((j - pos.y) * (j - pos.y)) + ((k - pos.y) * (k - pos.y)) <= (diskRadius * diskRadius):
       #         mc.setBlock(xCoord, j+35, z-95, block.AIR.id)
#section F - the two warp drive pylons
xPylon = 2
yPylon = 4
zPylon = 6
loopCount = 7
xTop = pos.x-15
yTop = pos.y+32
zTop = pos.z-42
#render the starboard pylon
for i in range(0,loopCount):
    #define the limits of the block to place
    xBottom = xTop - xPylon
    yBottom = yTop - yPylon
    zBottom = zTop - zPylon
    #place the next pylon section
    mc.setBlocks(xBottom, yBottom, zBottom, xTop, yTop, zTop, block.TNT.id,1)
    #increment the top coordinate for the next section
    xTop = xTop +1
    yTop = yTop -3

#render the port pylon
xTop = pos.x+15
yTop = pos.y+32
zTop = pos.z-42
for i in range(0,loopCount):
    #define the limits of the block to place
    xBottom = xTop - xPylon
    yBottom = yTop - yPylon
    zBottom = zTop - zPylon
    #place the next pylon section
    mc.setBlocks(xBottom, yBottom, zBottom, xTop, yTop, zTop, block.TNT.id,1)
    #increment the top coordinate for the next section
    xTop = xTop -1
    yTop = yTop -3


#section G - the connector to the sensor dish
diskHeight = 2
diskBottom = -14
diskTop = -12
diskRadius = 2
for i in range(int(math.floor(diskHeight))):
    zCoord = pos.z + math.floor(diskTop) + i
    print(zCoord)
    print("Disk layer (dish strut): " + str(i))

    for j in range(int(math.floor(pos.y - diskRadius - 1)), int(math.ceil(pos.y + diskRadius + 1))):
        for k in range(int(math.floor(pos.x - diskRadius - 1)), int(math.ceil(pos.x + diskRadius + 1))):
            if ((j - pos.y) * (j - pos.y)) + ((k - pos.x) * (k - pos.x)) <= (diskRadius * diskRadius):
                mc.setBlock(k, j+8, zCoord, block.TNT.id,1)
#section H - the sensor dish
diskHeight = 2
diskBottom = -12
diskTop = -10
diskRadius = 8
for i in range(int(math.floor(diskHeight))):
    zCoord = pos.z + math.floor(diskTop) + i
    print(zCoord)
    print("Disk layer (sensor dish): " + str(i))

    for j in range(int(math.floor(pos.y - diskRadius - 1)), int(math.ceil(pos.y + diskRadius + 1))):
        for k in range(int(math.floor(pos.x - diskRadius - 1)), int(math.ceil(pos.x + diskRadius + 1))):
            if ((j - pos.y) * (j - pos.y)) + ((k - pos.x) * (k - pos.x)) <= (diskRadius * diskRadius):
                mc.setBlock(k, j+8, zCoord, block.TNT.id,1)

#section I - the dish antenna

diskHeight = 6
diskBottom = -12
diskTop = -7
diskRadius = 2
for i in range(int(math.floor(diskHeight))):
    zCoord = pos.z + math.floor(diskTop) + i
    print(zCoord)
    print("Disk layer (sensor antenna): " + str(i))

    for j in range(int(math.floor(pos.y - diskRadius - 1)), int(math.ceil(pos.y + diskRadius + 1))):
        for k in range(int(math.floor(pos.x - diskRadius - 1)), int(math.ceil(pos.x + diskRadius + 1))):
            if ((j - pos.y) * (j - pos.y)) + ((k - pos.x) * (k - pos.x)) <= (diskRadius * diskRadius):
                mc.setBlock(k, j+8, zCoord-1, block.TNT.id,1)
#section J - the phaser banks
diskHeight = 1
diskBottom = 28
diskTop = 30
diskRadius = 6
for i in range(int(math.floor(diskHeight))):
    yCoord = pos.y + math.floor(diskTop) + i
    print("Disk layer: " + str(i))

    for j in range(int(math.floor(pos.x - diskRadius - 1)), int(math.ceil(pos.x + diskRadius + 1))):
        for k in range(int(math.floor(pos.z - diskRadius - 1)), int(math.ceil(pos.z + diskRadius + 1))):
            if ((j - pos.x) * (j - pos.x)) + ((k - pos.z) * (k - pos.z)) <= (diskRadius * diskRadius):
                mc.setBlock(j, yCoord, k, block.TNT.id,1)
                
#section K - the bridge part I
diskHeight = 1
diskBottom = 32
diskTop = 34
diskRadius = 8
for i in range(int(math.floor(diskHeight))):
    yCoord = pos.y + math.floor(diskTop) + i
    print("Disk layer: " + str(i))

    for j in range(int(math.floor(pos.x - diskRadius - 1)), int(math.ceil(pos.x + diskRadius + 1))):
        for k in range(int(math.floor(pos.z - diskRadius - 1)), int(math.ceil(pos.z + diskRadius + 1))):
            if ((j - pos.x) * (j - pos.x)) + ((k - pos.z) * (k - pos.z)) <= (diskRadius * diskRadius):
                mc.setBlock(j, yCoord, k, block.TNT.id,1)
#section L - the bridge part II
diskHeight = 1
diskBottom = 34
diskTop = 35
diskRadius = 5
for i in range(int(math.floor(diskHeight))):
    yCoord = pos.y + math.floor(diskTop) + i
    print("Disk layer: " + str(i))

    for j in range(int(math.floor(pos.x - diskRadius - 1)), int(math.ceil(pos.x + diskRadius + 1))):
        for k in range(int(math.floor(pos.z - diskRadius - 1)), int(math.ceil(pos.z + diskRadius + 1))):
            if ((j - pos.x) * (j - pos.x)) + ((k - pos.z) * (k - pos.z)) <= (diskRadius * diskRadius):
                mc.setBlock(j, yCoord, k, block.TNT.id,1)
#section M - the bridge part III
diskHeight = 1
diskBottom = 35
diskTop = 36
diskRadius = 2
for i in range(int(math.floor(diskHeight))):
    yCoord = pos.y + math.floor(diskTop) + i
    print("Disk layer: " + str(i))

    for j in range(int(math.floor(pos.x - diskRadius - 1)), int(math.ceil(pos.x + diskRadius + 1))):
        for k in range(int(math.floor(pos.z - diskRadius - 1)), int(math.ceil(pos.z + diskRadius + 1))):
            if ((j - pos.x) * (j - pos.x)) + ((k - pos.z) * (k - pos.z)) <= (diskRadius * diskRadius):
                mc.setBlock(j, yCoord, k, block.TNT.id,1)


