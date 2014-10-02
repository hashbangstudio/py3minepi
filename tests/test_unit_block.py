import unittest
from minecraft.block import Block
from minecraft.block import BlockType


class TestBlock(unittest.TestCase):

    def test_representation(self):
        # Test repr
        b = Block(2, 8)
        expected_string = "Block({:d}, {:d})".format(b.type, b.data)
        rep = repr(b)
        self.assertEqual(rep, expected_string)

    def test_instantiation_and_with_data_function(self):
        block = Block(12)
        self.assertEqual(block.type, 12)
        self.assertEqual(block.data, 0)
        block_with_data = Block(12, 4)
        self.assertEqual(block_with_data.type, 12)
        self.assertEqual(block_with_data.data, 4)
        otherBlckWithData = block.withData(8)
        self.assertEqual(otherBlckWithData.type, 12)
        self.assertEqual(otherBlckWithData.data, 8)

    def test_backwards_compatibility(self):
        block = Block(12)
        self.assertEqual(block.type, block.id)

    def test_equality(self):
        b1 = Block(8, 3)
        b_same = Block(8, 3)
        b_diff_id = Block(12, 3)
        b_diff_data = Block(8, 7)
        b_diff_id_and_data = Block(51, 7)

        self.assertTrue(b1 == b1)
        self.assertTrue(b1 == b_same)
        self.assertTrue(b1 != b_diff_id)
        self.assertTrue(b1 != b_diff_data)
        self.assertTrue(b1 != b_diff_id_and_data)

    def test_iteration(self):
        id_and_data = [35, 4]
        b = Block(id_and_data[0], id_and_data[1])
        for index, attr in enumerate(b):
            self.assertEqual(attr, id_and_data[index])

    def test_block_constants_aliases(self):
        self.assertEqual(BlockType.WATER,  BlockType.WATER_FLOWING)
        self.assertEqual(BlockType.LAVA,  BlockType.LAVA_FLOWING)

    def test_block_constants(self):
        self.assertEqual(BlockType.AIR,  0)
        self.assertEqual(BlockType.STONE,  1)
        self.assertEqual(BlockType.GRASS,  2)
        self.assertEqual(BlockType.DIRT,  3)
        self.assertEqual(BlockType.COBBLESTONE, 4)
        self.assertEqual(BlockType.WOOD_PLANKS,  5)
        self.assertEqual(BlockType.SAPLING,  6)
        self.assertEqual(BlockType.BEDROCK,  7)
        self.assertEqual(BlockType.WATER_FLOWING,  8)
        self.assertEqual(BlockType.WATER_STATIONARY, 9)
        self.assertEqual(BlockType.LAVA_FLOWING,  10)
        self.assertEqual(BlockType.LAVA_STATIONARY, 11)
        self.assertEqual(BlockType.SAND,  12)
        self.assertEqual(BlockType.GRAVEL,  13)
        self.assertEqual(BlockType.GOLD_ORE,  14)
        self.assertEqual(BlockType.IRON_ORE,  15)
        self.assertEqual(BlockType.COAL_ORE,  16)
        self.assertEqual(BlockType.WOOD,  17)
        self.assertEqual(BlockType.LEAVES,  18)
        self.assertEqual(BlockType.GLASS,  20)
        self.assertEqual(BlockType.LAPIS_LAZULI_ORE, 21)
        self.assertEqual(BlockType.LAPIS_LAZULI_BLOCK, 22)
        self.assertEqual(BlockType.SANDSTONE,  24)
        self.assertEqual(BlockType.BED,  26)
        self.assertEqual(BlockType.COBWEB,  30)
        self.assertEqual(BlockType.GRASS_TALL,  31)
        self.assertEqual(BlockType.WOOL,  35)
        self.assertEqual(BlockType.FLOWER_YELLOW,  37)
        self.assertEqual(BlockType.FLOWER_CYAN,  38)
        self.assertEqual(BlockType.MUSHROOM_BROWN,  39)
        self.assertEqual(BlockType.MUSHROOM_RED,  40)
        self.assertEqual(BlockType.GOLD_BLOCK,  41)
        self.assertEqual(BlockType.IRON_BLOCK,  42)
        self.assertEqual(BlockType.STONE_SLAB_DOUBLE, 43)
        self.assertEqual(BlockType.STONE_SLAB,  44)
        self.assertEqual(BlockType.BRICK_BLOCK,  45)
        self.assertEqual(BlockType.TNT,  46)
        self.assertEqual(BlockType.BOOKSHELF,  47)
        self.assertEqual(BlockType.MOSS_STONE,  48)
        self.assertEqual(BlockType.OBSIDIAN,  49)
        self.assertEqual(BlockType.TORCH,  50)
        self.assertEqual(BlockType.FIRE,  51)
        self.assertEqual(BlockType.STAIRS_WOOD,  53)
        self.assertEqual(BlockType.CHEST,  54)
        self.assertEqual(BlockType.DIAMOND_ORE,  56)
        self.assertEqual(BlockType.DIAMOND_BLOCK,  57)
        self.assertEqual(BlockType.CRAFTING_TABLE,  58)
        self.assertEqual(BlockType.FARMLAND,  60)
        self.assertEqual(BlockType.FURNACE_INACTIVE, 61)
        self.assertEqual(BlockType.FURNACE_ACTIVE,  62)
        self.assertEqual(BlockType.DOOR_WOOD,  64)
        self.assertEqual(BlockType.LADDER,  65)
        self.assertEqual(BlockType.STAIRS_COBBLESTONE, 67)
        self.assertEqual(BlockType.DOOR_IRON,  71)
        self.assertEqual(BlockType.REDSTONE_ORE,  73)
        self.assertEqual(BlockType.SNOW,  78)
        self.assertEqual(BlockType.ICE,  79)
        self.assertEqual(BlockType.SNOW_BLOCK,  80)
        self.assertEqual(BlockType.CACTUS,  81)
        self.assertEqual(BlockType.CLAY,  82)
        self.assertEqual(BlockType.SUGAR_CANE,  83)
        self.assertEqual(BlockType.FENCE,  85)
        self.assertEqual(BlockType.GLOWSTONE_BLOCK, 89)
        self.assertEqual(BlockType.BEDROCK_INVISIBLE, 95)
        self.assertEqual(BlockType.STONE_BRICK,  98)
        self.assertEqual(BlockType.GLASS_PANE,  102)
        self.assertEqual(BlockType.MELON,  103)
        self.assertEqual(BlockType.FENCE_GATE,  107)
        self.assertEqual(BlockType.GLOWING_OBSIDIAN, 246)
        self.assertEqual(BlockType.NETHER_REACTOR_CORE, 247)
