jumps = 0
list = []

with open('input/day5_in.txt') as file:
    for line in file:
        list.append(int(line))

list_len = len(list)
position = 0
escaped = False

while not escaped:
    old_position = position
    position += list[position]
    if list[old_position] >= 3:
        list[old_position] -= 1
    else:
        list[old_position] += 1

    jumps += 1
    # this takes too long to print!
    # print('jumped from {} to {}'.format(old_position, position))

    if position >= list_len:
        escaped = True
        print('escaped!!')

print('-----')
print(jumps)
