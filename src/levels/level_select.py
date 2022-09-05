from src.levels.level_1 import level_1_modules
from src.levels.level_2 import level_2_modules

level_dict = {
    1: level_1_modules,
    2: level_2_modules,
}


def get_level(level_num):
    return level_dict[level_num]
