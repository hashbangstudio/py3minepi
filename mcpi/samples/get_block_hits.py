#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Polls for block hits and then prints them to console if they have occurred
    Press Ctrl+c to exit the script
"""

from __future__ import print_function, division, absolute_import, unicode_literals

# Only need to poll every so often
from time import sleep

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

    while(True):
        hits = mc.events.pollBlockHits()
        if len(hits) > 0:
            print(hits)
        sleep(1)
