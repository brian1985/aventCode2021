points = {"X":1,"Y":2,"Z":3}
conversion = {"Y":"B", "X":"A", "Z":"C"}

draw = {"A":'X',"B":"Y","C":"Z"}
win = {"A":"Y", "B":"Z", "C":"X"}
lose = {"A":"Z", "B":"X", "C":"Y"}
def get_input():
    return (x.replace("\n","").split(" ") for x in open("2022/input02.txt"))


input = get_input()

total_score = 0
while True:
    try:
        opp, me = next(input)
        if me == "X":
            me = lose[opp]
        elif me == 'Y':
            me = draw[opp]
        else:
            me = win[opp]
        if opp == conversion[me]:
            total_score += 3
        elif ((opp == "A") & (me == "Y")) | ((opp == "B") & (me == "Z")) | ((opp == "C") & (me == "X")):
            total_score += 6
        total_score += points[me]
    except StopIteration:
        break
print(f"Final score= {total_score}")

total_score = 0
input = get_input()
while True:
    try:
        opp, me = next(input)

        if opp == conversion[me]:
            total_score += 3
        elif ((opp == "A") & (me == "Y")) | ((opp == "B") & (me == "Z")) | ((opp == "C") & (me == "X")):
            total_score += 6
        total_score += points[me]
    except StopIteration:
        break
print(f"Final score= {total_score}")
