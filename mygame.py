import pygame
import constants as con
import random as rand
import sys


class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.running = True
        self.player = Player()
        self.tiles = self.player.tiles

        self.window = pygame.display
        self.window.set_caption(con.CAPTION)
        self.window.set_icon(pygame.image.load(con.WUMPUS_ICON))

        self.surface = self.window.set_mode((self.tiles.width, self.tiles.height))
        for i in range(10):
            print(self.tiles.obstacle[i])

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.on_left_key_pressed()
                elif event.key == pygame.K_RIGHT:
                    self.player.on_right_key_pressed()
                elif event.key == pygame.K_UP:
                    self.player.on_up_key_pressed()
                elif event.key == pygame.K_DOWN:
                    self.player.on_down_key_pressed()
                # print(">>>>>>>>>>>>>>>>>>>>>>>>")
                # for i in range(10):
                #     print(self.tiles.tiles_con[i])

    def run(self):
        while self.running:
            self.event()

            self.surface.fill(con.BLACK)
            self.tiles.background(self.surface)
            self.tiles.grid(self.surface)
            self.tiles.text_view(self.surface)
            self.player.draw_player(self.surface)

            self.window.update()
            self.clock.tick(10)


class Player:
    def __init__(self):
        self.tiles = Tiles()

        self.player_image = pygame.image.load(con.PLAYER_DOWN)
        self.position = [0, 0]
        self.player_change = 0

    def draw_player(self, surface):
        surface.blit(self.player_image, (self.position[0], self.position[1]))

    def tile_state_change(self, value):
        x = value[0] // self.tiles.tiles_size
        y = value[1] // self.tiles.tiles_size
        if self.tiles.tiles_con[x][y] == 'h':
            self.tiles.tiles_con[x][y] = 'v'
        if self.tiles.obstacle[x][y] == 'p':
            print(".......YOU ARE DEAD.......\n.......FELL INTO PIT.......")
            sys.exit()
        elif self.tiles.obstacle[x][y] == 'w':
            print(".......YOU ARE DEAD.......\n.......EATEN BY WUMPUS.......")
            sys.exit()

    def on_right_key_pressed(self):
        self.player_image = pygame.image.load(con.PLAYER_RIGHT)
        if (self.position[0] + self.tiles.tiles_size) < self.tiles.width:
            self.position[0] += self.tiles.tiles_size
            self.tile_state_change(self.position)

    def on_left_key_pressed(self):
        self.player_image = pygame.image.load(con.PLAYER_LEFT)
        if (self.position[0] - self.tiles.tiles_size) >= 0:
            self.position[0] -= self.tiles.tiles_size
            self.tile_state_change(self.position)

    def on_up_key_pressed(self):
        self.player_image = pygame.image.load(con.PLAYER_UP)
        if (self.position[1] - self.tiles.tiles_size) >= 0:
            self.position[1] -= self.tiles.tiles_size
            self.tile_state_change(self.position)

    def on_down_key_pressed(self):
        self.player_image = pygame.image.load(con.PLAYER_DOWN)
        if (self.position[1] + self.tiles.tiles_size) < self.tiles.height:
            self.position[1] += self.tiles.tiles_size
            self.tile_state_change(self.position)


