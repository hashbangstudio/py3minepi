#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Sets the Tile that the player is on/in from command line arguments (x z)
    Player's height set from getHeight()
    For given horizontal position (x, z)
    y = height of the world at horizontal posn
    player position set to (x, y, z)
    Usage: python script.py xCoord zCoord
    Example usage: python script.py 9 -8
"""

from __future__ import print_function, division, absolute_import, unicode_literals

# We have to import the minecraft module to do anything in the minecraft world
import sys

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

    # create the output message as a string
    message = "You are at ({0:.1f}, {1:.1f}, {2:.1f})".format(player_position.x,
                                                              player_position.y,
                                                              player_position.z)

    # print to the python interpreter standard output (terminal or IDLE)
    print(message)

    # send message to the minecraft chat
    mc.postToChat(message)
    # Set Default values
    newXposn = 0
    newZposn = 0
    num_of_args = len(sys.argv)
    if num_of_args == 3:
        # Use float first in case argument is '3.3' string to avoid value error
        newXposn = int(float(sys.argv[1]))
        newZposn = int(float(sys.argv[2]))
    else:
        print("incorrect number of arguments")
        print("Usage: python script.py xCoord zCoord")
        print("Example usage: python script.py 9 -8")
        sys.exit()

    newYposn = mc.getHeight(newXposn, newZposn)

    mc.player.setTilePos(newXposn, newYposn, newZposn)

    # Get the current tile/block that the player is located at in the world
    player_position = mc.player.getTilePos()

    message = "You have been moved to  ({0:.1f}, {1:.1f}, {2:.1f})".format(
                player_position.x, player_position.y, player_position.z)

    print(message)
    mc.postToChat(message)
