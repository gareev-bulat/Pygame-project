import pygame as pg

WIDTH = 1024
HEIGHT = 768
OPTIONS_WIDTH, OPTIONS_HEIGHT = 400, 400
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 150)
PLAYER_SPEED = 350
FPS = 60
TITLE = "Go Around World!"
TILESIZE = 64
GRAVITY = 3
JUMP_COUNTER = 30
ATTACK = True
HEALTH = 0.1
MONEY_COUNTER = 0
FONT = 'serif'
ENEMIES_DAMAGE = {'shipp': 0.04}
PLAYER_DAMAGE = {'sword': 0.04}
active_weapon = 'sword'
active_skin = 'black'
LEVEL_LIST = ['map.tmx', 'map2.tmx']


