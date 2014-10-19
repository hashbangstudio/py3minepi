#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Create a wall using the setBlocks()
"""

from __future__ import print_function, division, absolute_import, unicode_literals

# import the needed modules
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

    wallStartXposn = player_position.x + 6
    wallStartYposn = player_position.y + 1
    wallZposn = player_position.z + 6

    wallEndXposn = wallStartXposn + 10
    wallEndYposn = wallStartYposn + 6

    # Create a wall
    mc.setBlocks(wallStartXposn, wallStartYposn, wallZposn,
                 wallEndXposn, wallEndYposn, wallZposn,
                 DIAMOND_BLOCK)
