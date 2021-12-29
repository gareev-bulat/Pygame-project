import pygame as pg
import os, sys
from settings import *
from sprites import *
from map import *


def load_image(name, colorkey=None):

    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        self.map = TiledMap('map.tmx')
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.houses = pg.sprite.Group()

    def run(self):
        self.dt = self.clock.tick(FPS) / 1000
        self.events()
        self.update_all()
        self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update_all(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw(self):
        pg.display.set_caption('{}'.format(round(self.clock.get_fps(), 2)))
        self.screen.blit(self.map_img, (120, 100))
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                    self.quit()


if __name__ == '__main__':
    game = Game()
    running = True
    while running:
        game.new()
        game.run()