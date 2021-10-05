import pygame

pygame.init()

window = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Wumpus World")
pygame.display.set_icon(pygame.image.load('./res/wumpus.png'))

player_image = pygame.image.load('./res/player_facing_to_down.png')
player_x = 0
player_y = 0
player_change = 0


def player(x, y):
    window.blit(player_image, (x, y))


def on_right_key_pressed():
    global player_x, player_image
    player_image = pygame.image.load("./res/player_facing_to_right.png")
    player_x += 80
    print("Right")


def on_left_key_pressed():
    global player_x, player_image
    player_image = pygame.image.load("./res/player_facing_to_left.png")
    player_x -= 80
    print("Left")


def on_up_key_pressed():
    global player_y, player_image
    player_image = pygame.image.load("./res/player_facing_to_up.png")
    player_y -= 80
    print("Up")


def on_down_key_pressed():
    global player_y, player_image
    player_image = pygame.image.load("./res/player_facing_to_down.png")
    player_y += 80
    print("Down")


running = True
while running:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                on_left_key_pressed()
            elif event.key == pygame.K_RIGHT:
                on_right_key_pressed()
            elif event.key == pygame.K_UP:
                on_up_key_pressed()
            elif event.key == pygame.K_DOWN:
                on_down_key_pressed()
    player(player_x, player_y)
    pygame.display.update()
