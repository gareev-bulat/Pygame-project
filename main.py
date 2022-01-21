import pygame as pg
import os, sys
from settings import *
from sprites import *
from map import *
import sqlite3
import random

pg.font.init()

def load_image(name, colorkey=None):
    fullname = name
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден!")
        sys.exit()
    image = pg.image.load(fullname)
    return image

class Shop:

    def __init__(self):
        pg.mixer.init()
        self.vol = 0.15
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.buttons = [load_image('level_1.png'),
                        load_image('level_2.png')]
        self.buttons_coords= {'level1': (10, 10),
                              'level2': (64, 10)}
        self.click_up_sound = pg.mixer.Sound("Menu/click_up.mp3")
        self.click_down_sound = pg.mixer.Sound("Menu/click_down.mp3")
        self.map_name = ''


    def terminate(self):
        pg.quit()
        sys.exit()

    def check_pos(self, pos):
        x, y = pos[0], pos[1]
        if 20 <= x <= 49 and 20 <= y <= 72:
            return 'level_1'
        if 76 <= x <= 112 and 20 <= y <= 72:
            return 'level_2'
        return False

    def click_button_music(self, state):
        if state == 'up':
            self.click_up_sound.set_volume(0.15)
            self.click_up_sound.play()
        elif state == 'down':
            self.click_down_sound.set_volume(0.15)
            self.click_down_sound.play()

    def choice_menu(self):

        fon = pg.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))
        level_1 = self.buttons[0]
        level_2 = self.buttons[1]
        self.screen.blit(level_1, self.buttons_coords['level1'])
        self.screen.blit(level_2, self.buttons_coords['level2'])

        while True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_MINUS:
                        if self.vol != 0:
                            self.vol = self.vol - 0.1
                            pg.mixer.music.set_volume(self.vol)
                    if event.key == pg.K_EQUALS:
                        if self.vol <= 2:
                            self.vol = self.vol + 0.1
                            pg.mixer.music.set_volume(self.vol)
                if event.type == pg.QUIT:
                    self.terminate()
                elif (event.type == pg.KEYUP or event.type == pg.MOUSEBUTTONUP):
                    self.click_button_music('up')
                    if self.check_pos(pg.mouse.get_pos()) == 'level_1':
                        self.map_name = 'map.tmx'
                    elif self.check_pos(pg.mouse.get_pos()) == 'level_2':
                        self.map_name = 'map2.tmx'
                    if self.map_name != '':
                        self.start_game()
                elif (event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN):
                    self.click_button_music('down')
            pg.display.flip()
            self.clock.tick(FPS)

    def start_game(self):
        game = Game(self.map_name)
        running = True
        game.new()
        while running:
            game.run()

class Options:

    def __init__(self, screen):
        self.screen = screen
        self.screen2 = pg.Surface((OPTIONS_WIDTH, OPTIONS_HEIGHT))

    def surface(self):
        fon = pg.transform.scale(load_image('Menu/options_fon.jpg'), (OPTIONS_WIDTH, OPTIONS_HEIGHT))
        self.screen2.blit(fon, (0, 0))
        self.event()

    def event(self):
        self.screen.blit(self.screen2, (WIDTH / 2 - OPTIONS_WIDTH / 2, HEIGHT / 2 - OPTIONS_HEIGHT / 2))

class Levels:
    def __init__(self):
        pg.mixer.init()
        self.vol = 0.15
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.buttons = [load_image('level_1.png'),
                        load_image('level_2.png')]
        self.buttons_coords= {'level1': (10, 10),
                              'level2': (64, 10)}
        self.click_up_sound = pg.mixer.Sound("Menu/click_up.mp3")
        self.click_down_sound = pg.mixer.Sound("Menu/click_down.mp3")
        self.map_name = ''


    def terminate(self):
        pg.quit()
        sys.exit()

    def check_pos(self, pos):
        x, y = pos[0], pos[1]
        if 20 <= x <= 49 and 20 <= y <= 72:
            return 'level_1'
        if 76 <= x <= 112 and 20 <= y <= 72:
            return 'level_2'
        return False

    def click_button_music(self, state):
        if state == 'up':
            self.click_up_sound.set_volume(0.15)
            self.click_up_sound.play()
        elif state == 'down':
            self.click_down_sound.set_volume(0.15)
            self.click_down_sound.play()

    def choice_menu(self):

        fon = pg.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))
        level_1 = self.buttons[0]
        level_2 = self.buttons[1]
        self.screen.blit(level_1, self.buttons_coords['level1'])
        self.screen.blit(level_2, self.buttons_coords['level2'])

        while True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_MINUS:
                        if self.vol != 0:
                            self.vol = self.vol - 0.1
                            pg.mixer.music.set_volume(self.vol)
                    if event.key == pg.K_EQUALS:
                        if self.vol <= 2:
                            self.vol = self.vol + 0.1
                            pg.mixer.music.set_volume(self.vol)
                if event.type == pg.QUIT:
                    self.terminate()
                elif (event.type == pg.KEYUP or event.type == pg.MOUSEBUTTONUP):
                    self.click_button_music('up')
                    if self.check_pos(pg.mouse.get_pos()) == 'level_1':
                        self.map_name = 'map.tmx'
                    elif self.check_pos(pg.mouse.get_pos()) == 'level_2':
                        self.map_name = 'map2.tmx'
                    if self.map_name != '':
                        self.start_game()
                elif (event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN):
                    self.click_button_music('down')
            pg.display.flip()
            self.clock.tick(FPS)

    def start_game(self):
        game = Game(self.map_name)
        running = True
        game.new()
        while running:
            game.run()

