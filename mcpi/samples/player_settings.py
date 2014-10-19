#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Runs through changing player settings in the minecraft world
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


def send_to_chat_and_console(minecraft_world, message):
    """
        Print message to the python standard output (terminal or IDLE)
        and send message to the chat
    """
    print(message)
    # send message to the minecraft chat
    minecraft_world.postToChat(message)


if __name__ == "__main__":

    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()

    send_to_chat_and_console(mc, "Turning off AutoJump")
    mc.player.setting('autojump', 0)
    send_to_chat_and_console(mc, "Turning AutoJump back on in 10 seconds")
    sleep(10)
    send_to_chat_and_console(mc, "Turning on AutoJump")
    mc.player.setting('autojump', 1)
