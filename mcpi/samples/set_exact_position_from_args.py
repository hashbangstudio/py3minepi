#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Sets the position of the player from command line arguments (x z)
    Player's height set from getHeight()
    For given horizontal position (x, z)
    y = height of the world at horizontal posn
    player position set to (x, y, z)
    Usage: python script.py x z
    Example usage: python script.py 9.2 8.5
"""

from __future__ import print_function, division, absolute_import, unicode_literals

import sys

# We have to import the minecraft  module to do anything in the minecraft world
try:
    from ..minecraft import Minecraft
except ImportError:
    try:
        from .mcpi.minecraft import Minecraft
    except ImportError:
        from mcpi.minecraft import Minecraft


# this means that the file can be imported
# without executing anything in this code block
if __name__ == "__main__":

    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()

    # Get the current position that the player is located at in the world
    player_position = mc.player.getPos()

    # create the output message as a string
    message = "You are at ({0:.1f}, {1:.1f}, {2:.1f})".format(
              player_position.x, player_position.y, player_position.z)

    # print to the python interpreter standard output (terminal or IDLE)
    print(message)

    # send message to the minecraft chat
    mc.postToChat(message)
    # set default values
    newXposn = 0
    newZposn = 0
    num_of_args = len(sys.argv)
    if num_of_args == 3:
        # NOTE: This would be better handled in a try except for invalid input
        # Left out for clarity of example
        newXposn = float(sys.argv[1])
        newZposn = float(sys.argv[2])
    else:
        print("incorrect number of arguments")
        print("Usage: python script.py xCoord zCoord")
        print("Example usage: python script.py 9.2 8.5")
        sys.exit()

    newYposn = float(mc.getHeight(newXposn, newZposn))

    mc.player.setPos(newXposn, newYposn, newZposn)

    # Get the current position that the player is located at in the world
    player_position = mc.player.getPos()

    message = "You have been moved to ({0:.1f}, {1:.1f}, {2:.1f})".format(
              player_position.x, player_position.y, player_position.z)

    print(message)
    mc.postToChat(message)
