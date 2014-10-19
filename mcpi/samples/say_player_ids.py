#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Gets a list of the Ids of all players in world
    Prints the list to standard output and the minecraft chat
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


# this means that the file can be imported without
# executing anything in this code block
if __name__ == "__main__":

    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()

    allIds = mc.getPlayerEntityIds()

    # create the output message as a string
    messages = ["There are {:d} player(s)".format(len(allIds))]

    # index in for loop starting at 1
    for player, entId in enumerate(allIds, 1):
        messages.append("player {:d} has id = {:d}".format(player, entId))

    for msg in messages:
        # print to the python interpreter standard output (terminal or IDLE)
        print(msg)

        # send message to the minecraft chat
        mc.postToChat(msg)
