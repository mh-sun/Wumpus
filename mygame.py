import pygame
import constants as con
import player


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

        self.surface = self.window.set_mode((self.tiles.width + 200, self.tiles.height))

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
            self.method_name()

            self.player.think_bro_think()

            self.method_name1()

    def method_name1(self):
        self.window.update()
        self.clock.tick(1)

    def method_name(self):
        self.event()
        self.surface.fill(con.LIGHTGREY)
        self.tiles.background(self.surface)
        self.tiles.text_view(self.surface)

        print("WUMPUS PROB")
        for i in range(10):
            print(self.player.wumpus_prob[i])

        self.player.draw_player(self.surface)


if __name__ == "__main__":
    game = Game()
    game.run()
