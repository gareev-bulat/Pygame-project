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
    for layer in gameMap.visible_layers:
        for x, y, gid, in layer:
            tile = gameMap.get_tile_image_by_gid(gid)
            if (tile != None):
                screen.blit(tile, (64 + x * 10 - y * 10, 32 + x * 5 + y * 5))
                #screen.blit(tile, (x * gameMap.tilewidth / 2, y * gameMap.tileheight / 2))



if __name__ == '__main__':
    pygame.init()
    width, height =  800, 800
    size = width, height
    screen = pygame.display.set_mode(size)
    gameMap = load_pygame("map.tmx")
    pygame.display.set_caption('')
    load_map()
    all_sprites = pygame.sprite.Group()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
