import sympy as s

with open("2022/input21.txt") as f:
    details = [(l.split(":")[0], l.split(" ")[1:]) for l in f.read().split("\n")]

# build our monkey knowledge
unknown_monkeys = {}
known_monkeys = {}
for m in details:
    name = m[0]
    if len(m[1]) == 1:
        known_monkeys[name] = int(m[1][0])
    else:


        val1 = m[1][0]
        val2 = m[1][2]
        op = m[1][1]
        if val1 == "humn":
            val1 = 'x'
        if val2 == 'humn':
            val2 = 'x'
        unknown_monkeys[name] = (val1, val2, op)

# fix our understanding to unknown humn, and proper root equation
known_monkeys.pop('humn')
root = unknown_monkeys['root']
unknown_monkeys['root'] = (root[0], root[1], "=")


root = unknown_monkeys['root']
root = root[0] + "-" + root[1]
unknown_monkeys.pop("root")

# loop that replaces changes known and unknown until all that is left is one variable representing humn
for i in range(200): #good change for generality would make this a while loop and check for changes to root
    for k in unknown_monkeys.keys():
        if root.find(k) >= 0:
            root = root.replace(k, "(" + unknown_monkeys[k][0] + unknown_monkeys[k][2] + unknown_monkeys[k][1] + ")")
    for k in known_monkeys.keys():
        if root.find(k) >= 0:
            root = root.replace(k, str(int(known_monkeys[k])))


results = root
eq = s.parsing.sympy_parser.parse_expr(results)

print(s.solve(eq))
