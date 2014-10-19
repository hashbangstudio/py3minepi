#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Gets the position of the player and sends it to the chat
"""

from __future__ import print_function, division, absolute_import, unicode_literals

# We have to import the minecraft module to do anything in the minecraft world
try:
    from ..minecraft import Minecraft
except ImportError:
    try:
        from .mcpi.minecraft import Minecraft
    except ImportError:
        from mcpi.minecraft import Minecraft


# Ensures that code in block is only run if script directly invoked
if __name__ == "__main__":

    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()

    # Get the block that the player is currently in
    player_position = mc.player.getPos()

    # create the output message as a string
    message = "You are at ({0:.1f}, {1:.1f}, {2:.1f})".format(player_position.x,
                                                              player_position.y,
                                                              player_position.z)

    # print to the python interpreter standard output (terminal or IDLE)
    print(message)

    # send message to the minecraft chat
    mc.postToChat(message)
