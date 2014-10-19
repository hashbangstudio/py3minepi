#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Gets the type of block at the player's horizontal position
    Vertical position is the ground height at the horiz position
"""

from __future__ import print_function, division, absolute_import, unicode_literals

# We have to import the minecraft module to do anything in the minecraft world
try:
    from ..minecraft import Minecraft
    from ..block import AIR
except ImportError:
    try:
        from .mcpi.minecraft import Minecraft
        from .mcpi.block import AIR
    except ImportError:
        from mcpi.minecraft import Minecraft
        from mcpi.block import AIR


# this means that the file can be imported without
# executing anything in this code block
if __name__ == "__main__":

    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()

    # Get the current tile/block that the player is located at in the world
    player_position = mc.player.getTilePos()

    height = mc.getHeight(player_position.x, player_position.z)
    # create the output message as a string
    message = "Height is " + str(height)

    # print to the python interpreter standard output (terminal or IDLE)
    print(message)

    # send message to the minecraft chat
    mc.postToChat(message)

    # Get the type of block for the highest point in world
    # This is done at the horizonal player posn
    blockIdNum = mc.getBlock(player_position.x, height, player_position.z)

    if (blockIdNum == AIR.id):
        # Need to do height minus one for this as not flower etc
        blockIdNum = mc.getBlock(player_position.x,
                                 height - 1,
                                 player_position.z)

    # Add to message, the type of block stood on
    message = "Block is of type " + str(blockIdNum)

    # If BlockType is available can determine the name of the block tyoe
    # blockName = BlockType(blockIdNum).name
    # message += " which is " + blockName

    # print to the python interpreter standard output (terminal or IDLE)
    print(message)

    # send message to the minecraft chat
    mc.postToChat(message)
