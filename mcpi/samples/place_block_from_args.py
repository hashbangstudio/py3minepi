#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Places a block next to player horizontally at world height vertically
    With given type and data from command line
    Usage : python script.py blockId,blockData
    OR
    Places a block with given type and data from command line
    At given coordinates from the command line
    Usage : python script.py blockId,blockData x,y,z
"""

from __future__ import print_function, division, absolute_import, unicode_literals

import sys

try:
    from ..minecraft import Minecraft
    from ..block import Block, AIR
except ImportError:
    try:
        from .mcpi.minecraft import Minecraft
        from .mcpi.block import Block, AIR
    except ImportError:
        from mcpi.minecraft import Minecraft
        from mcpi.block import Block, AIR


if __name__ == "__main__":

    # Create a connection to the Minecraft game
    mc = Minecraft.create()

    # Get the player position
    player_position = mc.player.getTilePos()

    # Set coordinates (position) for the block that is
    # slightly away from the player
    # Note y is the vertical coordinate, x and z the horizontal
    blockXposn = player_position.x + 1
    blockZposn = player_position.z + 1
    # set the y coordinate to be at the height of the world
    # at the (x,z) horisontal coordinate
    blockYposn = mc.getHeight(blockXposn, blockZposn)
    blockToPlace = AIR
    num_of_args = len(sys.argv) - 1
    if (num_of_args == 1 or num_of_args == 2):
        blockArgs = sys.argv[1].replace('(', '').replace(')', '').split(',')
        blockId = int(blockArgs[0])
        blockData = int(blockArgs[1])

        blockToPlace = Block(blockId, blockData)
        if num_of_args == 2:
            coords = sys.argv[2].replace('(', '').replace(')', '').split(',')
            print(("using coords = " + str(coords)))
            blockXposn = int(float(coords[0]))
            blockYposn = int(float(coords[1]))
            blockZposn = int(float(coords[2]))
    else:
        print("To place block next to player:")
        print("Usage : python script.py blockId,blockData")
        print("To place block at a specific coordinate")
        print("Usage : python script.py blockId,blockData x,y,z")
        print(("Expected 1 or 2 arguments but received " + str(num_of_args)))
        sys.exit()

    print(str(blockToPlace))
    print(str((blockXposn, blockYposn, blockZposn)))

    mc.setBlock(blockXposn, blockYposn, blockZposn,
                blockToPlace.id, blockToPlace.data)
