from enum import IntEnum


class Block:
    """
    Minecraft PI block description. Can be sent to Minecraft.setBlock/s
    block.type = the blockID of a block (Its material)
    For example grass, sand, dirt or wool
    block.data = The variant of the type of block.
    For example the colour of wool or the orientation of stairs
    """
    def __init__(self, type, data=0):
        self.type = type
        self.data = data

    def __eq__(self, rhs):
        """
            Equality override
            Two blocks are equal only if both the type and data attributes are equal
            """
        return all([self.type == rhs.type, self.data == rhs.data])

    def __ne__(self, rhs):
        """
            not equal override
        """
        return not (self == rhs)

    def __hash__(self):
        """
            Override of hash generation
            Returns a hashed representation of contents of block
        """
        return (self.type << 8) + self.data

    def withData(self, data):
        """
            Returns a new block with the same type as the invoking block but
            with the passed in data value
        """
        return Block(self.type, data)

    def __iter__(self):
        """
            Returns an Iterator of the contents of the Block class
            Makes the Block an Iterable object
            This means that Block can be treated like a list/tuple in places
            list/tuple of type and data
            For example when flattening lists or *args
            Allows a Block to be sent whenever id [and data] is needed
        """
        return iter((self.type, self.data))

    def __repr__(self):
        """ Override string representation """
        return "Block(%d, %d)" % (self.type, self.data)

    @property
    def id(self):
        """ Here for backwards compatibility for previous attribute name """
        return self.type

AIR = Block(0)
STONE = Block(1)
GRASS = Block(2)
DIRT = Block(3)
COBBLESTONE = Block(4)
WOOD_PLANKS = Block(5)
SAPLING = Block(6)
BEDROCK = Block(7)
WATER_FLOWING = Block(8)
WATER = WATER_FLOWING
WATER_STATIONARY = Block(9)
LAVA_FLOWING = Block(10)
LAVA = LAVA_FLOWING
LAVA_STATIONARY = Block(11)
SAND = Block(12)
GRAVEL = Block(13)
GOLD_ORE = Block(14)
IRON_ORE = Block(15)
COAL_ORE = Block(16)
WOOD = Block(17)
LEAVES = Block(18)
GLASS = Block(20)
LAPIS_LAZULI_ORE = Block(21)
LAPIS_LAZULI_BLOCK = Block(22)
SANDSTONE = Block(24)
BED = Block(26)
COBWEB = Block(30)
GRASS_TALL = Block(31)
WOOL = Block(35)
FLOWER_YELLOW = Block(37)
FLOWER_CYAN = Block(38)
MUSHROOM_BROWN = Block(39)
MUSHROOM_RED = Block(40)
GOLD_BLOCK = Block(41)
IRON_BLOCK = Block(42)
STONE_SLAB_DOUBLE = Block(43)
STONE_SLAB = Block(44)
BRICK_BLOCK = Block(45)
TNT = Block(46)
BOOKSHELF = Block(47)
MOSS_STONE = Block(48)
OBSIDIAN = Block(49)
TORCH = Block(50)
FIRE = Block(51)
STAIRS_WOOD = Block(53)
CHEST = Block(54)
DIAMOND_ORE = Block(56)
DIAMOND_BLOCK = Block(57)
CRAFTING_TABLE = Block(58)
FARMLAND = Block(60)
FURNACE_INACTIVE = Block(61)
FURNACE_ACTIVE = Block(62)
DOOR_WOOD = Block(64)
LADDER = Block(65)
STAIRS_COBBLESTONE = Block(67)
DOOR_IRON = Block(71)
REDSTONE_ORE = Block(73)
SNOW = Block(78)
ICE = Block(79)
SNOW_BLOCK = Block(80)
CACTUS = Block(81)
CLAY = Block(82)
SUGAR_CANE = Block(83)
FENCE = Block(85)
GLOWSTONE_BLOCK = Block(89)
BEDROCK_INVISIBLE = Block(95)
STONE_BRICK = Block(98)
GLASS_PANE = Block(102)
MELON = Block(103)
FENCE_GATE = Block(107)
GLOWING_OBSIDIAN = Block(246)
NETHER_REACTOR_CORE = Block(247)

