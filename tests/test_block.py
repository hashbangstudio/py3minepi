"""
Tests for the Block, BlockType classes and named Block instances
"""
from mcpi import block
from mcpi.block import Block
from mcpi.block import BlockType


block.Block(block.AIR)


class TestBlock():

    def test_representation(self):
        # Test repr
        b = Block(2, 8)
        expected_string = "Block(2, 8)"
        rep = repr(b)
        assert rep == expected_string
        blk = eval(repr(b))
        assert blk == b

    def test_instantiation_and_with_data_function(self):
        block = Block(12)
        assert block.type == 12
        assert block.data == 0

        block_and_data = Block(12, 4)
        assert block_and_data.type == 12
        assert block_and_data.data == 4

        other_block_with_data = block.withData(8)
        assert other_block_with_data.type == 12
        assert other_block_with_data.data == 8

    def test_backwards_compatibility(self):
        block = Block(12)
        assert block.type == block.id

    def test_equality(self):
        b1 = Block(8, 3)
        b_same = Block(8, 3)
        b_diff_id = Block(12, 3)
        b_diff_data = Block(8, 7)
        b_diff_id_and_data = Block(51, 7)

        assert b1 == b1
        assert b1 == b_same
        assert b1 != b_diff_id
        assert b1 != b_diff_data
        assert b1 != b_diff_id_and_data

    def test_iteration(self):
        id_and_data = [35, 4]
        b = Block(id_and_data[0], id_and_data[1])
        for index, attr in enumerate(b):
            assert attr == id_and_data[index]

    def test_block_constants_aliases(self):
        assert BlockType.WATER == BlockType.WATER_FLOWING
        assert BlockType.LAVA == BlockType.LAVA_FLOWING

    def test_block_constants(self):
        assert BlockType.AIR == 0
        assert BlockType.STONE == 1
        assert BlockType.GRASS == 2
        assert BlockType.DIRT == 3
        assert BlockType.COBBLESTONE == 4
        assert BlockType.WOOD_PLANKS == 5
        assert BlockType.SAPLING == 6
        assert BlockType.BEDROCK == 7
        assert BlockType.WATER_FLOWING == 8
        assert BlockType.WATER_STATIONARY == 9
        assert BlockType.LAVA_FLOWING == 10
        assert BlockType.LAVA_STATIONARY == 11
        assert BlockType.SAND == 12
        assert BlockType.GRAVEL == 13
        assert BlockType.GOLD_ORE == 14
        assert BlockType.IRON_ORE == 15
        assert BlockType.COAL_ORE == 16
        assert BlockType.WOOD == 17
        assert BlockType.LEAVES == 18
        assert BlockType.GLASS == 20
        assert BlockType.LAPIS_LAZULI_ORE == 21
        assert BlockType.LAPIS_LAZULI_BLOCK == 22
        assert BlockType.SANDSTONE == 24
        assert BlockType.BED == 26
        assert BlockType.COBWEB == 30
        assert BlockType.GRASS_TALL == 31
        assert BlockType.WOOL == 35
        assert BlockType.FLOWER_YELLOW == 37
        assert BlockType.FLOWER_CYAN == 38
        assert BlockType.MUSHROOM_BROWN == 39
        assert BlockType.MUSHROOM_RED == 40
        assert BlockType.GOLD_BLOCK == 41
        assert BlockType.IRON_BLOCK == 42
        assert BlockType.STONE_SLAB_DOUBLE == 43
        assert BlockType.STONE_SLAB == 44
        assert BlockType.BRICK_BLOCK == 45
        assert BlockType.TNT == 46
        assert BlockType.BOOKSHELF == 47
        assert BlockType.MOSS_STONE == 48
        assert BlockType.OBSIDIAN == 49
        assert BlockType.TORCH == 50
        assert BlockType.FIRE == 51
        assert BlockType.STAIRS_WOOD == 53
        assert BlockType.CHEST == 54
        assert BlockType.DIAMOND_ORE == 56
        assert BlockType.DIAMOND_BLOCK == 57
        assert BlockType.CRAFTING_TABLE == 58
        assert BlockType.FARMLAND == 60
        assert BlockType.FURNACE_INACTIVE == 61
        assert BlockType.FURNACE_ACTIVE == 62
        assert BlockType.DOOR_WOOD == 64
        assert BlockType.LADDER == 65
        assert BlockType.STAIRS_COBBLESTONE == 67
        assert BlockType.DOOR_IRON == 71
        assert BlockType.REDSTONE_ORE == 73
        assert BlockType.SNOW == 78
        assert BlockType.ICE == 79
        assert BlockType.SNOW_BLOCK == 80
        assert BlockType.CACTUS == 81
        assert BlockType.CLAY == 82
        assert BlockType.SUGAR_CANE == 83
        assert BlockType.FENCE == 85
        assert BlockType.GLOWSTONE_BLOCK == 89
        assert BlockType.BEDROCK_INVISIBLE == 95
        assert BlockType.STONE_BRICK == 98
        assert BlockType.GLASS_PANE == 102
        assert BlockType.MELON == 103
        assert BlockType.FENCE_GATE == 107
        assert BlockType.GLOWING_OBSIDIAN == 246
        assert BlockType.NETHER_REACTOR_CORE == 247

    def test_block_instances(self):
        assert block.AIR == Block(0, 0)
        assert block.STONE == Block(1, 0)
        assert block.GRASS == Block(2, 0)
        assert block.DIRT == Block(3, 0)
        assert block.COBBLESTONE == Block(4, 0)
        assert block.WOOD_PLANKS == Block(5, 0)
        assert block.SAPLING == Block(6, 0)
        assert block.BEDROCK == Block(7, 0)
        assert block.WATER_FLOWING == Block(8, 0)
        assert block.WATER_STATIONARY == Block(9, 0)
        assert block.LAVA_FLOWING == Block(10, 0)
        assert block.LAVA_STATIONARY == Block(11, 0)
        assert block.SAND == Block(12, 0)
        assert block.GRAVEL == Block(13, 0)
        assert block.GOLD_ORE == Block(14, 0)
        assert block.IRON_ORE == Block(15, 0)
        assert block.COAL_ORE == Block(16, 0)
        assert block.WOOD == Block(17, 0)
        assert block.LEAVES == Block(18, 0)
        assert block.GLASS == Block(20, 0)
        assert block.LAPIS_LAZULI_ORE == Block(21, 0)
        assert block.LAPIS_LAZULI_BLOCK == Block(22, 0)
        assert block.SANDSTONE == Block(24, 0)
        assert block.BED == Block(26, 0)
        assert block.COBWEB == Block(30, 0)
        assert block.GRASS_TALL == Block(31, 0)
        assert block.WOOL == Block(35, 0)
        assert block.FLOWER_YELLOW == Block(37, 0)
        assert block.FLOWER_CYAN == Block(38, 0)
        assert block.MUSHROOM_BROWN == Block(39, 0)
        assert block.MUSHROOM_RED == Block(40, 0)
        assert block.GOLD_BLOCK == Block(41, 0)
        assert block.IRON_BLOCK == Block(42, 0)
        assert block.STONE_SLAB_DOUBLE == Block(43, 0)
        assert block.STONE_SLAB == Block(44, 0)
        assert block.BRICK_BLOCK == Block(45, 0)
        assert block.TNT == Block(46, 0)
        assert block.BOOKSHELF == Block(47, 0)
        assert block.MOSS_STONE == Block(48, 0)
        assert block.OBSIDIAN == Block(49, 0)
        assert block.TORCH == Block(50, 0)
        assert block.FIRE == Block(51, 0)
        assert block.STAIRS_WOOD == Block(53, 0)
        assert block.CHEST == Block(54, 0)
        assert block.DIAMOND_ORE == Block(56, 0)
        assert block.DIAMOND_BLOCK == Block(57, 0)
        assert block.CRAFTING_TABLE == Block(58, 0)
        assert block.FARMLAND == Block(60, 0)
        assert block.FURNACE_INACTIVE == Block(61, 0)
        assert block.FURNACE_ACTIVE == Block(62, 0)
        assert block.DOOR_WOOD == Block(64, 0)
        assert block.LADDER == Block(65, 0)
        assert block.STAIRS_COBBLESTONE == Block(67, 0)
        assert block.DOOR_IRON == Block(71, 0)
        assert block.REDSTONE_ORE == Block(73, 0)
        assert block.SNOW == Block(78, 0)
        assert block.ICE == Block(79, 0)
        assert block.SNOW_BLOCK == Block(80, 0)
        assert block.CACTUS == Block(81, 0)
        assert block.CLAY == Block(82, 0)
        assert block.SUGAR_CANE == Block(83, 0)
        assert block.FENCE == Block(85, 0)
        assert block.GLOWSTONE_BLOCK == Block(89, 0)
        assert block.BEDROCK_INVISIBLE == Block(95, 0)
        assert block.STONE_BRICK == Block(98, 0)
        assert block.GLASS_PANE == Block(102, 0)
        assert block.MELON == Block(103, 0)
        assert block.FENCE_GATE == Block(107, 0)
        assert block.GLOWING_OBSIDIAN == Block(246, 0)
        assert block.NETHER_REACTOR_CORE == Block(247, 0)

    def test_block_constants_equal_instances(self):
        assert BlockType.AIR == block.AIR.id
        assert BlockType.STONE == block.STONE.id
        assert BlockType.GRASS == block.GRASS.id
        assert BlockType.DIRT == block.DIRT.id
        assert BlockType.COBBLESTONE == block.COBBLESTONE.id
        assert BlockType.WOOD_PLANKS == block.WOOD_PLANKS.id
        assert BlockType.SAPLING == block.SAPLING.id
        assert BlockType.BEDROCK == block.BEDROCK.id
        assert BlockType.WATER_FLOWING == block.WATER_FLOWING.id
        assert BlockType.WATER_STATIONARY == block.WATER_STATIONARY.id
        assert BlockType.LAVA_FLOWING == block.LAVA_FLOWING.id
        assert BlockType.LAVA_STATIONARY == block.LAVA_STATIONARY.id
        assert BlockType.SAND == block.SAND.id
        assert BlockType.GRAVEL == block.GRAVEL.id
        assert BlockType.GOLD_ORE == block.GOLD_ORE.id
        assert BlockType.IRON_ORE == block.IRON_ORE.id
        assert BlockType.COAL_ORE == block.COAL_ORE.id
        assert BlockType.WOOD == block.WOOD.id
        assert BlockType.LEAVES == block.LEAVES.id
        assert BlockType.GLASS == block.GLASS.id
        assert BlockType.LAPIS_LAZULI_ORE == block.LAPIS_LAZULI_ORE.id
        assert BlockType.LAPIS_LAZULI_BLOCK == block.LAPIS_LAZULI_BLOCK.id
        assert BlockType.SANDSTONE == block.SANDSTONE.id
        assert BlockType.BED == block.BED.id
        assert BlockType.COBWEB == block.COBWEB.id
        assert BlockType.GRASS_TALL == block.GRASS_TALL.id
        assert BlockType.WOOL == block.WOOL.id
        assert BlockType.FLOWER_YELLOW == block.FLOWER_YELLOW.id
        assert BlockType.FLOWER_CYAN == block.FLOWER_CYAN.id
        assert BlockType.MUSHROOM_BROWN == block.MUSHROOM_BROWN.id
        assert BlockType.MUSHROOM_RED == block.MUSHROOM_RED.id
        assert BlockType.GOLD_BLOCK == block.GOLD_BLOCK.id
        assert BlockType.IRON_BLOCK == block.IRON_BLOCK.id
        assert BlockType.STONE_SLAB_DOUBLE == block.STONE_SLAB_DOUBLE.id
        assert BlockType.STONE_SLAB == block.STONE_SLAB.id
        assert BlockType.BRICK_BLOCK == block.BRICK_BLOCK.id
        assert BlockType.TNT == block.TNT.id
        assert BlockType.BOOKSHELF == block.BOOKSHELF.id
        assert BlockType.MOSS_STONE == block.MOSS_STONE.id
        assert BlockType.OBSIDIAN == block.OBSIDIAN.id
        assert BlockType.TORCH == block.TORCH.id
        assert BlockType.FIRE == block.FIRE.id
        assert BlockType.STAIRS_WOOD == block.STAIRS_WOOD.id
        assert BlockType.CHEST == block.CHEST.id
        assert BlockType.DIAMOND_ORE == block.DIAMOND_ORE.id
        assert BlockType.DIAMOND_BLOCK == block.DIAMOND_BLOCK.id
        assert BlockType.CRAFTING_TABLE == block.CRAFTING_TABLE.id
        assert BlockType.FARMLAND == block.FARMLAND.id
        assert BlockType.FURNACE_INACTIVE == block.FURNACE_INACTIVE.id
        assert BlockType.FURNACE_ACTIVE == block.FURNACE_ACTIVE.id
        assert BlockType.DOOR_WOOD == block.DOOR_WOOD.id
        assert BlockType.LADDER == block.LADDER.id
        assert BlockType.STAIRS_COBBLESTONE == block.STAIRS_COBBLESTONE.id
        assert BlockType.DOOR_IRON == block.DOOR_IRON.id
        assert BlockType.REDSTONE_ORE == block.REDSTONE_ORE.id
        assert BlockType.SNOW == block.SNOW.id
        assert BlockType.ICE == block.ICE.id
        assert BlockType.SNOW_BLOCK == block.SNOW_BLOCK.id
        assert BlockType.CACTUS == block.CACTUS.id
        assert BlockType.CLAY == block.CLAY.id
        assert BlockType.SUGAR_CANE == block.SUGAR_CANE.id
        assert BlockType.FENCE == block.FENCE.id
        assert BlockType.GLOWSTONE_BLOCK == block.GLOWSTONE_BLOCK.id
        assert BlockType.BEDROCK_INVISIBLE == block.BEDROCK_INVISIBLE.id
        assert BlockType.STONE_BRICK == block.STONE_BRICK.id
        assert BlockType.GLASS_PANE == block.GLASS_PANE.id
        assert BlockType.MELON == block.MELON.id
        assert BlockType.FENCE_GATE == block.FENCE_GATE.id
        assert BlockType.GLOWING_OBSIDIAN == block.GLOWING_OBSIDIAN.id
        assert BlockType.NETHER_REACTOR_CORE == block.NETHER_REACTOR_CORE.id