class Menu:

    def __init__(self):
        pg.mixer.init()
        self.vol = 0.15
        pg.mixer.music.load('Menu/menu_music.mp3')
        pg.mixer.music.play(-5, 7.3, 10)
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(self.vol)
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.buttons = [load_image('Menu/play.png'),
                        load_image('Menu/options.png'),
                        load_image('Menu/exit.png'),
                        load_image('Menu/shop.png')]
        self.buttons_sizes = {'play': (221, 100), 
                              'options': (326, 79), 
                              'exit': (204, 79),
                              'shop': (211, 100)}
        self.click_up_sound = pg.mixer.Sound("Menu/click_up.mp3")
        self.click_down_sound = pg.mixer.Sound("Menu/click_down.mp3")
        self.con = sqlite3.connect("database.db")
        self.text_font = pg.font.SysFont(settings.FONT, 35)


    def terminate(self):
        pg.quit()
        sys.exit()

    def check_pos(self, pos):
        x, y = pos[0], pos[1]
        print(x, y)
        if 409 <= x <= 609 and 298 <= y <= 344:
            return 'Play'
        elif 414 <= x <= 598 and 391 <= y <= 440:
            return 'Shop'
        elif 358 <= x <= 662 and 485 <= y <= 538:
            return 'Options'
        elif 414 <= x <= 600 and 574 <= y <= 629:
            return 'Exit'
        return False

    def click_button_music(self, state):
        if state == 'up':
            self.click_up_sound.set_volume(0.15)
            self.click_up_sound.play()
        elif state == 'down':
            self.click_down_sound.set_volume(0.15)
            self.click_down_sound.play()

    def start_screen(self):

        fon = pg.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))
        button_1 = self.buttons[0]
        button_2 = self.buttons[1]
        button_3 = self.buttons[2]
        button_4 = self.buttons[3]
        self.screen.blit(button_1, (WIDTH / 2 - (self.buttons_sizes['play'][0] // 2), HEIGHT / 2 - 100))
        self.screen.blit(button_2, (WIDTH / 2 - (self.buttons_sizes['options'][0] // 2), HEIGHT / 2 + 90))
        self.screen.blit(button_3, (WIDTH / 2 - (self.buttons_sizes['exit'][0] // 2), HEIGHT / 2 + 100 + 79))
        self.screen.blit(button_4, (WIDTH / 2 - (self.buttons_sizes['shop'][0] // 2 + 5), HEIGHT / 2 - 5))
        self.screen.blit(load_image('money.png'), (10, 10))
        text = self.work_with_base()
        print(text)
        menu_money_counter = self.text_font.render(text, True, settings.DARK_BLUE)
        self.screen.blit(menu_money_counter, (50, 5))


        while True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_MINUS:
                        if self.vol != 0:
                            self.vol = self.vol - 0.1
                            pg.mixer.music.set_volume(self.vol)
                    if event.key == pg.K_EQUALS:
                        if self.vol <= 2:
                            self.vol = self.vol + 0.1
                            pg.mixer.music.set_volume(self.vol)
                if event.type == pg.QUIT:
                    self.terminate()
                elif (event.type == pg.KEYUP or event.type == pg.MOUSEBUTTONUP):
                    self.click_button_music('up')
                    if self.check_pos(pg.mouse.get_pos()) == 'Play':
                        levels = Levels()
                        levels.choice_menu()
                    elif self.check_pos(pg.mouse.get_pos()) == 'Shop':
                        shop = Shop()
                        shop.choice_menu()
                    elif self.check_pos(pg.mouse.get_pos()) == 'Options':
                        options = Options(self.screen)
                        options.surface()
                    elif self.check_pos(pg.mouse.get_pos()) == 'Exit':
                        pg.quit()
                        sys.exit()
                elif (event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN):
                    self.click_button_music('down')
                    # начинаем игру
            pg.display.flip()
            self.clock.tick(FPS)

    def work_with_base(self):
        cur = self.con.cursor()
        result = cur.execute("""SELECT * FROM money_counter""").fetchall()
        return str(result[0][0])


class Game:
    def __init__(self, map_name):
        pg.init()
        self.vol = 0.15
        pg.mixer.music.load('menuMusicNeedToChange.mp3')
        pg.mixer.music.play(-5, 7.3, 10)
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(self.vol)
        self.jump_sound = [pg.mixer.Sound('jump_sound_1.mp3'), pg.mixer.Sound('jump_sound_2.mp3'), pg.mixer.Sound('jump_sound_3.mp3')]
        for sound in self.jump_sound:
            sound.set_volume(0.2)
        self.title = map_name
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.money_image = load_image('money.png')
        self.health_image = load_image('health_icon.png')
        self.text_font = pg.font.SysFont(settings.FONT, 35)
        self.clock = pg.time.Clock()
        self.flag = True
        self.con = sqlite3.connect("database.db")
        self.snow_list = []
        self.load_data()
        self.prepare_snow()

    def prepare_snow(self):
        for i in range(400):
            snow_x, snow_y = random.randint(0, WIDTH - 5), random.randint(-settings.HEIGHT, 20)
            self.snow_list.append([snow_x, snow_y, random.choice((0.3, 0.5))])

    def load_data(self):
        self.map = TiledMap(self.title)
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
        self.screen.blit(self.health_image, (170, 10))
        self.screen.blit(self.money_image, (900, 10))


        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.money:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.medthings:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.enemies:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        #for sprite in self.sword:
        #    self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.snow_animation()
        pg.display.set_caption('{}'.format(round(self.clock.get_fps(), 2)))
        self.screen_panels()
        pg.display.flip()

    def snow_animation(self):
        for i in range(len(self.snow_list)):
            if self.snow_list[i][1] >= settings.HEIGHT:
                self.snow_list[i][1] = random.randint(-settings.HEIGHT, 20)
            pg.draw.circle(self.screen, 'white', (self.snow_list[i][0], self.snow_list[i][1]), 2)
            self.snow_list[i][1] += self.snow_list[i][2]


    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.ladders = pg.sprite.Group()
        self.money = pg.sprite.Group()
        self.shipp = pg.sprite.Group()
        self.medthings = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.sword = pg.sprite.Group()
        # for row, tiles in enumerate(self.map.data):
        #     for col, tile in enumerate(tiles):
        #         if tile == '1':
        #             Wall(self, col, row)
        #         if tile == 'P':
        #             self.player = Player(self, col, row)



        for object in self.map.tmx.objects:
            if object.name == 'player':
                self.player = Player(self, object.x, object.y)
            elif object.name == 'enemy(bat)':
                self.enemy_bat = Enemies(self, object.x, object.y, 'bat')
            elif object.name == 'wall':
                Wall(self, object.x, object.y, object.width, object.height)
            elif object.name == 'ladder':
                Ladder(self, object.x, object.y, object.width, object.height)
            elif object.name == 'money':
                Money(self, object.x, object.y, object.width, object.height)
            elif object.name == 'shipp':
                Shipp(self, object.x, object.y, object.width, object.height)
            elif object.name == 'medkit':
                MedKit(self, object.x, object.y, object.width, object.height)
            elif object.name == 'bandage':
                Bandage(self, object.x, object.y, object.width, object.height)
            elif object.name == 'sword':
                Sword(self, object.x, object.y, object.width, object.height)


        self.camera = Camera(self.map.width, self.map.height)

    def screen_panels(self):
        if 60 <= (settings.HEALTH * 100) <= 100:
            self.color_of_health = GREEN
        elif 25 <= (settings.HEALTH * 100) < 60:
            self.color_of_health = YELLOW
        elif 0 <= (settings.HEALTH * 100) < 25:
            self.color_of_health = RED
        pg.draw.rect(self.screen, (255, 255, 255), (10, 10, 155, 40), 4)
        pg.draw.rect(self.screen, self.color_of_health, (13, 13, settings.HEALTH * 150, 35))
        text_money_counter = self.text_font.render(str(settings.MONEY_COUNTER) + "/20", True, settings.DARK_BLUE)
        if 0 <= settings.MONEY_COUNTER < 10:
            self.screen.blit(text_money_counter, (830, 6))
        elif 10 <= settings.MONEY_COUNTER < 99:
            self.screen.blit(text_money_counter, (810, 6))
        if settings.HEALTH <= 0:
            self.game_over()
        pg.display.flip()

    def game_over(self):
        Game_Over(self.screen).do()
        if self.flag:
            self.work_with_base()
            self.flag = False


    def work_with_base(self):
        cur = self.con.cursor()
        result = cur.execute("""SELECT * FROM money_counter""").fetchall()
        cur.execute('UPDATE money_counter SET update_money=?', [int(result[0][0]) + settings.MONEY_COUNTER])
        self.con.commit()

    def run(self):
        self.dt = self.clock.tick(FPS) / 1000
        self.events()
        self.update_all()
        self.draw()
        self.screen_panels()

    def quit(self):
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    menu = Menu()
    menu.start_screen()
