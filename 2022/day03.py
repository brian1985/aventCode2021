def get_input():
    data = []
    with open("2022/input03.txt") as f:
        for line in f:
            data.append(line.replace("\n", ""))
    return data

def get_priority_val(priority):
    if priority.isupper():
        priority_total = ord(priority[0]) - 38
    else:
        priority_total = ord(priority[0]) - 96

    return priority_total


def part1(input):
    priority_total = 0
    for i in input:
        l =list(i)

        s1 = set(l[:int(len(l)/2)])
        s2 = set(l[int(len(l)/2):])
        priority = (s1.intersection(s2)).pop()

        priority_total += get_priority_val(priority)

    return priority_total

def part2(input):
    total = 0
    for i in range(0,len(input), 3):
        s1 = set(list(input[i]))
        s2 = set(list(input[i+1]))
        s3 = set(list(input[i+2]))

        priority = s1.intersection(s2).intersection(s3).pop()

        total += get_priority_val(priority)

    return total

#7859 too high
input = get_input()
result = part1(input)
result2 = part2(input)
