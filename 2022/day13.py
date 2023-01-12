with open("2022/input13.txt") as f:
    groups = f.read().strip().split("\n\n")

def compare(item1, item2):


    if isinstance(item1, int) & isinstance(item2, list):
        item1 = [item1]
    if isinstance(item1, list) and isinstance(item2, int):
        item2 = [item2]
    if (isinstance(item1, int)) and (isinstance(item2, int)):
        # print(item1, item2)
        if item1 < item2:
            return 1
        elif item2 < item1:
            return -1
        else:
            return 0

    if isinstance(item1, list) and isinstance(item2, list):
        i = 0

        while i < len(item1) and i < len(item2):
            x = compare(item1[i], item2[i])
            # print(x, item1[i],item2[i])
            if x == -1:
                return -1

            if x == 1:
                return 1

            i += 1

        if i == len(item1):
            if len(item1) == len(item2):
                return 0
            return 1

        if i == len(item2):
            return -1


#5764 too high
#5683 too high
#4680 not item2
#748 too low
#820 too low
#4451 not item2
#5304 not item2
#5506 item2
#got hints from: https://github.com/womogenes/AoC-2022-Solutions/blob/main/day_13/day_13_p1.py
# had a few bugs in the code.
total = 0
items = []
for idx, g in enumerate(groups):
    a,b = map(eval, g.split("\n"))

    result = compare(a,b)

    if result == 1:
        items.append(a)
        items.append(b)
        total += (idx+1)
    else:
        items.append(b)
        items.append(a)



items.append([[2]])
items.append([[6]])


import functools
compared = sorted(items, key=functools.cmp_to_key(compare), reverse=True)

#3660 too low
print("IDX multiple is:", (compared.index([[2]])+1) * (compared.index([[6]])+1))