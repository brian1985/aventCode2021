import numpy as np


class Plant:
    def __init__(self, grid, move):
        self.grid = grid
        self.move_order = move.copy()
        self.elfs = []

        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i,j] == 1:
                    self.elfs.append((i,j)) #list of positions of elves

        # print(self.elfs)

    def move_north(self, y, x):
        s = sum(self.grid[y-1, x-1:x+2])
        print(s, "N")
        if s == 0:
            return True, (y-1, x)
        return False, (None, None)

    def move_south(self, y, x):
        s = sum(self.grid[y+1, x-1:x+2])
        # print(s, "S")
        if s == 0:
            return True, (y+1, x)
        return False, (None, None)

    def move_east(self,y, x):
        s = sum(self.grid[y-1:y+2, x+1])
        # print(s, "E")
        if s == 0:
            return True, (y, x+1)
        return False, (None, None)

    def move_west(self, y, x):
        s = sum(self.grid[y - 1:y + 2, x - 1])
        # print(s, "W")
        if s == 0:
            return True, (y, x - 1)
        return False, (None, None)

    def move_eight(self, y, x):
        print("Move EIght", (y,x))
        # first element is whether it is empty
        # if all true then empty and don't need to move. So return true.
        return all([self.move_south(y,x)[0], self.move_north(y,x)[0], self.move_east(y,x)[0], self.move_west(y,x)[0]])

    def get_moves(self):
        new_loc = {}

        for elf in self.elfs:
            found_move = False
            dir = 'N'
            is_alone = self.move_eight(elf[0], elf[1])
            # print("processing elf", elf)
            if not is_alone:
                for move_dir in self.move_order:
                    if move_dir == 'N' and (not found_move):
                        found_move, move = self.move_north(elf[0], elf[1])
                        dir = 'N'

                    if (move_dir == 'S') and (not found_move):
                        found_move, move = self.move_south(elf[0], elf[1])
                        dir = 'S'

                    if (move_dir == 'E') and (not found_move):
                        found_move, move = self.move_east(elf[0], elf[1])
                        dir = 'E'

                    if (move_dir == 'W') and (not found_move):
                        found_move, move = self.move_west(elf[0], elf[1])
                        dir = 'W'

                print("Move:", f"Current: {elf} to {move}")


                #  idea is if key is not there, they are first to propose the move
                #  else conflict and both don't move.
                    #add current elf to current location
                    #replace existing key with modified key based on its value (direction)
                #  never more than two elves will propose same spot.
                if move in new_loc.keys():
                    val = new_loc.pop(move)

                    # Here val is the direction it moved to get here. So reverse that move and add as key
                    if val == 'S':
                        new_loc[(move[0]-1,move[1])] = "Same"
                    elif val == 'N':
                        new_loc[(move[0]+1,move[1])] = "Same"
                    elif val == 'E':
                        new_loc[(move[0],move[1]-1)] = "Same"
                    elif val == 'W':
                        new_loc[(move[0],move[1]+1)] = "Same"
                    else:
                        print("Error?", val, move)

                    new_loc[elf] = "Same"
                else:
                    new_loc[move] = dir

            else:
                print("Alone")
        return list(new_loc.keys())


    def rebuild_grid(self):
        print("Rebuild")
        self.grid = np.zeros(self.grid.shape)
        for elf in self.elfs:
            print(elf, "elf loc")
            self.grid[elf] = 1

    def cycle_move_order(self):
        first_move = self.move_order.pop(0)
        self.move_order.append(first_move)

    def run(self):
        for _ in range(2):
            print("Iterating")
            self.elfs = self.get_moves()
            self.rebuild_grid()
            self.cycle_move_order()


with open("2022/input23.txt") as f:
    inputs = f.read()
    grid = [list(map(eval,list(l))) for l in inputs.replace(" ", "0")\
    .replace(".", "0")\
    .replace("#", "1").split("\n")]

moves = ['N', 'S', 'W', 'E'] #0=North, 1=south, 2=West, 3=East
grid = np.array(grid)

p = Plant(grid, moves)
p.run()
