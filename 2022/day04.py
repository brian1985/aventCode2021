def get_input():
    groups = []
    with open("2022/input04.txt") as f:
        for l in f:
            row = l.replace("\n","").split(",")
            print(row)
            result = [row[0].split("-"), row[1].split("-")]
            groups.append(result)
    return groups



#453 too low
pairs = get_input()
total_overlaps = 0
partial_overlaps = 0
for r in pairs:
    a,b,c,d = int(r[0][0]), int(r[0][1]), int(r[1][0]), int(r[1][1])
    print(a,b,c,d)
    if (a >= c) & (b <= d):
        total_overlaps += 1
    if (c > a) & (d <= b) | (c >= a) & (d < b):
        total_overlaps += 1
    if ((b >= c) & (b <= d)) | ((a <= d) & (a >= c)) | ((c >= a) & (c<=b)):
        print("Three")
        partial_overlaps += 1
