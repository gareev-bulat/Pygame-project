import pygame, os, sys
from pytmx import load_pygame


def load_image(name, colorkey=None):

    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def load_map():
    print(gameMap)



if __name__ == '__main__':
    pygame.init()
    width, height =  500, 500
    size = width, height
    gameMap = load_pygame("map.tmx")
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('')
    load_map()
    all_sprites = pygame.sprite.Group()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
