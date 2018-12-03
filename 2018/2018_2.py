# Part 1


def id_contains_multiple(id_str: str, count_num: int) -> bool:
    letters = set(id_str)
    counts = [id_str.count(x) for x in letters]
    if count_num in counts:
        return True
    else:
        return False


two_count = 0
three_count = 0
with open("input/day2_in.txt") as file:
    for line in file:
        if id_contains_multiple(line, 2):
            two_count += 1
        if id_contains_multiple(line, 3):
            three_count += 1

result = two_count * three_count
print(f'Part 1: {result}')


# Part 2


def id_different_char(id_str1: str, id_str2: str) -> int:
    compare_words = zip(id_str1, id_str2)
    diff_count = len([a for a, b in compare_words if a != b])
    return diff_count


def id_same_chars(id_str1: str, id_str2: str) -> str:
    compare_words = zip(id_str1, id_str2)
    same_chars = [a for a, b in compare_words if a == b]
    return ''.join(same_chars)


ids = []
with open("input/day2_in.txt") as file:
    for line in file:
        ids.append(line)

match_found = False
for current_box_id in ids:
    for comp_box_id in ids:
        if id_different_char(current_box_id, comp_box_id) == 1:
            print(f"Found match: {current_box_id}, {comp_box_id}")
            match_found = True
            break
    if match_found:
        break

result = id_same_chars(current_box_id, comp_box_id)
print(f'result: {result}')
print('done')
