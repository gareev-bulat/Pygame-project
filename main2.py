import pygame, os, sys



print('brtrf')


def Player(x, y):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, 'green', (x, y, 20, 20))


def key():
    global player_x, player_y
    k = pygame.key.get_pressed()
    if k[pygame.K_RIGHT]:
        player_x += speed
    if k[pygame.K_LEFT]:
        player_x -= speed
    if k[pygame.K_UP]:
        player_y -= speed
    if k[pygame.K_DOWN]:
        player_y += speed
    check()

def check():
    global player_x, player_y
    if player_x < 0:
        player_x = width - 20
    elif player_x > width:
        player_x = 0
    if player_y < 0:
        player_y = height - 20
    elif player_y > height:
        player_y = 0



player_x, player_y, speed = 20, 10, 5

if __name__ == '__main__':
    fps = 300
    clock = pygame.time.Clock()
    pygame.init()
    width, height =  700, 500
    size = width, height
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('карлсон который живёт на крыше')
    all_sprites = pygame.sprite.Group()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key()
        Player(player_x, player_y)
        clock.tick(fps)
        pygame.display.flip()
