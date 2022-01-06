import pygame as pg
from settings import *


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



class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.make_jump = False
        self.vniz = False
        self.jump_counter = 50
        self.x = x
        self.y = y

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        # if keys[pg.K_UP] or keys[pg.K_w]:
        #     self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        if keys[pg.K_SPACE] and self.make_jump is False:
            self.make_jump = True
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
        if len(hits_with_walls) != 0:
            self.collide_with_walls('x')
            self.collide_with_walls('y')
            self.jump_counter = 50
            self.make_jump = False

    def collide_with_walls(self, direction):
        if direction == 'x':
            hits_with_walls = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits_with_walls:
                if self.vx < 0:
                    self.x = hits_with_walls[0].rect.right
                if self.vx > 0:
                    self.x = hits_with_walls[0].rect.left - self.rect.width
                self.vx = 0
                self.rect.x = self.x
        if direction == 'y':
            hits_with_walls = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits_with_walls:
                if self.vy < 0 or self.jump_counter >= 0:
                    self.y = hits_with_walls[0].rect.bottom
                if self.vy > 0 or self.jump_counter <= 0:
                    self.y = hits_with_walls[0].rect.top - self.rect.height
                self.vy = 0
                self.rect.y = self.y

    def update(self):
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
