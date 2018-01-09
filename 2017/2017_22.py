grid = []
with open('input/day22_in.txt') as file:
    for line in file:
        grid.append([int(x) for x in line.replace('.', '0').replace('#', '1').rstrip()])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

x = int(len(grid) / 2)
y = int(len(grid) / 2)
direction = UP
infections = 0

for i in range(10000):
    if grid[y][x] == 1:
        direction = (direction + 1) % 4
        grid[y][x] = 0
    else:
        direction = (direction - 1) % 4
        grid[y][x] = 1
        infections += 1

    if direction == UP:
        y -= 1
    elif direction == DOWN:
        y += 1
    elif direction == LEFT:
        x -= 1
    elif direction == RIGHT:
        x += 1
    else:
        raise AssertionError('bad direction')

    if x < 0:
        x = 0
        grid = [[0, *row] for row in grid]
    if x == len(grid[0]):
        grid = [[*row, 0] for row in grid]
    if y < 0:
        y = 0
        grid = [[0] * len(grid[0]), *grid]
    if y == len(grid):
        grid = [*grid, [0] * len(grid[0])]

print('-----------\npart 1')
print(infections)
