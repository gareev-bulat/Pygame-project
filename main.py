import pygame


if __name__ == '__main__':
    pygame.init()
    width, height =  1000, 700
    size = width, height
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('')
    all_sprites = pygame.sprite.Group()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()