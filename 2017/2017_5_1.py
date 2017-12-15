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
    list[old_position] += 1
    jumps += 1
    print('jumped from {} to {}'.format(old_position, position))

    if position >= list_len:
        escaped = True
        print('escaped!!')

print('-----')
print(jumps)
