from collections import deque

def get_input():
    stacks = [deque(['P','L','M','N','W','V','B','H']),\
             deque(['H','Q','M']),\
             deque(['L','M','Q','F','G','B','D','N']),\
             deque(['G','W','M','Q','F','T','Z']),\
             deque(['P','H','T','M']),\
             deque(['T','G','H','D','J','M','B','C']),\
             deque(['R','V','F','B','N','M']),\
             deque(['S','G','R','M','H','L','P']),\
             deque(['N','C','B','D','P'])]
    instructions = []
    with open("2022/input05.txt") as f:
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        final = f.readline()
        print(final)
        for l in f:
            s = l.replace("\n", "").split(" ")
            a,b,c = int(s[1]), int(s[3]), int(s[5])
            instructions.append([a,b,c])

    return stacks, instructions


stacks, instructions = get_input()
stacks9001 = stacks.copy()

def p1(stacks, instructions):
    for item in instructions:
        fromstack = item[1]
        tostack = item[2]
        for i in range(item[0]):
            top = stacks[fromstack-1].popleft()
            stacks[tostack-1].appendleft(top)

    answer = []
    for item in stacks:
        answer.append(item.popleft())

    return answer

def p2(stacks, instructions):

    for item in instructions:
        move_list = []
        fromstack = item[1]
        tostack = item[2]
        for i in range(item[0]):
            move_list.append(stacks[fromstack - 1].popleft())
        move_list.reverse()
        stacks[tostack - 1].extendleft(move_list)

    answer = []
    for item in stacks:
        answer.append(item.popleft())
    return answer

answer1 = p1(stacks, instructions)
answer2 = p2(stacks9001, instructions)
