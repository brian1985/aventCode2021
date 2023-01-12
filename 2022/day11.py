


class Monkey:
    def __init__(self, worry_levels, div_num, true_num, false_num, op, op_num):
        self.worry_levels = worry_levels
        self.counter = 0

        # testing values
        self.div_num = int(div_num)
        self.true_num = int(true_num)
        self.false_num = int(false_num)

        # operation values
        self.op = op
        self.op_num = op_num

    def operation(self, worry_num):
        if self.op == "*":
            if self.op_num == 'old':
                return worry_num * worry_num
            else:
                return worry_num * int(self.op_num)
        else:
            return worry_num + int(self.op_num)


    def test(self, worry):
        return int(self.true_num) if worry%int(self.div_num) ==0 else int(self.false_num)

    def inspect(self):
            self.counter += 1

    def adjust_worry(self, idx):
        self.worry_levels[idx] = self.operation(self.worry_levels[idx])
        self.worry_levels[idx] = self.worry_levels[idx]%9699690

    def where_throw(self, idx):
        # print("where throw", idx, self.worry_levels[idx], self.test(self.worry_levels[idx]))
        next_monkey = self.test(self.worry_levels[idx])
        return next_monkey

    def add_item(self, item):
        self.worry_levels.append(item)


class Round:
    def __init__(self, monkeys):
        self.monkeys = monkeys

    def play_round(self):
        for m_num, monkey in enumerate(monkeys):
            for idx, worry in enumerate(monkey.worry_levels.copy()):
                monkey.inspect()
                monkey.adjust_worry(idx)
                next_monkey = monkey.where_throw(idx)
                #  print(next_monkey, m_num)
                self.monkeys[next_monkey].add_item(monkey.worry_levels[idx])
            monkey.worry_levels = []


def get_process_input():
    monkeys = []
    with open("2022/input11.txt") as f:
        for l in f:
            if l[0:6] == 'Monkey':
                worry_levels = [int(x) for x in f.readline().replace("\n", "").replace(",","").strip().split(" ")[2:]]
                line = f.readline().replace("\n", "").strip().split(" ")
                num = line[-1]

                div_num = f.readline().strip().replace("\n","").split(" ")[-1]
                true_num = f.readline().strip().replace("\n","").split(" ")[-1]
                false_num = f.readline().strip().replace("\n","").split(" ")[-1]

                # print(div_num,true_num,false_num,test(196))

                monkeys.append(Monkey(worry_levels, div_num, true_num, false_num, line[-2], num))


    return monkeys

# 36 items
monkeys = get_process_input()


r = Round(monkeys)

for i in range(10000):
    r.play_round()
inspections = []
for m in r.monkeys:
    inspections.append(m.counter)

inspections.sort()

#  received hint on this part. Chinese remainder theorem still doesn't make sense.
from math import prod
ans = prod([2,7,13,3,19,17,11,5])
# print(monkeys[0].test(196))
print(inspections[-1] * inspections[-2])
print("FInished")

