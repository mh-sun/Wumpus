import pygame
import constants as con
import player
import time

class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.running = True
        self.player = player.Player()
        self.tiles = self.player.tiles

        self.window = pygame.display
        self.window.set_caption(con.CAPTION)
        self.window.set_icon(pygame.image.load(con.WUMPUS_ICON))

        self.surface = self.window.set_mode((self.tiles.width, self.tiles.height))

        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        for i in range(10):
            print(self.tiles.obstacle[i])

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.on_left_key_pressed()
                    print(self.player.position)
                elif event.key == pygame.K_RIGHT:
                    self.player.on_right_key_pressed()
                    print(self.player.position)
                elif event.key == pygame.K_UP:
                    self.player.on_up_key_pressed()
                    print(self.player.position)
                elif event.key == pygame.K_DOWN:
                    self.player.on_down_key_pressed()
                    print(self.player.position)

    def run(self):
        while self.running:
            self.event()

            self.surface.fill(con.LIGHTGREY)
            self.tiles.background(self.surface)
            self.tiles.text_view(self.surface)
            self.player.draw_player(self.surface)

            self.player.think_bro_think()
            self.window.update()

            self.clock.tick(1)

if __name__ == "__main__":
    game = Game()
    game.run()
