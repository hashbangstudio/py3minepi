#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Places a Diamond block next to the player
"""

from __future__ import print_function, division, absolute_import, unicode_literals

# import the needed modules for communication with minecraft world
try:
    from ..minecraft import Minecraft
    from ..block import DIAMOND_BLOCK
except ImportError:
    try:
        from .mcpi.minecraft import Minecraft
        from .mcpi.block import DIAMOND_BLOCK
    except ImportError:
        from mcpi.minecraft import Minecraft
        from mcpi.block import DIAMOND_BLOCK

if __name__ == "__main__":

    # Create a connection to the Minecraft game
    mc = Minecraft.create()

    # Get the player position
    player_position = mc.player.getTilePos()

    # define the position of the block
    blockXposn = int(player_position.x + 1)
    blockYposn = int(player_position.y + 1)
    blockZposn = int(player_position.z + 1)

    print(("Creating block at ({:d}, {:d}, {:d})".format(blockXposn,
                                                         blockYposn,
                                                         blockZposn)))

    # Create a block
    mc.setBlock(blockXposn, blockYposn, blockZposn,
                DIAMOND_BLOCK.id)
