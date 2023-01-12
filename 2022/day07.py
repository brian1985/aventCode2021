def get_input():
    commands = []
    with open("2022/input07.txt") as f:
        for l in f:
            commands.append(l)

    return commands

class Tree:
    def __init__(self, name, parent_node=None):
        self.name = name
        self.parent_node = parent_node
        self.files = {}
        self.subdirectories = {}
        self.total_direct_size = 0

        self.small_directories = {}
        self.large_directories = {}

    def add_directory(self, name, node):
        if name not in self.subdirectories:
            self.subdirectories[name] = node


    def add_file(self, size, name):
        if name not in self.files:
            self.files[name] = size
            self.total_direct_size += size

    def depth_traverse_sum(self, node):
        for n in node.subdirectories.values():
            node.total_direct_size += self.depth_traverse_sum(n)
        return node.total_direct_size

    # only call after depth_traverse_sum
    def depth_traverse_find(self, node, root, threshold=100000, direction='s'):
        for n in node.subdirectories.values():
            self.depth_traverse_find(n, root, threshold, direction)
            if (n.total_direct_size <= threshold) & (direction == 's'):
                #when adding directories, care is taken if a subdirectory name matches a directory name.
                # don't add new key, but add value to existing key
                if n.name in root.small_directories:
                    root.small_directories[n.name.replace("\n", "")] += n.total_direct_size
                else:
                    root.small_directories[n.name.replace("\n", "")] = n.total_direct_size
            elif (n.total_direct_size >= threshold) & (direction == 'l'):
                if n.name not in root.large_directories:
                    root.large_directories[n.name.replace("\n", "")] = n.total_direct_size
                elif n.name.replace("\n", "")+"_"+n.parent_node.name.replace("\n", "") not in root.large_directories:
                    root.large_directories[n.name.replace("\n", "")+"_"+n.parent_node.name.replace("\n", "")] = n.total_direct_size
                else:
                    print("Still can't separate")
        return

import re
file_search = re.compile("^[0-9]+")
in_directory = re.compile("^\$ cd [a-zA-Z]+")
out_directory = re.compile("^\$ cd \.\.")
listed_dir = re.compile("^dir")
home_dir = re.compile("^\$ cd /")
ls_command = re.compile("^\$ ls")

m =home_dir.match("$ cd /")
def p1(commands):
    root = Tree("root")

    current_node = root
    for c in commands:
        if home_dir.match(c) is not None: #command run
            current_node = root
        if ls_command.match(c) is not None:
            pass
        if listed_dir.match(c) is not None:
            node = Tree(c.split(" ")[1], current_node)
            current_node.add_directory(c.split(" ")[1], node)
        if file_search.match(c) is not None:
            current_node.add_file(int(c.split(" ")[0]), c.split(" ")[1])
        if in_directory.match(c) is not None:
            # print("Switching nodes from", current_node)
            current_node = current_node.subdirectories[c.split(" ")[2]]
            # print("Switching nodes to", current_node)
        if out_directory.match(c) is not None:
            # print(f"Out: {c}", node)
            current_node = current_node.parent_node

    return root

commands = get_input()
tree = p1(commands)
tree.depth_traverse_sum(tree)
tree.depth_traverse_find(tree, tree)

#1253191 is too small
#1379061 too small
#42476859 too large
#33921587 not right
size_small = 0
for d in tree.small_directories.values():
    size_small += d

total_free_space = 70000000 - tree.total_direct_size
needed_space = 30000000-total_free_space

#4131645 too large
print("Finding larger")
tree.depth_traverse_find(tree, tree, needed_space, 'l')
print(min(tree.large_directories.values()))
