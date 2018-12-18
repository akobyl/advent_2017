from copy import deepcopy

map_size = 50
map = []
with open('input/day18_in.txt') as file:
    for row in file:
        map.append(list(row.rstrip()))


def get_surrounding_acres(x, y):
    surrounding = []

    a = x - 1
    b = y - 1
    if map_size > a >= 0 and map_size > b >= 0:
        surrounding.append(map[b][a])
    a = x
    b = y - 1
    if map_size > a >= 0 and map_size > b >= 0:
        surrounding.append(map[b][a])
    a = x + 1
    b = y - 1
    if map_size > a >= 0 and map_size > b >= 0:
        surrounding.append(map[b][a])
    a = x - 1
    b = y + 1
    if map_size > a >= 0 and map_size > b >= 0:
        surrounding.append(map[b][a])
    a = x + 1
    b = y + 1
    if map_size > a >= 0 and map_size > b >= 0:
        surrounding.append(map[b][a])
    a = x
    b = y + 1
    if map_size > a >= 0 and map_size > b >= 0:
        surrounding.append(map[b][a])
    a = x - 1
    b = y
    if map_size > a >= 0 and map_size > b >= 0:
        surrounding.append(map[b][a])
    a = x + 1
    b = y
    if map_size > a >= 0 and map_size > b >= 0:
        surrounding.append(map[b][a])

    open_count = len([c for c in surrounding if c == '.'])
    tree_count = len([c for c in surrounding if c == '|'])
    lumberyard_count = len([c for c in surrounding if c == '#'])

    return open_count, tree_count, lumberyard_count

minute = 0
last_total_trees = 0
last_total_lumberyards = 0

while minute < 1000:
    new_map = []
    for y, row in enumerate(map):
        new_row = list(row)
        for x, acre in enumerate(row):
            open_count, tree_count, lumberyard_count = get_surrounding_acres(x, y)

            if acre == '.':
                if tree_count >= 3:
                    new_row[x] = '|'

            elif acre == '|':
                if lumberyard_count >= 3:
                    new_row[x] = '#'
            elif acre == '#':
                if lumberyard_count >= 1 and tree_count >= 1:
                    pass
                else:
                    new_row[x] = '.'
        new_map.append(new_row)
    minute += 1

    map = deepcopy(new_map)
    with open('day18_out.txt', 'a') as outfile:
        outfile.write(f'minute {minute}\n')
        for row in map:
            outfile.write(''.join(row) + '\n')
    print(f'minute {minute}')
    # for row in map:
    #     print(''.join(row))


total_trees = 0
total_lumberyards = 0

for row in map:
    total_trees += len([c for c in row if c == '|'])
    total_lumberyards += len([c for c in row if c == '#'])

result1 = total_trees * total_lumberyards
print(f'Part 1: {result1}')
print('done')
