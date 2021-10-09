import pygame
import constants as con


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

    def run(self):
        while self.running:
            self.event()

            self.surface.fill(con.BLACK)
            self.tiles.background(self.surface)
            self.tiles.grid(self.surface)
            self.player.draw_player(self.surface)

            self.window.update()
            self.clock.tick(30)


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

    def on_right_key_pressed(self):
        self.player_image = pygame.image.load(con.PLAYER_RIGHT)
        if (self.position[0] + self.tiles.tiles_size) <= self.tiles.width:
            self.position[0] += self.tiles.tiles_size
            self.tile_state_change(self.position)
        print("Right")

    def on_left_key_pressed(self):
        self.player_image = pygame.image.load(con.PLAYER_LEFT)
        if (self.position[0] - self.tiles.tiles_size) >= 0:
            self.position[0] -= self.tiles.tiles_size
            self.tile_state_change(self.position)
        print("Left")

    def on_up_key_pressed(self):
        self.player_image = pygame.image.load(con.PLAYER_UP)
        if (self.position[1] - self.tiles.tiles_size) >= 0:
            self.position[1] -= self.tiles.tiles_size
            self.tile_state_change(self.position)
        print("Up")

    def on_down_key_pressed(self):
        self.player_image = pygame.image.load(con.PLAYER_DOWN)
        if (self.position[1] + self.tiles.tiles_size) <= self.tiles.height:
            self.position[1] += self.tiles.tiles_size
            self.tile_state_change(self.position)
        print("Down")


class Tiles:
    def __init__(self):
        self.tiles_row_count = 10
        self.tiles_col_count = 10
        self.tiles_size = 64
        self.height = self.tiles_size * self.tiles_row_count
        self.width = self.tiles_size * self.tiles_col_count
        self.visible_floor = pygame.image.load(con.VISIBLE_FLOOR)
        self.hidden_floor = pygame.image.load(con.HIDDEN_FLOOR)

        self.tiles_con = []
        self.define_con(self.tiles_con)

    def define_con(self, tiles_con):
        for i in range(self.tiles_col_count):
            temp = []
            for j in range(self.tiles_row_count):
                temp.append('h')
            tiles_con.append(temp)
        self.tiles_con[0][0] = 'v'

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
                elif self.tiles_con[i][j] == 'v':
                    surface.blit(self.visible_floor, (i * self.tiles_size, j * self.tiles_size))


if __name__ == "__main__":
    game = Game()
    game.run()
