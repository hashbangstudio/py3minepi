#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Gets the type of block at the command line given coordinates
    If two coords given uses world height for y coordinate
    if three coords given uses those
    Gets the data/variant of the block and if is wool prints the colour
"""

from __future__ import print_function, division, absolute_import, unicode_literals

import sys

# We have to import the minecraft  module to do anything in the minecraft world
try:
    from ..minecraft import Minecraft
    from ..block import WOOL
    # from ..block import BlockType
    # from ..blockData import Color
except ImportError:
    try:
        from .mcpi.minecraft import Minecraft
        from .mcpi.block import WOOL
        # from .mcpi.block import BlockType
        # from .mcpi.blockData import Color
    except ImportError:
        from mcpi.minecraft import Minecraft
        from mcpi.block import WOOL
        # from mcpi.block import BlockType
        # from mcpi.blockData import Color


# this means that the file can be imported without
# executing anything in this code block
if __name__ == "__main__":

    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()

    num_of_args = len(sys.argv) - 1
    if num_of_args == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
    elif num_of_args == 2:
        x = int(sys.argv[1])
        z = int(sys.argv[2])
        # Get the block that would be stood on at this Horiz posn
        y = mc.getHeight(x, z) - 1
    else:
        print("Number of arguments incorrect")
        print(("Expected 2 or 3 arguments but got {:d}".format(num_of_args)))
        print("Usage with 3 args: python script.py xcoord ycoord zcoord")
        print("Usage with 2 args: python script.py xcoord zcoord")
        sys.exit()

    blockAndData = mc.getBlockWithData(x, y, z)

    # Add to message, the type of block stood on
    message = "Block is of type " + str(blockAndData.id)

    # If BlockType is available can determine the name of the block tyoe
    # blockName = BlockType(blockAndData.id).name
    # message += " which is " + blockName

    # print to the python interpreter standard output (terminal or IDLE )
    print(message)
    # post message to the chat
    mc.postToChat(message)

    message = "Block data " + str(blockAndData.data)
    # print to the python interpreter standard output (terminal or IDLE )
    print(message)
    # post message to the chat
    mc.postToChat(message)

    if blockAndData.id == WOOL.id:
        print("Is wool")
        # If colour enum is avaiable, can determine the colour name
        # colourMsg = "Colour is " + Color(blockAndData.data).name
        colourMsg = "Colour is " + str(blockAndData.data)
        print(colourMsg)
        mc.postToChat(colourMsg)
