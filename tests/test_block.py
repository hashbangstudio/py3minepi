from minecraft.block import Block
from minecraft.block import BlockType


class TestBlock():

    def test_representation(self):
        # Test repr
        b = Block(2, 8)
        expected_string = "Block({:d}, {:d})".format(b.type, b.data)
        rep = repr(b)
        assert rep == expected_string

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
