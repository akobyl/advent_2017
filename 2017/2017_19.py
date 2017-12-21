class Point(object):
    letter = None
    vertical = False
    horizontal = False


UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

map = []
with open('input/day19_in.txt') as file:
    for line in file:
        map.append(list(line.replace('\n', '')))

y = 0
x = map[y].index('|')
direction = DOWN

letters = []
map_chars = ['|', '-', '+', ' ']
steps = 0

while map[y][x] != ' ':
    steps += 1
    if direction == DOWN:
        y += 1
    elif direction == UP:
        y -= 1
    elif direction == RIGHT:
        x += 1
    elif direction == LEFT:
        x -= 1

    current = map[y][x]

    if current not in map_chars:
        letters.append(current)

    if (direction == DOWN) or (direction == UP):
        if current == '+':
            if map[y][x + 1] == '-':
                direction = RIGHT
            elif map[y][x - 1] == '-':
                direction = LEFT
            else:
                raise AssertionError('bad +!')
    elif (direction == LEFT) or (direction == RIGHT):
        if current == '+':
            if map[y + 1][x] == '|':
                direction = DOWN
            elif map[y - 1][x] == '|':
                direction = UP
            else:
                raise AssertionError('bad +!')


print('-----\npart1')
print(letters)

print('-----\npart2')
print(steps)
