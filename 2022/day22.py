import re
import numpy as np

with open("2022/input22.txt") as f:
    inputs = f.read().split("\n\n")
    image = [list(map(eval,list(l))) for l in inputs[0].replace(" ", "0")\
    .replace("v",".")\
    .replace(">",".")\
    .replace("<v>",".")\
    .replace(".", "1")\
    .replace("#", "2").split("\n")]
    #image = np.array(image)
    input = inputs[1]

max_length = 0
for l in image:
    max_length = max(max_length, len(l))
for idx, l in enumerate(image):
    image[idx] += [0] * (max_length-len(l))

image_pad = np.pad(np.array(image),[1,1])
image = np.array(image)
# input = "10R5L5R10L4R5L5"
input = re.split("([A-Z])", input)
input.insert(0, "R")

def move_face2face(x, y, d):

    if x >= 50 and x < 100 and y < 50:
        face = 'A'
    elif x >= 100 and y < 50:
        face = 'B'
    elif x < 50 and y >= 100 and y < 150:
        face = "D"
    elif x < 50 and y >= 150:
        face = "F"
    elif x >= 50 and y >= 50 and y < 100:
        face = "C"
    elif x >= 50 and x < 100 and y >= 100 and y < 150:
        face = "E"
    else:
        print("Bad value for x and y", x,y)

    if d == 'U':
        if face == 'A':
            d = 'R'
            temp = x
            x = 0
            y = temp + 100

        if face == 'B':
            x -= 100
            y += image.shape[0]-1

        if face == "D":
            d = 'R'
            temp = x
            x = 50
            y = 50 + temp

    elif d == 'L':
        if face == 'A':
            d = 'R'
            x = 0
            y = 149 - y

        if face == 'C':
            d = 'D'
            x = y-50
            y = 100

        if face == 'D':
            d = 'R'
            x = 50
            y = 149 - y

        if face == "F":
            d = 'D'
            x = y-100
            y = 0

    elif d == 'R':
        if face == 'B':
            d = 'L'
            x = 99
            y = 149 - y

        if face == 'C':
            d = 'U'
            x = y + 50
            y = 49

        if face == 'E':
            d = 'L'
            x = image.shape[1]-1
            y = 149 - y

        if face == 'F':
            d = 'U'
            x = y-100
            y = 149

    elif d == 'D':
        if face == 'B':
            d = 'L'
            temp = x
            x = 99
            y = temp - 50

        if face == 'F':
            x += 100
            y = 0

        if face == 'E':
            d = 'L'
            temp = x
            x = 49
            y = temp + 100

    return x,y,d

def move(d, num, x, y, debug=0):
    for i in range(num):
        facechange = False
        if debug == 1:
            print((y,x), d)
        if d == "R":
            if x + 1 == image.shape[1]:
                facechange = True
            elif image[y,x+1] == 2:
                return x,y,d
            elif image[y, x+1] == 1:
                x += 1
            else:
                facechange = True

                # j = 0
                # while image[y, j] != 1:
                #     if image[y, j] == 2:
                #         return x, y
                #     j += 1
                # x = j

        if d == "L":
            if x == 0:
                facechange = True
            elif image[y,x-1] == 2:
                return x,y,d
            elif image[y, x-1] == 1:
                x -= 1
            else:
                facechange = True
                # j = image.shape[1]-1
                # while image[y, j] != 1:
                #     if image[y, j] == 2:
                #         return x,y
                #     j -= 1
                # x = j

        if d == "U":
            if y == 0:
                facechange = True
            elif image[y-1, x] == 2:
                return x, y,d
            elif image[y-1, x] == 1:
                y -= 1
            else:
                facechange = True
                # j = image.shape[0] - 1
                # while image[j, x] != 1:
                #     if image[j, x] == 2:
                #         return x, y
                #     j -= 1
                # y = j

        if d == "D":
            if y+1 == image.shape[0]:
                facechange = True
            elif image[y+1, x] == 2:
                return x, y,d
            elif image[y+1, x] == 1:
                y += 1
            else:
                facechange = True
                # j = 0
                # while image[j, x] != 1:
                #     if image[j, x] == 2:
                #         return x,y
                #     j += 1
                # y=j
        if facechange:
            temp_x, temp_y, temp_d = move_face2face(x, y, d)
            if image[temp_y, temp_x] == 2:
                return x, y, d
            else:
                x, y, d = temp_x, temp_y, temp_d

    return x, y, d

# x,y = move('R', 3, 8, 0)
# x,y = move('D',5, x, y)
def p1(image, input, x, y, cur_direction='U'):
    cw = {"U":"R", "R":"D", "D":"L", "L":"U"}

    for i in range(0, len(input), 2):
        rotation = input[i]
        if rotation == 'R':
            cur_direction = cw[cur_direction]
        else:
            cur_direction = cw[cw[cw[cur_direction]]]
        x, y, cur_direction = move(cur_direction, int(input[i + 1]), x, y, 0)

    return x+1, y+1, cur_direction

x,y, final_facing = p1(image, input,50, 0)

facing_val = {'L':2, 'R':0, "U": 3, "D":1}

#147084 too high

print(1000*y+4*x + facing_val[final_facing])

