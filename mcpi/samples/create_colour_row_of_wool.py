#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Creates a row of wool blocks showing all the colours
"""

from __future__ import print_function, division, absolute_import, unicode_literals

# import the needed modules
try:
    from ..minecraft import Minecraft
    from ..block import WOOL
    # from ..blockdata import Color
except ImportError:
    try:
        from .mcpi.minecraft import Minecraft
        from .mcpi.block import WOOL
        # from .mcpi.blockdata import Color
    except ImportError:
        from mcpi.minecraft import Minecraft
        from mcpi.block import WOOL
        # from mcpi.blockdata import Color

if __name__ == "__main__":

    # Create a connection to the Minecraft game
    mc = Minecraft.create()

    # Get the player position
    player_position = mc.player.getTilePos()

    # Set coordinates (position) for the block that is
    # slightly away from the player
    # Note y is the vertical coordinate, x and z the horizontal
    blockYposn = int(player_position.y + 1)
    blockZposn = int(player_position.z + 1)

    # If Color Enum is available then can iterate through colours with names
    # for col in Color:
    #    # increase the distance along and up that the block is placed at
    #    blockXposn = player_position.x + 1 + col.value
    #    print(
    #        ("Creating block of color {} from data {:d}".format(col.name,
    #                                                            col.value) +
    #         " at ({:d}, {:d}, {:d})".format(blockXposn,
    #                                         blockYposn,
    #                                         blockZposn)))
    #    # Create a block
    #    mc.setBlock(blockXposn, blockYposn, blockZposn,
    #                WOOL.id, col.value)

    for col in range(0, 16):
        # increase the distance along and up that the block is placed at
        blockXposn = int(player_position.x + 1 + col)
        print(
            ("Creating block of color {:d}".format(col) +
             " at ({:d}, {:d}, {:d})".format(blockXposn,
                                             blockYposn,
                                             blockZposn)))
        # Create a block
        mc.setBlock(blockXposn, blockYposn, blockZposn,
                    WOOL.id, col)
