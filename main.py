import pygame
import constants as con

pygame.init()

pygame.display.set_caption("Wumpus World")
pygame.display.set_icon(pygame.image.load('./res/wumpus.png'))

player_image = pygame.image.load('./res/player_facing_to_down.png')
player_x = 8
player_y = 8
player_change = 0
tiles_row_count = 10
tiles_col_count = 10
tiles_size = 80
height = tiles_size*tiles_row_count
width = tiles_size*tiles_col_count
running = True
window = pygame.display.set_mode((tiles_col_count*tiles_size, tiles_row_count*tiles_size))


def player(x, y):
    window.blit(player_image, (x, y))


def on_right_key_pressed():
    global player_x, player_image
    player_image = pygame.image.load("./res/player_facing_to_right.png")
    if (player_x + tiles_size) <= width:
        player_x += tiles_size
    print("Right")


def on_left_key_pressed():
    global player_x, player_image
    player_image = pygame.image.load("./res/player_facing_to_left.png")
    if (player_x - tiles_size) >= 0:
        player_x -= tiles_size
    print("Left")


def on_up_key_pressed():
    global player_y, player_image
    player_image = pygame.image.load("./res/player_facing_to_up.png")
    if (player_y - tiles_size) >= 0:
        player_y -= tiles_size
    print("Up")


def on_down_key_pressed():
    global player_y, player_image
    player_image = pygame.image.load("./res/player_facing_to_down.png")
    if (player_y + tiles_size) <= height:
        player_y += tiles_size
    print("Down")


def grid_view():
    for i in range(tiles_row_count):
        pygame.draw.line(window, con.WHITE, (0, i * tiles_size), (width, i * tiles_size))
    pygame.draw.line(window, con.WHITE, (0, height-1), (width, height-1))

    for i in range(tiles_col_count):
        pygame.draw.line(window, con.WHITE, (i * tiles_size, 0), (i * tiles_size, height))
    pygame.draw.line(window, con.WHITE, (width-1, 0), (width-1, height))


def backgroud_view():
    pass


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
    backgroud_view()
    grid_view()
    player(player_x, player_y)
    pygame.display.update()
