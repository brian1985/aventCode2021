import numpy as np


def get_input():
    with open("2022/input12.txt") as f:
        heightmap = f.readlines()
        heightmap = [list(m.replace("\n","")) for m in heightmap]
        heightmap = [list(map(ord, hm)) for hm in heightmap]
        heightmap = np.array(heightmap)
        sx,sy = np.where(heightmap == 83)
        ex,ey = np.where(heightmap == 69)

        sx= sx[0]
        sy= sy[0]
        ex= ex[0]
        ey= ey[0]
        return heightmap, (sx,sy), (ex,ey)


class Tree:
    def __init__(self, height, location, depth):
        self.children = []
        self.height = height
        self.location = location

        self.depth = depth
        self.is_connected_end = False



    def get_children(self, node, map, checked_spots, end_spot):
        checked_spots, boolU = node.check_add_up(map, checked_spots, end_spot)
        checked_spots, boolD  = node.check_add_down(map, checked_spots, end_spot)
        checked_spots, boolL  = node.check_add_left(map, checked_spots, end_spot)
        checked_spots, boolR  = node.check_add_right(map, checked_spots, end_spot)

        if any([boolU,boolD,boolR,boolL]):
            for child in node.children:
                # print("Loop", child.height, child.location)
                node.get_children(child, map, checked_spots, end_spot)
        return checked_spots

    def check_add_up(self, hm, checked_spots, end_spot):
        x, y = self.location[1], self.location[0]

        if (y != 0):
            height = hm[y - 1, x]

            if (height <= self.height + 1):
                self.set_is_connected(end_spot, (y-1,x))
                if (y-1,x) == end_spot:
                    self.is_connected_end = True

                if (checked_spots[y - 1, x] != 1):
                    t = Tree(height, (y-1,x), self.depth+1)
                    self.children.append(t)
                    checked_spots[y-1, x] = 1

                    return checked_spots, True
        return checked_spots, False

    def check_add_down(self, hm, checked_spots, end_spot):
        x, y = self.location[1], self.location[0]

        if (y != hm.shape[0]-1):
            height = hm[y + 1, x]

            if (height <= self.height + 1):
                self.set_is_connected(end_spot, (y+1,x))

                if (checked_spots[y + 1, x] != 1):
                        t = Tree(height, (y + 1, x), self.depth+1)
                        self.children.append(t)
                        checked_spots[y + 1, x] = 1

                        return checked_spots, True
        return checked_spots, False

    def check_add_left(self, hm, checked_spots, end_spot):
        x, y = self.location[1], self.location[0]

        if (x != 0):
            height = hm[y, x - 1]

            if (height <= self.height + 1):
                self.set_is_connected(end_spot, (y,x-1))
                if (checked_spots[y, x - 1] != 1):

                    t = Tree(height, (y, x - 1), self.depth+1)
                    self.children.append(t)
                    checked_spots[y, x - 1] = 1

                    return checked_spots, True
        return checked_spots, False

    def check_add_right(self, hm, checked_spots, end_spot):
        x, y = self.location[1], self.location[0]

        if (x != hm.shape[1]-1):
            height = hm[y, x + 1]
            if (height <= self.height + 1):

                self.set_is_connected(end_spot, (y,x+1))

                if (checked_spots[y, x + 1] != 1):
                    t = Tree(height, (y, x + 1), self.depth+1)
                    self.children.append(t)
                    checked_spots[y, x + 1] = 1

                    return checked_spots, True
        return checked_spots, False

    def set_is_connected(self, e, loc):
        if e == loc:
            self.is_connected_end = True

    def find_end_depth(self, node, min_depth = 1000000):
        if node.is_connected_end:
            print(node.depth)
            return node.depth
        for child in node.children:
            print(child.location)
            depth = node.find_end_depth(child)
            min_depth = min(depth, min_depth)
        return min_depth

heightmap, s,e = get_input()

#remove
# heightmap = heightmap[:3,:3]
# e = (2,2)
#end remove

heightmap[s] = 97
heightmap[e] = 122

#re3move
# heightmap[e] = 98
#end remove

checked_spots = np.zeros([heightmap.shape[0], heightmap.shape[1]])
checked_spots[s] = 1

root = Tree(heightmap[s], s, 0)
checked_spots = root.get_children(root, heightmap, checked_spots, e)

#562 too high
min_depth = root.find_end_depth(root) - 1


from queue import PriorityQueue



pq = PriorityQueue()


def DijkstraAlgorithm(heightmap, s):

    sptSet = PriorityQueue()

    all_nodes = PriorityQueue()

    #init root node
    checked_spots = np.zeros([heightmap.shape[0], heightmap.shape[1]]) # 1 = visited
    checked_spots[s] = 1

    def update_children(node):
        loc = node[1]
        dist = node[0]
        y = loc[0]
        x = loc[1]
        node_height = heightmap[y,x]

        # dL,dR,dU,dD = 0,0,0,0

        #  left
        if loc[1] != 0 and heightmap[y, x-1] <= node_height+1:
            dL = 1

        #  right
        if loc[1] != heightmap.shape[1]-1 and heightmap[y, x+1] <= node_height+1:
            dR = 1

        #  up
        if loc[0] != 0 and heightmap[y-1, x] <= node_height+1:
            dU = 1

        #  down
        if loc[0] != heightmap.shape[0]-1 and heightmap[y+1, x] <= node_height+1:
            dD = 1

        return

    #build nodes with their distances (0 and ~inf)
    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):
            if (i,j) == s:
                all_nodes.put((0, s))
            else:
                all_nodes.put((105000, (i,j)))

    min_node = all_nodes.get()
    sptSet.put(min_node)

    update_children(min_node)



    def traverse(self):

        if s[0] != 0:
            # up
            pass

        if s[0] != map.shape[0] - 1:
            # down
            pass

        if s[1] != 0:
            # left
            pass

        if s[1] != map.shape[1] - 1:
            # right
            pass













