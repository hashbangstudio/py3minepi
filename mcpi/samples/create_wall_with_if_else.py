#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Creates a wall of Diamond blocks one by one apart from one block
    A Primed TNT block is created at a specified location
    This is done using an if else conditional
"""

from __future__ import print_function, division, absolute_import, unicode_literals

# needed to slow down the wall building for illustration of iteration
from time import sleep

# import the needed modules for communication with minecraft world
try:
    from ..minecraft import Minecraft
    from ..block import DIAMOND_BLOCK, TNT
except ImportError:
    try:
        from .mcpi.minecraft import Minecraft
        from .mcpi.block import DIAMOND_BLOCK, TNT
    except ImportError:
        from mcpi.minecraft import Minecraft
        from mcpi.block import DIAMOND_BLOCK, TNT

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
            print(
                 ("Creating block at ({:d}, {:d}, {:d})".format(blockXposn,
                                                                blockYposn,
                                                                blockZposn)))
            # Create a block
            if (row == 2) and (column == 2):
                mc.setBlock(blockXposn, blockYposn, blockZposn,
                            TNT.withData(1))
            else:
                mc.setBlock(blockXposn, blockYposn, blockZposn,
                            DIAMOND_BLOCK)
            sleep(0.5)

    mc.postToChat("Now hit the TNT block and stand well back!")
