import os
from pygame import image, font

from scripts.core.tilemap import TileMap

font.init()

IMG_PATH = 'data/images/'
MAP_PATH = 'data/maps/'
MUSIC_PATH = 'data/musics/'
SFX_PATH = 'data/sfx/'

DEBUG_FONT = font.SysFont('Arial', 24)
WINNER_FONT = font.SysFont('Arial', 64)

def show_text(surface, value, pos=(0, 0), color=(0, 0, 0), center=False, font=DEBUG_FONT):
    text_surface = font.render(value, True, color)
    if center:
        width = text_surface.get_width()
        height = text_surface.get_height()
        surface.blit(text_surface, (pos[0] - width // 2, pos[1] - height // 2))
    else:
        surface.blit(text_surface, pos)


def load_image(path):
    img = image.load(IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    imgs = []
    for img_name in sorted(os.listdir(IMG_PATH + path)):
        imgs.append(load_image(path + "/" + img_name))
    return imgs

def load_map(game, path):
    tilemap = TileMap(game)
    tilemap.load(MAP_PATH + '/' + path)
    return tilemap

def load_maps(game):
    maps = []
    for map_name in sorted(os.listdir(MAP_PATH)):
        maps.append(load_map(game, map_name))
    return maps

def play_sfx(sfx):
    sfx.stop()
    sfx.play()

def add_points(point1, point2, sub=False):
    """ Calculate a position with or without an offset """
    if not sub:
        return point1[0] + point2[0], point1[1] + point2[1]
    return point1[0] - point2[0], point1[1] - point2[1]

def point_to_int(point):
    """ Convert position to int position"""
    return [int(point[0]), int(point[1])]
