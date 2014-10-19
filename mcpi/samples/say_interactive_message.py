#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Asks for input at the console and sends that to the chat
"""

from __future__ import print_function, division, absolute_import, unicode_literals
import sys

# We have to import the minecraft module to do anything in the minecraft world
try:
    from ..minecraft import Minecraft
except ImportError:
    try:
        from .mcpi.minecraft import Minecraft
    except ImportError:
        from mcpi.minecraft import Minecraft

if __name__ == "__main__":

    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()

    prompt = "Please enter some text to send to the chat: "

    # Get the output message as a string from keyboard input
    if sys.version_info[:1] == (3,):
        message = input(prompt)
    else:
        message = raw_input(prompt)

    # print to the python interpreter standard output (terminal or IDLE)
    print(message)

    # send message to the minecraft chat
    mc.postToChat(message)
