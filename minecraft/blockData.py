from enum import IntEnum


# available 0-1 affects whether striking block sets off fuse
class Tnt_type(IntEnum):
    SAFE = 0
    ARMED = 1


# available range 0-15 affects colour of wool block
class Color(IntEnum):
    WHITE = 0
    ORANGE = 1
    MAGENTA = 2
    LIGHT_BLUE = 3
    YELLOW = 4
    LIME = 5
    PINK = 6
    GREY = 7
    GRAY = 7
    LIGHT_GREY = 8
    LIGHT_GRAY = 8
    CYAN = 9
    PURPLE = 10
    BLUE = 11
    BROWN = 12
    GREEN = 13
    RED = 14
    BLACK = 15


# only 0-2 seem to do anything for texture
# 0 to 3 is type beyond that is decay counter
# avilable range 0-15
class Leaves_type(IntEnum):
    OAK = 0
    PINE = 1
    SPRUCE = 1
    BIRCH = 2
    JUNGLE = 3


# only 0-2 seem to do anything
# available values 0-15 affects texture and rotation
class Wood_planks_type(IntEnum):
    OAK_UP = 0
    SPRUCE_UP = 1
    BIRCH_UP = 2
    JUNGLE_UP = 3
    OAK_EAST = 4
    SPRUCE_EAST = 5
    BIRCH_EAST = 6
    JUNGLE_EAST = 7
    OAK_NORTH = 8
    SPRUCE_NORTH = 9
    BIRCH_NORTH = 10
    JUNGLE_NORTH = 11
    OAK_BARK = 12
    SPRUCE_BARK = 13
    BIRCH_BARK = 14
    JUNGLE_BARK = 15


# available 0-15
# 6,7,14 and 15 don't work (uses default stone)
class Slab(IntEnum):
    STONE = 0
    SANDSTONE = 1
    WOODEN = 2
    COBBLESTONE = 3
    BRICK = 4
    STONE_BRICK = 5
    # JUST IS STONE
    NETHER_BRICK = 6
    # JUST IS STONE
    QUARTZ = 7
    STONE_TOP = 8
    SANDSTONE_TOP = 9
    WOODEN_TOP = 10
    COBBLESTONE_TOP = 11
    BRICK_TOP = 12
    STONE_BRICK_TOP = 13
    # JUST IS STONE
    NETHER_BRICK_TOP = 14
    # JUST IS STONE
    QUARTZ_TOP = 15


# available 0-15
# only 1 to 5 does anything
# 6 and 7 wil use default stone
# above that just cycles back round
class Double_slab_type(IntEnum):
    STONE = 0
    SANDSTONE = 1
    WOODEN = 2
    COBBLESTONE = 3
    BRICK = 4
    STONE_BRICK = 5
    # JUST IS STONE
    NETHER_BRICK = 6
    # JUST IS STONE
    QUARTZ = 7


# available 0 to 2
class Sandstone_type(IntEnum):
    SANDSTONE = 0
    CHISELED = 1
    SMOOTH = 2


# available 0 to 3
class Bed_type(IntEnum):
    SOUTH = 0
    WEST = 1
    NORTH = 2
    EAST = 3


# available 0 to 3
# no effect seemingly
class Grass_type(IntEnum):
    SHRUB = 0
    GRASS = 1
    FERN = 2
    BIOME_SHRUB = 3


# direction of ascending 0 to 7 available
# 0 to 3 for normal stairs 4-7 for inverted stairs
class Stairs_type(IntEnum):
    EAST = 0
    WEST = 1
    SOUTH = 2
    NORTH = 3
    EAST_INVERTED = 4
    WEST_INVERTED = 5
    SOUTH_INVERTED = 6
    NORTH_INVERTED = 7


class Door_type(IntEnum):
    NORTHWEST = 0
    NORTHEAST = 1
    SOUTHEAST = 2
    SOUTHWEST = 3
    NORTHWEST_SWUNG = 4
    NORTHEAST_SWUNG = 5
    SOUTHEAST_SWUNG = 6
    SOUTHWEST_SWUNG = 7
    NORTHWEST_TOP = 8
    NORTHEAST_TOP = 9
    SOUTHEAST_TOP = 10
    SOUTHWEST_TOP = 11
    NORTHWEST_TOP_SWUNG = 12
    NORTHEAST_TOP_SWUNG = 13
    SOUTHEAST_TOP_SWUNG = 14
    SOUTHWEST_TOP_SWUNG = 15
