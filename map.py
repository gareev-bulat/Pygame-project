import pytmx
import pygame as pg
from settings import *
vec = pg.math.Vector2


class TiledMap:
    def __init__(self, filename):
        tm_map = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm_map.width * tm_map.tilewidth
        self.height = tm_map.height * tm_map.tilewidth
        self.tmxdata = tm_map

    def render(self, surface):
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.tmxdata.get_tile_image_by_gid(gid)
                    if tile:
                        self.vel = vec(x * TILESIZE, y * TILESIZE)
                        surface.blit(tile, self.vel)

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface