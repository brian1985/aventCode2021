import numpy as np
with open("2022/input20.txt") as f:
    l = list(map(eval,f.read().strip().split("\n")))

# for all i
    #step one remove item at index i
    #place item at index i + val modulo the length of list
    #update indexes
        #if placed further down the list, subtract 1 from middle indexes
        # if placed before its prior index, add 1 to middle indexes

z = list(range(len(l)))

def p1(l,z):
    for i in range(len(l)): # len(l)
        current_index = z[i]
        item = l[current_index]
        new_index = (item + current_index) % (len(l)-1)
        if new_index == 0:
            new_index = len(l)-1


        if new_index > current_index:
            val = l.pop(current_index)
            l.insert(new_index, val)
            for j in range(len(l)):
                if j == i:
                    pass
                elif z[j] <= new_index and z[j] >= current_index:
                    z[j] -= 1



        elif new_index < current_index:
            l.insert(new_index, item)
            l.pop(current_index+1)
            for j in range(len(l)):
                if i == j:
                    pass
                elif z[j] <= current_index and z[j >= new_index]:
                    z[j] +=1

        z[i] = new_index
    idx0 = l.index(0)
    print(idx0)
    total = l[(idx0 + 1000) % len(l)] + l[(idx0 + 2000) % len(l)] + l[(idx0 + 3000) % len(l)]
    return total, l[(idx0 + 1000) % len(l)], l[(idx0 + 2000) % len(l)], l[(idx0 + 3000) % len(l)]


# total,l1,l2,l3 = p1(l,z)








###part 2
import numpy as np
with open("2022/input20.txt") as f:
    l = list(map(eval,f.read().strip().split("\n")))
d={}
for l1 in l:
    d[l1] = 1

l = [20,19,7,0,6,3]
scale = 1#811589153
l = [l1*scale for l1 in l] #
ol = l.copy()
# for all i
    #step one remove item at index i
    #place item at index i + val modulo the length of list
    #update indexes
        #if placed further down the list, subtract 1 from middle indexes
        # if placed before its prior index, add 1 to middle indexes

z = list(range(len(l)))

print(z,l)
def p2(l,z):
    for mixNum in range(1):
        for i in range(len(l)): # len(l)
            current_index = z[i]
            item = l[current_index]
            new_index = (item + current_index) % (len(l)-1)

            # print(item, current_index, new_index)
            if (new_index == 0) and (item < 0):
                new_index = len(l)-1
            if (new_index == len(l)-1) and (item > 0):
                new_index = 0

            if ol[i] == 20:
                print(current_index, new_index)

            l.pop(current_index)
            l.insert(new_index, item)

            for j in range(len(l)):
                loc = l.index(ol[j])
                z[j] = loc

            print(current_index,new_index,item,z,l, ol[i])
        print(f"Item={item}",f"i={i}", "(c,n)", (current_index,new_index), z, l)


    print("Final array", l)
    idx0 = l.index(0)
    total = l[(idx0+1000) % len(l)] + l[(idx0+2000) % len(l)] + l[(idx0+3000) % len(l)]
    return total

p2(l,z)