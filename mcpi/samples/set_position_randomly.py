#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Moves the position of the player a random amount from current position
"""

from __future__ import print_function, division, absolute_import, unicode_literals

# Required to generate random numbers
from random import randint

# We have to import the minecraft module to do anything in the minecraft world
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
    message = ("You are at (" + str(player_position.x) + ", "
               + str(player_position.y) + ", "
               + str(player_position.z) + ")")

    # print to the python interpreter standard output (terminal or IDLE )
    print(message)

    # Send message to the minecraft chat
    mc.postToChat(message)

    # Randomly generates the amount to shift position by
    xShift = randint(-10, 10)
    zShift = randint(-10, 10)
    # Set variables for the new position
    newXposn = player_position.x + xShift
    newZposn = player_position.z + zShift
    # Set y position to be the height of the world so not in middle of a block
    newYposn = mc.getHeight(newXposn, newZposn)
    # Set the position of the player
    mc.player.setTilePos(newXposn, newYposn, newZposn)
    # Get the current tile/block that the player is located at in the world
    player_position = mc.player.getTilePos()

    message = ("You have been moved to (" + str(player_position.x) + ", "
               + str(player_position.y) + ", "
               + str(player_position.z) + ")")

    # print message and send to the chat
    print(message)
    mc.postToChat(message)
