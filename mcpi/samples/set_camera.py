#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example usage of the Python Minecraft API
    Takes a camera mode and parameters to set the type of camera being used
    normal = first person view (entityId optional)
    Usage : python script.py normal [entityId]
    follow = follows entity looking straight down on them (entityId optional)
    Usage : python script.py follow [entityId]
    fixed = keeps camera at a fixed position pointing downwards
    Usage : python script.py fixed X Y Z
"""

from __future__ import print_function, division, absolute_import, unicode_literals

import sys

try:
    from ..minecraft import Minecraft
except ImportError:
    try:
        from .mcpi.minecraft import Minecraft
    except ImportError:
        from mcpi.minecraft import Minecraft


def print_available_camera_modes():
    """ Prints the available camera modes """
    print("Available camera modes are:")
    print("normal, follow, fixed")


def print_usage():
    """ Prints the usage information """
    print("Usage : python script.py normal [entityId]")
    print("Usage : python script.py follow [entityId]")
    print("Usage : python script.py fixed Xcoord Ycoord Zcoord")


# this means that the file can be imported without
# executing anything in this code block
if __name__ == "__main__":

    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()

    min_num_of_params = 1
    # Remember that this also includes the script name
    num_of_params_given = len(sys.argv) - 1

    if num_of_params_given >= min_num_of_params:
        camera_mode = sys.argv[1]

        if camera_mode == "follow":
            if num_of_params_given == 1:
                mc.camera.setFollow()
            elif num_of_params_given == 2 and sys.argv[2].isdigit():
                mc.camera.setFollow(sys.argv[2])
            else:
                print(("Expected 1 or 2 parameters but got " +
                      str(num_of_params_given)))
                print_usage()
                sys.exit()
        elif camera_mode == "normal":
            if num_of_params_given == 1:
                mc.camera.setNormal()
            elif num_of_params_given == 2 and sys.argv[2].isdigit():
                mc.camera.setNormal(sys.argv[2])
            else:
                print(("Expected 1 or 2 parameters but got " +
                       str(num_of_params_given)))
                print_usage()
                sys.exit()
        elif camera_mode == "fixed":
            if num_of_params_given == 4:
                # should verify arguments are integer coordinates
                mc.camera.setFixed()
                mc.camera.setPos(sys.argv[2],
                                 sys.argv[3],
                                 sys.argv[4])
            else:
                print("insufficient parameters given")
                print(("Require 4 but got " + str(num_of_params_given)))
                print_usage()
                sys.exit()
        else:
            print(("unknown camera mode parameter given " + sys.argv[1]))
            print_available_camera_modes()
            print_usage()
            sys.exit()
    else:
        print("insufficient parameters given")
        print(("Require minimum of " + str(min_num_of_params) +
               ", got " + str(num_of_params_given)))
        print_usage()
        sys.exit()
