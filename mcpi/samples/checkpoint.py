#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Runs through using checkpoints in the minecraft world
"""

from __future__ import print_function, division, absolute_import, unicode_literals

from time import sleep

# import the needed modules fo communication with minecraft world
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


def send_to_chat_console(minecraft, message):
    """
        print message to the python standard output (terminal or IDLE)
        Send message to the chat
    """
    print(message)
    # send message to the minecraft chat
    minecraft.postToChat(message)


if __name__ == "__main__":

    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()

    send_to_chat_console(mc, "Saving Checkpoint")
    # Save a checkpoint for the world state
    mc.saveCheckpoint()

    # wait for 2 seconds
    sleep(2)
    send_to_chat_console(mc, "Building Wall")
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

    # wait for 4 seconds
    sleep(4)

    send_to_chat_console(mc, "Restoring Checkpoint")
    # Set the world back to the state it was in at the last saved checkpoint
    mc.restoreCheckpoint()
