import numpy as np


class Tetris:
    def __init__(self, start):
        self.tetris_map = None
        self.sand_counter = 0
        self.start = start
        self.max_y = 0

        self.build_map(start)
        self.tetris_map[-1,:] = 1


    def read_file(self):
        with open("2022/input14.txt") as f:
            walls = f.read().strip().split('\n')
        return walls

    def init_map(self):
        self.tetris_map = np.zeros([self.max_y + 2 + 1, 1000]) # max_y + 2 per rules + 1 to include endpoint of index

    def parse_walls(self, walls):
        for idx, wall in enumerate(walls.copy()):
            wall = wall.replace(" ", "").split("->")

            for i in range(len(wall)):
                x = int(wall[i].split(",")[0])
                y = int(wall[i].split(",")[1])
                wall[i] = (y, x)

                self.max_y = max(self.max_y, y)
            walls[idx] = wall
        return walls

    def build_map(self, start):
        walls = self.read_file()
        walls = self.parse_walls(walls)

        self.init_map()

        for segments in walls:
            self.add_wall(segments)

        self.tetris_map[start[0], start[1]] = 2

    def add_wall(self, segments):

        for idx in range(len(segments)-1):
            left = min(segments[idx][1],segments[idx+1][1])
            right = max(segments[idx][1],segments[idx+1][1])
            top = min(segments[idx][0],segments[idx+1][0])
            btm = max(segments[idx][0],segments[idx+1][0])

            self.tetris_map[top:btm+1, left:right+1] = 1


    def place_sand(self):
        current_pos = self.start.copy()

        while True:
            try:
                if self.tetris_map[current_pos[0]+1, current_pos[1]] == 0:
                    current_pos[0] += 1
                elif self.tetris_map[current_pos[0]+1, current_pos[1]-1] == 0:
                    current_pos[0] += 1
                    current_pos[1] -= 1
                elif self.tetris_map[current_pos[0] + 1, current_pos[1] + 1] == 0:
                    current_pos[0] += 1
                    current_pos[1] += 1
                else:
                    if current_pos == self.start:
                        return False
                    else:
                        break

            except IndexError:
                print("Need wider map, index error from side")
                return False
        self.tetris_map[current_pos[0], current_pos[1]] = 1
        return True


    def play(self):
        while True:
            is_placed = self.place_sand()
            if is_placed:
                self.sand_counter += 1
            else:
                break


#30018
best_game = 0
for i in range(300,600):
    t = Tetris([0, i])
    t.play()
    best_game = max(best_game, t.sand_counter+1)