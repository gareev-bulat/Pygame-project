import pygame as pg
import settings
from random import choice
import os, sys


# class Wall(pg.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self.groups = game.all_sprites, game.walls
#         pg.sprite.Sprite.__init__(self, self.groups)
#         self.game = game
#         self.image = pg.Surface((TILESIZE, TILESIZE))
#         self.image.fill(GREEN)
#         self.rect = self.image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.x = x * TILESIZE
#         self.rect.y = y * TILESIZE


def load_image(name, colorkey=None):
    fullname = name
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


def cut_sheet(sheet, columns, rows, frames):
    rect = pg.Rect(0, 0, sheet.get_width() // columns,
                        sheet.get_height() // rows)
    for j in range(rows):
        for i in range(columns):
            frame_location = (rect.w * i, rect.h * j)
            frames.append(pg.transform.scale(sheet.subsurface(pg.Rect(
                frame_location, rect.size)), (64, 64)))


class Enemies(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.mixer.init()
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.clock = pg.time.Clock()
        self.frames = []
        self.first_count = 0
        self.second_count = 0
        cut_sheet(load_image("testPersonRight.png"), 4, 1, self.frames)
        cut_sheet(load_image("testPersonLeft.png"), 4, 1, self.frames)
        self.image = self.frames[4]
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.make_jump = False
        self.vniz = False
        self.onLadder = False
        self.jump_counter = 50
        self.levitating = 0
        self.x = x
        self.y = y


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.mixer.init()
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.money_music = pg.mixer.Sound('picking a coin.mp3')
        self.player_damage_music = pg.mixer.Sound('hit_player.mp3')
        self.money_music.set_volume(1.0)
        self.game = game
        self.clock = pg.time.Clock()
        self.frames = []
        self.first_count = 0
        self.second_count = 0
        cut_sheet(load_image("testPersonRight.png"), 4, 1, self.frames)
        cut_sheet(load_image("testPersonLeft.png"), 4, 1, self.frames)
        self.image = self.frames[4]
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.make_jump = False
        self.vniz = False
        self.onLadder = False
        self.jump_counter = 50
        self.levitating = 0
        self.x = x
        self.y = y


    def get_keys(self):
        hits_with_ladders = pg.sprite.spritecollide(self, self.game.ladders, False)
        hits_with_money = pg.sprite.spritecollide(self, self.game.money, False)
        hits_with_shipp = pg.sprite.spritecollide(self, self.game.shipp, False)
        if len(hits_with_money) == 1:
            hits_with_money[0].kill()
            settings.MONEY_COUNTER += 1
            self.sounds('coin')
        if len(hits_with_ladders) != 0:
            self.onLadder = True
        else:
            self.onLadder = False
        if len(hits_with_shipp) == 1 and settings.ATTACK:
            settings.HEALTH -= settings.ENEMIES_DAMAGE['shipp']
            settings.ATTACK = False
            self.sounds('damage_to_player')
        elif len(hits_with_shipp) == 0:
            settings.ATTACK = True
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        mods = pg.key.get_mods()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            if self.make_jump:
                self.image = self.frames[4]
            if not self.make_jump:
                self.first_count = round(self.first_count + 0.25, 2)
                if int(self.first_count) == self.first_count:
                    self.image = self.frames[4:8][int(self.first_count) % 4]
            self.vx = -settings.PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            if self.make_jump:
                self.image = self.frames[0]
            self.vx = settings.PLAYER_SPEED
            if not self.make_jump:
                self.second_count = round(self.second_count + 0.25, 3)
                if int(self.second_count) == self.second_count:
                    self.image = self.frames[:4][int(self.second_count) % 4]
        if keys[pg.K_UP] or keys[pg.K_w]:
            if self.onLadder:
                self.y = self.y - 10
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = settings.PLAYER_SPEED
        if mods & pg.KMOD_SHIFT and (keys[pg.K_LEFT] or keys[pg.K_a]):
            self.vx = -settings.PLAYER_SPEED - 150
        if mods & pg.KMOD_SHIFT and (keys[pg.K_RIGHT] or keys[pg.K_d]):
            self.vx = settings.PLAYER_SPEED + 150
        if (keys[pg.K_SPACE] or keys[pg.K_UP]) and self.make_jump is False:
            self.make_jump = True
            choice(self.game.jump_sound).play()
        if self.vx != 0 and self.vy != 0:
            self.vx = self.vx // 1.5
            self.vy = self.vy // 1.5

    def jump(self):
        hits_with_walls = pg.sprite.spritecollide(self, self.game.walls, False)
        if self.jump_counter >= -50:
            self.y = self.y - self.jump_counter / 2.5
            self.jump_counter -= 1
        else:
            self.jump_counter = 50
            self.make_jump = False
        # if len(hits_with_walls) != 0:
        #     self.collide_with_walls('x')
        #     self.collide_with_walls('y')
        #     self.jump_counter = 50
        #     self.make_jump = False

    def collide_with_walls(self, direction):
        hits_with_walls = pg.sprite.spritecollide(self, self.game.walls, False)

        try:
            if self.rect.bottom - 1 == hits_with_walls[0].rect.top or self.rect.bottom - 10 == hits_with_walls[0].rect.top:
                self.make_jump = False
                self.jump_counter = 50
        except IndexError:
            pass

        if direction == 'x':
            if hits_with_walls:
                if self.vx < 0:
                    self.x = hits_with_walls[0].rect.right
                if self.vx > 0:
                    self.x = hits_with_walls[0].rect.left - self.rect.width
                self.vx = 0
                self.rect.x = self.x
        if direction == 'y':
            if hits_with_walls:
                if self.vy < 0 or self.jump_counter >= 0:
                    self.y = hits_with_walls[0].rect.bottom
                if self.vy > 0 or self.jump_counter <= 0:
                    self.y = hits_with_walls[0].rect.top - self.rect.height
                if self.vy == 0 and not self.make_jump and hits_with_walls[0].rect.top > self.rect.top:
                    self.y = hits_with_walls[0].rect.top - self.rect.height
                if (self.vy == 0 or self.vy > 0) and hits_with_walls[0].rect.top <= self.rect.top:
                    self.y = hits_with_walls[0].rect.bottom
                self.vy = 0
                self.levitating = 0
                self.rect.y = self.y
            else:
                self.levitating = 5

    def sounds(self, what):
        if what == 'coin':
            self.money_music.play()
        if what == 'damage_to_player':
            self.player_damage_music.play()

    def update(self):
        self.y = self.y + self.levitating
        self.get_keys()
        if self.make_jump:
            self.jump()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, x1, y1):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, x1, y1)
        # self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Ladder(pg.sprite.Sprite):
    def __init__(self, game, x, y, x1, y1):
        self.groups = game.ladders
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, x1, y1)
        # self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Money(pg.sprite.Sprite):
    def __init__(self, game, x, y, x1, y1):
        self.groups = game.money
        pg.sprite.Sprite.__init__(self, self.groups)
        image = load_image('money.png')
        self.image = pg.transform.scale(image, (32, 32))
        self.rect = pg.Rect(x, y, x1, y1)
        # self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y


class Shipp(pg.sprite.Sprite):
    def __init__(self, game, x, y, x1, y1):
        self.groups = game.shipp
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, x1, y1)
        # self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
