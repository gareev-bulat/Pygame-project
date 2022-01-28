import pytmx
import pygame as pg
from settings import *
from settings import *

# игровое поле
class TiledMap:
    def __init__(self, filename):
        self.tmx = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = self.tmx.width * self.tmx.tilewidth
        self.height = self.tmx.height * self.tmx.tileheight

    def render(self, surface):
        for layer in self.tmx.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = self.tmx.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmx.tilewidth,
                                            y * self.tmx.tileheight))

    def make_map(self):
        surface = pg.Surface((self.width, self.height))
        self.render(surface)
        return surface


# камера
class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, target):
        return target.rect.move(self.camera.topleft)

    def apply_rect_for_map(self, target):
        return target.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + WIDTH // 2
        y = -target.rect.y + HEIGHT // 2

        # limit to map
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - WIDTH), x)
        y = max(-(self.height - HEIGHT), y)
        self.camera = pg.Rect(x, y, self.width, self.height)