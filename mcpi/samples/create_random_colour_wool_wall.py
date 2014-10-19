#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Creates a wall of wool using a random colour for each block
"""

from __future__ import print_function, division, absolute_import, unicode_literals

# needed to slow down the wall building
from time import sleep
# needed to generate a random number for the colour of wool
from random import randint

# import the needed modules fo communication with minecraft world
try:
    from ..minecraft import Minecraft
    # import needed block definitions
    from ..block import WOOL
    # from ..blockData import Color
except ImportError:
    try:
        from .mcpi.minecraft import Minecraft
        from .mcpi.block import WOOL
    except ImportError:
        from mcpi.minecraft import Minecraft
        from mcpi.block import WOOL


# create a function to create a random block of wool
def getWoolBlockWithRandomColour():
    """
        Generate a random number within the allowed range of colours
        colour range is (0 to 15 inclusive)
    """
    randomNumber = randint(0, 15)
    print(("random num to be used = " + str(randomNumber)))
    # print((" Colour = " + Color(randomNumber).name))
    generatedBlock = WOOL.withData(randomNumber)
    return generatedBlock


if __name__ == "__main__":

    # Create a connection to the Minecraft game
    mc = Minecraft.create()

    # Get the player position
    player_position = mc.player.getTilePos()

    # define the position of the bottom left block of the wall
    blockXposn = int(player_position.x + 6)
    firstColumnX = blockXposn
    blockYposn = int(player_position.y + 1)
    blockZposn = int(player_position.z + 6)

    # Create a wall using nested for loops
    for row in range(6):
        # increase the height of th current row to be built
        blockYposn += 1
        blockXposn = firstColumnX
        for column in range(10):
            # increase the distance along the row that the block is placed at
            blockXposn += 1
            print(("Creating block at ({:d}, {:d}, {:d})".format(blockXposn,
                                                                 blockYposn,
                                                                 blockZposn)))
            my_block = getWoolBlockWithRandomColour()
            # Create a block
            mc.setBlock(blockXposn, blockYposn, blockZposn,
                        my_block.id, my_block.data)
            sleep(0.5)
