#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Runs through the available blocks making a wall 10 columns wide
"""

from __future__ import print_function, division, absolute_import, unicode_literals

# needed to slow down the wall building for illustration of iteration
from time import sleep

# import the needed modules fo communication with minecraft world
try:
    from ..minecraft import Minecraft
    # from ..block import BlockType
except ImportError:
    try:
        from .mcpi.minecraft import Minecraft
        # from .mcpi.block import BlockType
    except ImportError:
        from mcpi.minecraft import Minecraft
        # from mcpi.block import BlockType


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
    columWrap = firstColumnX + 10

    # If BlockType is available can iterate over the enum
    # Create a wall of all types available
    # for blk in BlockType:
    #    if blockXposn == columWrap:
    #        # reset to the beginning of the row
    #        blockXposn = firstColumnX
    #        # increase the height of the current row to be built
    #        blockYposn += 1
    #
    #    # increase the distance along the row that the block is placed at
    #    blockXposn += 1
    #    print(
    #         ("Creating block {} with id = {:d} ".format(blk.name,
    #                                                     blk.value) +
    #          "at ({:d}, {:d}, {:d})".format(blockXposn,
    #                                         blockYposn,
    #                                         blockZposn)))
    #    # Create a block
    #    mc.setBlock(blockXposn, blockYposn, blockZposn, blk.value)
    #    sleep(0.5)

    for blk in range(0, 248):
        if blockXposn == columWrap:
            # reset to the beginning of the row
            blockXposn = firstColumnX
            # increase the height of the current row to be built
            blockYposn += 1

        # increase the distance along the row that the block is placed at
        blockXposn += 1
        print(
             ("Creating block with id = {:d} ".format(blk) +
              "at ({:d}, {:d}, {:d})".format(blockXposn,
                                             blockYposn,
                                             blockZposn)))
        # Create a block
        mc.setBlock(blockXposn, blockYposn, blockZposn, blk)
        sleep(0.5)
