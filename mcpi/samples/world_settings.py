#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Runs through changing various world settings in the minecraft world
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

    send_to_chat_and_console(mc, "Making World unbreakable")
    mc.setting('world_immutable', 1)
    # wait for 8 seconds
    sleep(8)
    send_to_chat_and_console(mc, "Making World breakable")
    mc.setting('world_immutable', 0)
    # wait for 4 seconds
    sleep(4)
    # Follow the player
    send_to_chat_and_console(mc, "Set Camera to follow the player")
    mc.camera.setFollow()
    # wait for 4 seconds
    sleep(4)
    send_to_chat_and_console(mc, "Making nametags visible")
    mc.setting('nametags_visible', 1)
    # wait for 6 seconds
    sleep(6)
    send_to_chat_and_console(mc, "Making nametags invisible")
    mc.setting('nametags_visible', 0)
    # wait for 4 seconds
    sleep(4)
    send_to_chat_and_console(mc, "Set Camera to normal player first person")
    mc.camera.setNormal()
