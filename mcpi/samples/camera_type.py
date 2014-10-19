#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Runs through the different camera types in the minecraft world
"""

from __future__ import print_function, division, absolute_import, unicode_literals

from time import sleep

# import the needed modules for communication with minecraft world
# import needed block definitions
try:
    from ..minecraft import Minecraft
except ImportError:
    try:
        from .mcpi.minecraft import Minecraft
    except ImportError:
        from mcpi.minecraft import Minecraft


def send_to_chat_and_console(minecraft, message):
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

    # wait for 2 seconds
    sleep(2)
    # Follow the player
    send_to_chat_and_console(mc, "Set Camera to follow the player")
    mc.camera.setFollow()
    # wait for 4 seconds
    sleep(4)
    # Get the block that the player is currently in
    player_position = mc.player.getTilePos()
    send_to_chat_and_console(mc, "Set Camera to fixed position above ground")
    mc.camera.setFixed()
    mc.camera.setPos(player_position.x, player_position.y + 15, player_position.z)
    # wait for 4 seconds
    sleep(4)
    send_to_chat_and_console(mc, "Set Camera to normal player first person")
    mc.camera.setNormal()