ALL_BLOCKS = (AIR, STONE, GRASS, DIRT, COBBLESTONE, WOOD_PLANKS, SAPLING, BEDROCK,
              WATER_FLOWING, WATER, WATER_STATIONARY, LAVA_FLOWING, LAVA, LAVA_STATIONARY,
              SAND, GRAVEL, GOLD_ORE, IRON_ORE, COAL_ORE, WOOD, LEAVES, GLASS,
              LAPIS_LAZULI_ORE, LAPIS_LAZULI_BLOCK, SANDSTONE, BED, COBWEB, GRASS_TALL,
              WOOL, FLOWER_YELLOW, FLOWER_CYAN, MUSHROOM_BROWN, MUSHROOM_RED,
              GOLD_BLOCK, IRON_BLOCK, STONE_SLAB_DOUBLE, STONE_SLAB, BRICK_BLOCK,
              TNT, BOOKSHELF, MOSS_STONE, OBSIDIAN, TORCH, FIRE, STAIRS_WOOD, CHEST,
              DIAMOND_ORE, DIAMOND_BLOCK, CRAFTING_TABLE, FARMLAND,
              FURNACE_INACTIVE, FURNACE_ACTIVE, DOOR_WOOD, LADDER,
              STAIRS_COBBLESTONE, DOOR_IRON, REDSTONE_ORE, SNOW, ICE, SNOW_BLOCK,
              CACTUS, CLAY, SUGAR_CANE, FENCE, GLOWSTONE_BLOCK, BEDROCK_INVISIBLE, STONE_BRICK,
              GLASS_PANE, MELON, FENCE_GATE, GLOWING_OBSIDIAN, NETHER_REACTOR_CORE, )


class BlockType(IntEnum):
    AIR = 0
    STONE = 1
    GRASS = 2
    DIRT = 3
    COBBLESTONE = 4
    WOOD_PLANKS = 5
    SAPLING = 6
    BEDROCK = 7
    WATER_FLOWING = 8
    WATER = WATER_FLOWING
    WATER_STATIONARY = 9
    LAVA_FLOWING = 10
    LAVA = LAVA_FLOWING
    LAVA_STATIONARY = 11
    SAND = 12
    GRAVEL = 13
    GOLD_ORE = 14
    IRON_ORE = 15
    COAL_ORE = 16
    WOOD = 17
    LEAVES = 18
    GLASS = 20
    LAPIS_LAZULI_ORE = 21
    LAPIS_LAZULI_BLOCK = 22
    SANDSTONE = 24
    BED = 26
    COBWEB = 30
    GRASS_TALL = 31
    WOOL = 35
    FLOWER_YELLOW = 37
    FLOWER_CYAN = 38
    MUSHROOM_BROWN = 39
    MUSHROOM_RED = 40
    GOLD_BLOCK = 41
    IRON_BLOCK = 42
    STONE_SLAB_DOUBLE = 43
    STONE_SLAB = 44
    BRICK_BLOCK = 45
    TNT = 46
    BOOKSHELF = 47
    MOSS_STONE = 48
    OBSIDIAN = 49
    TORCH = 50
    FIRE = 51
    STAIRS_WOOD = 53
    CHEST = 54
    DIAMOND_ORE = 56
    DIAMOND_BLOCK = 57
    CRAFTING_TABLE = 58
    FARMLAND = 60
    FURNACE_INACTIVE = 61
    FURNACE_ACTIVE = 62
    DOOR_WOOD = 64
    LADDER = 65
    STAIRS_COBBLESTONE = 67
    DOOR_IRON = 71
    REDSTONE_ORE = 73
    SNOW = 78
    ICE = 79
    SNOW_BLOCK = 80
    CACTUS = 81
    CLAY = 82
    SUGAR_CANE = 83
    FENCE = 85
    GLOWSTONE_BLOCK = 89
    BEDROCK_INVISIBLE = 95
    STONE_BRICK = 98
    GLASS_PANE = 102
    MELON = 103
    FENCE_GATE = 107
    GLOWING_OBSIDIAN = 246
    NETHER_REACTOR_CORE = 247
