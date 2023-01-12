def get_input():
    with open ("2022/input01.txt") as f:
        return f.read()

input = get_input()
results = input.split("\n\n")
totals = []
for r in results:
    totals.append(sum([int(x) for x in r.split("\n")]))

max(totals)
totals.sort()
sum(totals[-3:])




#  understanding someone elses generator code:


from heapq import nlargest

result = (row for row in open("2022/input01.txt"))

# calorie_counter = 0
# #  for now store all values, next iteration store just top n for memory
# sums = []
# while True:
#     try:
#         input = next(result)
#         calorie_counter += input
#         print(f"Value of {input}")
#     except ValueError:
#         sums.append(calorie_counter)
#         print("Next elf please!")

from heapq import nlargest
def input():
    while True:
        with open("2022/input01.txt") as f:
            yield f.readline()



def gen_elf_lines():
    """a generator of consecutive elf lines, converted to int

    call multiple times to get different elves, won't yield at all
    (StopIteration exception) when there are no more.

    Elves line items with value zero are included, so don't assume
    sum(gen_elf_lines())==0 means end of file
    """
    while True:
        try:
            yield int(input())
        # catching ValueError covers the blank lines, EOFError covers
        # when we reach end of file
        except (ValueError, EOFError):
            break # while True

def gen_elf_sums():
    """A generator of elf sums.

    Uses constant memory, one elf with many items is fine
    """
    while True: # StopIteration exception will stop this loop
        # we test for more input by starting with one line
        # StopIteration will be raised if we're all out
        #
        # this apprach supports 0 as an allowable input
        # otherwise we would just sum(gen_elf_lines()) and stop when 0 hit
        elf_line_gen = iter(gen_elf_lines())
        try:
            first_elf_line = next(elf_line_gen) # raises StopIteration
        except StopIteration:
            break
        yield sum(elf_line_gen, first_elf_line)


def part_1():
    return max(gen_elf_sums())

print(part_1())