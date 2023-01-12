import numpy as np

def get_input():
    with open("2022/input09.txt") as f:
        return [l.replace("\n", "").split(" ") for l in f]


input = get_input()


moves = {}

rope_pos = np.zeros([10,2])
for i in range(10):
    rope_pos[i,0] -= 1000
    rope_pos[i,1] += 1000

def move(direction, distance):
    tail_positions = set()
    for d in range(distance):
        # print("dir and dist", direction, distance)
        for k in range(9):
            if k == 0:
                if direction == "R":
                    rope_pos[k][1] +=1
                elif direction == "L":
                    rope_pos[k][1] -= 1
                elif direction == "U":
                    rope_pos[k][0] -= 1
                else:
                    rope_pos[k][0] += 1


            if (abs(rope_pos[k+1,0] - rope_pos[k,0]) <= 1) & (abs(rope_pos[k+1,1] - rope_pos[k,1]) <= 1):
                None
            elif direction == "R":
                # print("R", k, rope_pos[k+1,:], rope_pos[k,:])
                rope_pos[k+1,1] +=1
                if rope_pos[k+1,0] < rope_pos[k,0]:
                    rope_pos[k+1,0] += 1
                elif rope_pos[k+1,0] > rope_pos[k,0]:
                    rope_pos[k + 1, 1] -= 1
            elif direction  == "L":
                # print("L", k, rope_pos[k+1,:], rope_pos[k,:])
                rope_pos[k+1,1] -=1
                if rope_pos[k+1,0] < rope_pos[k,0]:
                    rope_pos[k+1,0] += 1
                elif rope_pos[k+1,0] > rope_pos[k,0]:
                    rope_pos[k+1, 0] -= 1
            elif direction == "U":
                # print("U", k, rope_pos[k+1,:], rope_pos[k,:])
                rope_pos[k+1,0] -=1
                if rope_pos[k+1,1] < rope_pos[k,1]:
                    rope_pos[k+1,1] += 1
                elif rope_pos[k+1,1] > rope_pos[k,1]:
                    rope_pos[k + 1, 1] -= 1
            elif direction  == "D":
                # print("K", k, rope_pos[k+1,:], rope_pos[k,:])
                rope_pos[k+1,0] +=1
                if rope_pos[k+1,1] < rope_pos[k,1]:
                    rope_pos[k+1,1] += 1
                elif rope_pos[k+1,1] > rope_pos[k,1]:
                    rope_pos[k + 1, 1] -= 1
            # add the position to the list

        print(rope_pos)
        tail_positions.add(tuple(rope_pos[9, :]))
    print("Full pos:", direction, rope_pos,"end full")
    # print("Position of tail", tuple(rope_pos[9, :]))
    # tail_positions.add((0,0)) #  starting position
    return tail_positions


def p1(input):
    all_pos = set()
    for i in input[:3]:
        direction = i[0]
        distance = int(i[1])

        positions = move(direction, distance)
        all_pos = all_pos.union(positions)

    return all_pos

#Possible inputs
input = [['R', '4']
         ,['U', '4']
         ,['L', '3']
         ,['D', '1']
         ,['R', '4']
         ,['D', '1']
         ,['L', '5']
         ,['R', '2']]

input = [['R', '5']
         ,['U', '8']
         ,['L', '8']
         ,['D', '3']
         ,['R', '17']
         ,['D', '10']
         ,['L', '25']
         ,['U', '20']]

#6888 too high
#4508 too high
results = p1(input)
print("Done")

tail_places = np.zeros([2000,2000])
for i in results:
    tail_places[int(-i[0]),int(i[1])] = 1