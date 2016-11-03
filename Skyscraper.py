#import all the necessary modules
from mcpi.minecraft import Minecraft
from mcpi import block
import time, random

#connect with the Minecraft world
mc=Minecraft.create()

#get the player's position
pos=mc.player.getTilePos()

#set the block choices for the floors we can use in our skyscraper
blocks = [block.GLOWING_OBSIDIAN.id,
          block.STONE_BRICK.id,
          block.SANDSTONE.id,
          block.GOLD_BLOCK.id,
          block.GRASS.id,
          block.DIRT.id,
          block.IRON_ORE.id,
          block.WOOL.id, random.randint(0,15),
          block.CLAY.id,
          block.TNT.id, 1, 
          block.SNOW_BLOCK.id,
          block.NETHER_REACTOR_CORE.id, random.randint(0,2),
          block.IRON_BLOCK.id,
          block.GRAVEL.id,
          block.LAPIS_LAZULI_BLOCK.id,
          block.SAND.id,
          block.SNOW.id,
          block.ICE.id,
          block.REDSTONE_ORE.id,
          block.DIAMOND_BLOCK.id,
          block.MOSS_STONE.id,
          block.LAVA.id]

#carve out a negative space to the bottom of the game world
mc.setBlocks(pos.x+10,64,pos.z+10,pos.x-10,
             -64,pos.z-10,block.AIR.id)

#set a layer of bedrock to build our skyscraper on
mc.setBlocks(pos.x+10,-64,pos.z+10,pos.x-10,-64,pos.z-10,block.BEDROCK.id)

#teleport the player to a safe place
mc.player.setTilePos(pos.x-10, pos.y, pos.z-10)

#warn the player this might take a little while
mc.postToChat("Stand by... preparing construction.")

#use a for loop to randomly generate floors and build up to the sky!
for i in range(-64, 100, 1):
    mc.setBlocks(pos.x+7,(i*2)-64,pos.z+7,pos.x-7,(i*2)-59,pos.z-7,random.choice(blocks))
    #add in a time delay so that we can see the tower being built
    time.sleep(0.2)

#let the player know that they can continue without risk of ending up inside the building!
mc.postToChat("Construction of Steve Tower complete.")
mc.postToChat(str(random.randint(0, 255)) + " days since last reported accident.")



