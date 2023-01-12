import numpy as np

def get_input():
    lines = []
    with open("2022/input10.txt") as f:
        for l in f:
            lines.append(l.replace("\n","").split(" "))
    return lines



lines = get_input()


def p1(lines):
    illuminated_pixels = np.zeros(240)
    x = 1
    current_cycle = 1

    sums = 0
    for idx, l in enumerate(lines):
        # print(f"Line {l}")
        if l[0] == 'noop':
            if ((x-1== current_cycle%40) | (x+1==current_cycle%40) | (x==current_cycle%40)):
                # print("illuminate noop", x, current_cycle-1)
                illuminated_pixels[current_cycle-1] = 1

            if current_cycle in [20, 60, 100, 140, 180, 220]:
                sums += current_cycle * x
            current_cycle += 1
        if l[0] == 'addx':
            for c in range(2): # two cycles for addx
                if ((x-1 == current_cycle%40) | (x+1 == current_cycle%40) | (x == current_cycle%40)):
                    # print("illuminate", x, current_cycle-1)
                    illuminated_pixels[current_cycle - 1] = 1

                if current_cycle in [20, 60, 100, 140, 180, 220]:
                    sums += current_cycle * x

                current_cycle += 1
            # print("Next value to add",int(l[1]))
            x += int(l[1])

    return sums, illuminated_pixels


#5760 too low
total, _ = p1(lines)


def p2(lines):
    x = 1
    cycle = 1
    illuminated_pixels = np.zeros(240)
    operation_times = {'noop':1, 'addx':2}

    def next_cycle():
        return 1

    def process_cycle(c, x):
        if ((c-1)%40) in [x,x+1,x-1]:
            return 1
        return 0
    def increment_x(x, addon):
        return x+addon

    for op in lines:
        for idx in range(operation_times[op[0]]):
            result = process_cycle(cycle, x)

            illuminated_pixels[cycle-1] = result
            cycle += next_cycle()

        if op[0] == 'addx':
            x = increment_x(x, int(op[1]))

    return illuminated_pixels

illuminated_pixels = p2(lines)
final_image = illuminated_pixels.reshape([-1,40])