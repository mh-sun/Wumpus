import pygame

pygame.init()

screen = pygame.display
screen_mode = screen.set_mode((800, 600))

screen.set_caption("Wumpus World")
screen.set_icon(pygame.image.load('./res/wumpus.png'))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen_mode.fill((255, 255, 255))
    screen.update()