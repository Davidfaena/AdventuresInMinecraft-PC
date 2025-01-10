from MyAdventures.mcpi import block
import time

# Function that places some tnt

def main(mc):

    # Get player location
    pos = mc.player.getTilePos()

    # Coords to place the tnt nest to the player
    x, y, z = pos.x + 2, pos.y, pos.z

    mc.setBlock(x, y, z, block.TNT)
    mc.postToChat("¡TNT placed!")

    time.sleep(2)

    mc.setBlock(x, y+1, z, block.REDSTONE_BLOCK)
    mc.setBlock(x, y+1, z, block.AIR)

    mc.postToChat("¡TNT activated!")