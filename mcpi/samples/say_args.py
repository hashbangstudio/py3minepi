#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Sends a single command line argument to the chat
    Usage: python script.py "message to send"
"""

from __future__ import print_function, division, absolute_import, unicode_literals
# We have to import sys module to get the command line arguments
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

    # sys.argv is a list of script_name and any command arguments given
    # therefore the number of arguments is one less than this
    num_of_arguments = len(sys.argv) - 1

    # Check that have the appropriate number of command line arguments
    # one argument is required in this case
    if (num_of_arguments == 1):
        # create the output message as a string
        # NOTE: this is [1] as [0] contains the script name
        message = sys.argv[1]

        # print to the python interpreter standard output (terminal or IDLE)
        print(message)

        # send message to the minecraft chat
        mc.postToChat(message)
    else:
        print(("Expected only one argument, but received {:d}".format(num_of_arguments)))
