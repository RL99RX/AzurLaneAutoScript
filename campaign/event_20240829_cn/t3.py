from .campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger
from .t1 import Config as ConfigBase

MAP = CampaignMap('T3')
<<<<<<< HEAD
MAP.shape = 'I8'
MAP.camera_data = ['D2', 'D6', 'F2', 'F6']
MAP.camera_data_spawn_point = ['D6']
MAP.map_data = """
    ++ ++ Me -- MB -- ++ -- --
    ++ ++ -- ME -- ME ++ Me ME
    -- ME -- -- __ -- Me -- --
    -- ME -- ++ -- -- -- -- ME
    -- ++ MS ++ MS ++ -- -- ME
    -- Me -- -- -- MS -- Me --
    ME -- -- -- -- -- -- ++ ++
    ++ ++ ++ SP SP ++ ME -- ++
=======
MAP.shape = 'I10'
MAP.camera_data = ['D5', 'D8', 'F5']
MAP.camera_data_spawn_point = ['D8']
MAP.map_data = """
    -- -- -- ++ ++ ++ -- -- --
    -- -- -- ++ ++ ++ -- -- --
    ++ ++ ++ ++ ++ ++ ++ ++ ++
    ME -- ME -- MB -- ME -- ME
    -- ME -- -- __ -- -- ME --
    -- -- -- -- Me -- -- -- --
    ++ Me -- MS ++ MS ++ ++ ++
    ME -- -- -- MS -- Me -- --
    -- Me ++ -- -- -- ++ ++ --
    -- -- ++ SP -- SP ++ ++ --
>>>>>>> 289c592f8f6fbf61cf9c2675f29b2af6d20e2da0
"""
MAP.weight_data = """
    50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50
<<<<<<< HEAD
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 3, 'siren': 2},
    {'battle': 1, 'enemy': 2},
    {'battle': 2, 'enemy': 1},
    {'battle': 3, 'enemy': 1},
    {'battle': 4},
=======
    50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 2, 'siren': 2},
    {'battle': 1, 'enemy': 2, 'siren': 1},
    {'battle': 2, 'enemy': 2},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 1},
>>>>>>> 289c592f8f6fbf61cf9c2675f29b2af6d20e2da0
    {'battle': 5, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, I1, \
A2, B2, C2, D2, E2, F2, G2, H2, I2, \
A3, B3, C3, D3, E3, F3, G3, H3, I3, \
A4, B4, C4, D4, E4, F4, G4, H4, I4, \
A5, B5, C5, D5, E5, F5, G5, H5, I5, \
A6, B6, C6, D6, E6, F6, G6, H6, I6, \
A7, B7, C7, D7, E7, F7, G7, H7, I7, \
A8, B8, C8, D8, E8, F8, G8, H8, I8, \
A9, B9, C9, D9, E9, F9, G9, H9, I9, \
A10, B10, C10, D10, E10, F10, G10, H10, I10, \
    = MAP.flatten()


class Config(ConfigBase):
    # ===== Start of generated config =====
    MAP_SIREN_TEMPLATE = ['AmagiMasked']
    MOVABLE_ENEMY_TURN = (2,)
    MAP_HAS_SIREN = True
    MAP_HAS_MOVABLE_ENEMY = True
    MAP_HAS_MAP_STORY = False
    MAP_HAS_FLEET_STEP = True
    MAP_HAS_AMBUSH = False
    MAP_HAS_MYSTERY = False
    # ===== End of generated config =====

    MAP_ENSURE_EDGE_INSIGHT_CORNER = 'bottom'
    MAP_SWIPE_MULTIPLY = (1.325, 1.349)
    MAP_SWIPE_MULTIPLY_MINITOUCH = (1.281, 1.305)
    MAP_SWIPE_MULTIPLY_MAATOUCH = (1.244, 1.266)


class Campaign(CampaignBase):
    MAP = MAP
    ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'

    def battle_0(self):
        if self.clear_siren():
            return True
        if self.clear_filter_enemy(self.ENEMY_FILTER, preserve=0):
            return True

        return self.battle_default()

    def battle_5(self):
        return self.fleet_boss.clear_boss()