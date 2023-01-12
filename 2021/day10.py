from collections import Counter
import numpy as np

def get_data():
    with open("data\\day10.txt") as f:
        data = f.readlines()

    return data

compare_dict = {")":"("
    , "}":"{"
    , "]":"["
    , ">":"<"}

def part_a(data):
    # data = data[:1]
    faulty_characters = []
    incomplete_lines = []

    for d in data:
        is_bad = False
        parsed_list = []

        if len(d) == 0:
            pass
        else:
            parsed_list.append(d[0])
        for ch in d.strip()[1:]:
            # print(parsed_list, "CHAR:",ch)
            if len(parsed_list) == 0:
                parsed_list.append(ch)
            elif ch in compare_dict.values():
                parsed_list.append(ch)
            elif parsed_list[len(parsed_list)-1] == compare_dict[ch]:
                parsed_list.pop()
            else:
                faulty_characters.append(ch)
                is_bad = True
                break

        if not is_bad:
            incomplete_lines.append(parsed_list)


    counts = Counter(faulty_characters)


    char_score = {")":3
                  ,"]":57
                  ,"}":1197
                  ,">":25137}
    total = [char_score[x] * counts[x] for x in counts]
    solution = np.array(total).sum()

    return solution, incomplete_lines


def part_b(incomplete_lines):
    scoring = {'{': 3, '[': 2, '(': 1, '<': 4}
    scores = []
    for line in incomplete_lines:
        line_score = 0

        line.reverse()
        for val in line:
            cost = scoring.get(val,6)
            line_score = 5*line_score + cost

        scores.append(line_score)

    return np.median(np.array(scores))

data = get_data()
score_a, lines = part_a(data)



score_b = part_b(lines)
