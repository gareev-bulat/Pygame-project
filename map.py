import pytmx
import pygame as pg
from settings import *
from settings import *


class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'r') as file:
            for line in file:
                self.data.append(line.strip())

        self.width = len(self.data[0]) * TILESIZE
        self.height = len(self.data) * TILESIZE


class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, target):
        return target.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + WIDTH // 2
        y = -target.rect.y + HEIGHT // 2

        # limit to map
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - WIDTH), x)
        y = max(-(self.height - HEIGHT), y)
        self.camera = pg.Rect(x, y, self.width, self.height)