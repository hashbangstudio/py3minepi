#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Gets the height of the world at the player's horizontal position
    OR gets the height of the world at the command line given coordinates (x,z)
    To get the height of the world at the player
    Usage: python script.py
    To get the height of the world at a specific coordinate
    Usage: python script.py x z
"""

from __future__ import print_function, division, absolute_import, unicode_literals
# this must be imported to get command line arguments
import sys

# We have to import the minecraft  module to do anything in the minecraft world
try:
    from ..minecraft import Minecraft
except ImportError:
    try:
        from .mcpi.minecraft import Minecraft
    except ImportError:
        from mcpi.minecraft import Minecraft

# this means that the file can be imported without
# executing anything in this code block
if __name__ == "__main__":

    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()

    # Get the current tile/block that the player is located at in the world
    player_position = mc.player.getTilePos()

    x = player_position.x
    z = player_position.z

    # sys.argv is a list of the command arguments given and the script name
    num_of_args = len(sys.argv) - 1

    # Check that have the appropriate number of command line arguments
    # Two or zero in this case
    if num_of_args == 2:
        x = int(sys.argv[1])
        z = int(sys.argv[2])
    elif num_of_args == 0:
        # just use the player position for x and z
        pass
    else:
        print(("Expected 2 or 0 arguments but recieved " + str(num_of_args)))
        print("To get the height of the world at the player")
        print("Usage: python script.py")
        print("To get the height of the world at a specific coordinate")
        print("Usage: python script.py x z")
        sys.exit()

    # get the height of the world at the coordinates (x,z)
    height = mc.getHeight(x, z)

    # create the output message as a string
    message = "Height of world is " + str(height) + " at " + str((x, z))

    # print to the python interpreter standard output (terminal or IDLE)
    print(message)

    # send message to the minecraft chat
    mc.postToChat(message)
