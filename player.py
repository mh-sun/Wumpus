import pygame
import constants as con
import sys
import tiles
import time


class Player:
    def __init__(self):
        self.tiles = tiles.Tiles()
        self.player_image = pygame.image.load(con.PLAYER_DOWN)
        self.position = [0, 0]
        self.track = [[0, 0]]
        self.map = tiles.array_construct('u')
        self.map_probability = tiles.array_construct(0)
        self.sensor_op(self.position[0], self.position[1])

    def draw_player(self, surface):

        surface.blit(self.player_image, (self.position[1] * con.TILE_SIZE, self.position[0] * con.TILE_SIZE))

    def tile_state_change(self):
        x = self.position[0]
        y = self.position[1]
        if self.tiles.tiles_con[x][y] == 'h':
            self.tiles.tiles_con[x][y] = 'v'

        self.sensor_op(x, y)
        self.track.append([x, y])
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # for i in range(10):
        #     print(self.map[i])

        print("Player Position", end=" ")
        print(self.position)

        if self.tiles.obstacle[x][y] == 'p':
            print(".......YOU ARE DEAD.......\n.......FELL INTO PIT.......")
            time.sleep(30)
        elif self.tiles.obstacle[x][y] == 'w':
            print(".......YOU ARE DEAD.......\n.......EATEN BY WUMPUS.......")
            time.sleep(30)
        time.sleep(1)

    def on_right_key_pressed(self):
        self.player_image = pygame.image.load(con.PLAYER_RIGHT)
        if ((self.position[1] + 1) * con.TILE_SIZE) < self.tiles.width:
            self.position[1] += 1
            self.tile_state_change()

    def on_left_key_pressed(self):
        self.player_image = pygame.image.load(con.PLAYER_LEFT)
        if ((self.position[1] - 1) * con.TILE_SIZE) >= 0:
            self.position[1] -= 1
            self.tile_state_change()

    def on_up_key_pressed(self):
        self.player_image = pygame.image.load(con.PLAYER_UP)
        if ((self.position[0] - 1) * con.TILE_SIZE) >= 0:
            self.position[0] -= 1
            self.tile_state_change()

    def on_down_key_pressed(self):
        self.player_image = pygame.image.load(con.PLAYER_DOWN)
        if ((self.position[0] + 1) * con.TILE_SIZE) < self.tiles.height:
            self.position[0] += 1
            self.tile_state_change()

    def add_knowledge(self, x, y, char):
        if isinstance(self.map[x][y], str):
            if self.map[x][y] == 'u':
                self.map[x][y] = char
            else:
                if char not in self.map[x][y]:
                    temp = [self.map[x][y], char]
                    self.map[x][y] = temp
        elif isinstance(self.map[x][y], list):
            if char not in self.map[x][y]:
                self.map[x][y].append(char)

    def think_bro_think(self):
        # time.sleep(1)
        valid_path = self.get_valid_path()
        print(valid_path)
        unvisited_path = self.get_unvisited(valid_path)
        print(unvisited_path)
        flag = False
        for i in range(len(unvisited_path)):
            if self.isSafe(unvisited_path[i][0], unvisited_path[i][1]):
                if unvisited_path[i][2] == 'up':
                    self.on_up_key_pressed()
                    flag = True
                elif unvisited_path[i][2] == 'left':
                    self.on_left_key_pressed()
                    flag = True
                elif unvisited_path[i][2] == 'right':
                    self.on_right_key_pressed()
                    flag = True
                elif unvisited_path[i][2] == 'down':
                    self.on_down_key_pressed()
                    flag = True

            if not flag:
                break


    def get_valid_path(self):
        temp = []
        if self.position[1] + 1 < con.COL_COUNT:
            temp.append([self.position[0], self.position[1] + 1, 'right'])
        if self.position[1] - 1 >= 0:
            temp.append([self.position[0], self.position[1] - 1, 'left'])
        if self.position[0] + 1 < con.ROW_COUNT:
            temp.append([self.position[0] + 1, self.position[1], 'down'])
        if self.position[0] - 1 >= 0:
            temp.append([self.position[0] - 1, self.position[1], 'up'])
        return temp

    def sensor_op(self, x, y):
        self.add_knowledge(x, y, 'o')
        self.add_knowledge(x, y, 'v')

        sensors = self.tiles.get_map(x, y)
        for i in range(len(sensors)):
            self.add_knowledge(x, y, sensors[i])

    def isSafe(self, x, y):
        if 'v' in self.map[self.position[0]][self.position[1]] and ('s' or 'b') not in self.map[self.position[0]][self.position[1]]:
            print('OK block')
            return True
        elif 'v' in self.map[self.position[0]][self.position[1]] and ('s' or 'b') in self.map[self.position[0]][self.position[1]]:
            if x + 1 < 10:
                if 'v' in self.map[x+1][y] and ('s' or 'b') not in self.map[x+1][y]:
                    print('safe block')
                    return True
            if x - 1 >= 0:
                if 'v' in self.map[x-1][y] and ('s' or 'b') not in self.map[x-1][y]:
                    print('safe block')
                    return True
            if y + 1 < 10:
                if 'v' in self.map[x][y+1] and ('s' or 'b') not in self.map[x][y+1]:
                    print('safe block')
                    return True
            if y - 1 >= 0:
                if 'v' in self.map[x][y-1] and ('s' or 'b') not in self.map[x][y-1]:
                    print('safe block')
                    return True
        return False


    def get_unvisited(self, valid_path):
        temp = []
        for i in range(len(valid_path)):
            x = valid_path[i][0]
            y = valid_path[i][1]

            if 'u' in self.map[x][y]:
                temp.append(valid_path[i])
        return temp
