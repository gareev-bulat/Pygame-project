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
        self.vol = 0.3
        pg.mixer.music.load('menuMusicNeedToChange.mp3')
        pg.mixer.music.play(-5, 7.3, 10)
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(self.vol)
        self.jump_sound = [pg.mixer.Sound('jump_sound_1.mp3'), pg.mixer.Sound('jump_sound_2.mp3'), pg.mixer.Sound('jump_sound_3.mp3')]
        for sound in self.jump_sound:
            sound.set_volume(0.2)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        self.map = TiledMap('map.tmx')
        self.map_image = self.map.make_map()
        self.map_rect = self.map_image.get_rect()

    def update_all(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                    self.quit()
                if event.key == pg.K_MINUS:
                    if self.vol != 0:
                        self.vol = self.vol - 0.1
                        pg.mixer.music.set_volume(self.vol)
                if event.key == pg.K_EQUALS:
                    if self.vol <= 2:
                        self.vol = self.vol + 0.1
                        pg.mixer.music.set_volume(self.vol)

    def draw(self):
        self.screen.fill(BLACK)

        self.screen.blit(self.map_image, self.camera.apply_rect_for_map(self.map_rect))

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.set_caption('{}'.format(round(self.clock.get_fps(), 2)))
        pg.display.flip()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player = pg.sprite.Group()
        # for row, tiles in enumerate(self.map.data):
        #     for col, tile in enumerate(tiles):
        #         if tile == '1':
        #             Wall(self, col, row)
        #         if tile == 'P':
        #             self.player = Player(self, col, row)

        for object in self.map.tmx.objects:
            if object.name == 'player':
                self.player = Player(self, object.x, object.y)
            if object.name == 'wall':
                Wall(self, object.x, object.y, object.width, object.height)
            if object.name == 'ladder':
                Ladder(self, object.x, object.y)

        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.dt = self.clock.tick(FPS) / 1000
        self.events()
        self.update_all()
        self.draw()

    def quit(self):
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    game = Game()
    running = True
    game.new()
    while running:
        game.run()