class Tiles:
    def __init__(self):
        self.tiles_row_count = 10
        self.tiles_col_count = 10
        self.tiles_size = 64

        self.height = self.tiles_size * self.tiles_row_count
        self.width = self.tiles_size * self.tiles_col_count

        self.wumpus_count = 10
        self.pit_count = 4
        self.gold_count = 5

        self.visible_floor = pygame.image.load(con.VISIBLE_FLOOR)
        self.hidden_floor = pygame.image.load(con.HIDDEN_FLOOR)
        self.wumpus = pygame.image.load(con.WUMPUS)
        self.pit = pygame.image.load(con.PIT)
        self.gold = pygame.image.load(con.GOLD)

        self.tiles_con = self.define_con()
        self.obstacle = self.define_obstacle()
        self.set_obstacle()

    def define_con(self):
        tiles_con = []
        for i in range(self.tiles_col_count):
            temp = []
            for j in range(self.tiles_row_count):
                temp.append('h')
            tiles_con.append(temp)
        tiles_con[0][0] = 'v'
        return tiles_con

    def define_obstacle(self):
        obstacle = []
        for i in range(self.tiles_col_count):
            temp = []
            for j in range(self.tiles_row_count):
                temp.append('n')
            obstacle.append(temp)
        return obstacle

    def set_obstacle(self):
        self.set_value(self.wumpus_count, "w")
        self.set_value(self.gold_count, "g")
        self.set_value(self.pit_count, "p")

    def set_value(self, count, cls):
        for i in range(count):
            x = rand.randint(1, 9)
            y = rand.randint(1, 9)
            self.obstacle[x][y] = cls

    def text_view(self, surface):
        font = pygame.font.SysFont('timesnewroman', 10)
        breeze = font.render("BREEZE", False, con.BLACK, con.WHITE)
        stench = font.render("STENCH", False, con.BLACK, con.WHITE)

        for i in range(self.tiles_col_count):
            for j in range(self.tiles_row_count):
                # if self.tiles_con[i][j] == 'h':
                #     continue
                # elif self.tiles_con[i][j] == 'v':
                if self.obstacle[i][j] == 'p':
                    self.set_breeze(breeze, i, j, surface)
                if self.obstacle[i][j] == 'w':
                    self.set_stench(stench, i, j, surface)

    def set_breeze(self, text, i, j, surface):
        if i + 1 < self.tiles_col_count:
            surface.blit(text, ((i + 1) * self.tiles_size, j * self.tiles_size))
        if i - 1 >= 0:
            surface.blit(text, ((i - 1) * self.tiles_size, j * self.tiles_size))
        if j + 1 < self.tiles_row_count:
            surface.blit(text, (i * self.tiles_size, (j + 1) * self.tiles_size))
        if j - 1 >= 0:
            surface.blit(text, (i * self.tiles_size, (j - 1) * self.tiles_size))

    def set_stench(self, text, i, j, surface):
        if i + 1 < self.tiles_col_count:
            surface.blit(text, ((i + 1) * self.tiles_size, j * self.tiles_size + 52))
        if i - 1 >= 0:
            surface.blit(text, ((i - 1) * self.tiles_size, j * self.tiles_size + 52))
        if j + 1 < self.tiles_row_count:
            surface.blit(text, (i * self.tiles_size, (j + 1) * self.tiles_size + 52))
        if j - 1 >= 0:
            surface.blit(text, (i * self.tiles_size, (j - 1) * self.tiles_size + 52))

    def grid(self, surface):
        for i in range(self.tiles_row_count):
            pygame.draw.line(surface, con.WHITE, (0, i * self.tiles_size), (self.width, i * self.tiles_size))
        pygame.draw.line(surface, con.WHITE, (0, self.height - 1), (self.width, self.height - 1))

        for i in range(self.tiles_col_count):
            pygame.draw.line(surface, con.WHITE, (i * self.tiles_size, 0), (i * self.tiles_size, self.height))
        pygame.draw.line(surface, con.WHITE, (self.width - 1, 0), (self.width - 1, self.height))

    def background(self, surface):
        for i in range(self.tiles_col_count):
            for j in range(self.tiles_row_count):
                if self.tiles_con[i][j] == 'h':
                    surface.blit(self.hidden_floor, (i * self.tiles_size, j * self.tiles_size))
                    continue
                elif self.tiles_con[i][j] == 'v':
                    surface.blit(self.visible_floor, (i * self.tiles_size, j * self.tiles_size))
                if self.obstacle[i][j] == 'p':
                    surface.blit(self.pit, (i * self.tiles_size, j * self.tiles_size))
                elif self.obstacle[i][j] == 'w':
                    surface.blit(self.wumpus, (i * self.tiles_size, j * self.tiles_size))
                elif self.obstacle[i][j] == 'g':
                    surface.blit(self.gold, (i * self.tiles_size, j * self.tiles_size))


if __name__ == "__main__":
    game = Game()
    game.run()
