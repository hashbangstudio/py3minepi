#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Gets the type of block at the player's horizontal position
    Vertical position is the ground height at the horiz position
    Gets the data/variant of the block and if is wool prints the colour
"""

from __future__ import print_function, division, absolute_import, unicode_literals

try:
    from ..minecraft import Minecraft
    from ..block import WOOL, AIR
    # from ..block import BlockType
    # from ..blockData import Color
except ImportError:
    try:
        from .mcpi.minecraft import Minecraft
        from .mcpi.block import WOOL, AIR
        # from .mcpi.block import BlockType
        # from .mcpi.blockData import Color
    except ImportError:
        from mcpi.minecraft import Minecraft
        from mcpi.block import WOOL, AIR
        # from mcpi.block import BlockType
        # from mcpi.blockData import Color

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
    # print to the python interpreter standard output (terminal or IDLE )
    print(message)
    # post message to the chat
    mc.postToChat(message)

    # Get the type of block for the highest point in world at horiz player posn
    blockAndData = mc.getBlockWithData(player_position.x,
                                       height,
                                       player_position.z)

    if blockAndData.id == AIR.id:
        # Need to do height minus one for this
        blockAndData = mc.getBlockWithData(player_position.x,
                                           height - 1,
                                           player_position.z)

    # Add to message, the type of block stood on
    message = "Block is of type " + str(blockAndData.id)

    # If BlockType is available can determine the name of the block tyoe
    # blockName = BlockType(blockAndData.id).name
    # message += " which is " + blockName

    # print to the python interpreter standard output (terminal or IDLE )
    print(message)
    # post message to the chat
    mc.postToChat(message)

    dataMessage = "Block data is " + str(blockAndData.data)
    print(dataMessage)
    mc.postToChat(dataMessage)

    if blockAndData.id == WOOL.id:
        print("Is wool")
        # If colour enum is avaiable, can determine the colour name
        # colourMsg = "Colour is " + Color(blockAndData.data).name
        colourMsg = "Colour is " + str(blockAndData.data)
        print(colourMsg)
        mc.postToChat(colourMsg)
