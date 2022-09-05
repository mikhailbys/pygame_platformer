from src.camera import Camera, camera_configure
from src.sprites.blocks import PLATFORM_WIDTH, PLATFORM_HEIGHT


def init_camera(level):
    # init camera
    total_level_width = len(level[0]) * PLATFORM_WIDTH  # level fact width
    total_level_height = len(level) * PLATFORM_HEIGHT  # level fact height
    camera = Camera(camera_configure, total_level_width, total_level_height)
    return camera
