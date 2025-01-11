from MyAdventures.mcpi.minecraftstuff import MinecraftTurtle

def main(mc):

    # Create a turtle instance
    tortuga = MinecraftTurtle(mc, mc.player.getTilePos())

    # Draws a square
    for _ in range(4):
        tortuga.speed(10)
        tortuga.forward(10)
        tortuga.right(90)
