grid = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
rules = []

with open('input/day21_in.txt') as file:
    for line in file:
        inputs = line.split(' ')
        in_pattern = [list(x) for x in inputs[0].replace('.', '0').replace('#', '1').rstrip().split('/')]
        new_in = []
        for row in in_pattern:
            new_in.append([int(x) for x in row])
        out_pattern = [list(x) for x in inputs[2].replace('.', '0').replace('#', '1').rstrip().split('/')]
        new_out = []
        for row in out_pattern:
            new_out.append([int(x) for x in row])
        size = len(new_in)
        rules.append((size, new_in, new_out))


def print_grid():
    for row in grid:
        row_str = ''.join([str(x) for x in row]).replace('0', '.').replace('1', '#')
        print(row_str)


two_rules = [x for x in rules if x[0] == 2]
three_rules = [x for x in rules if x[0] == 3]


def rotate_grid(size, grid):
    if size == 2:
        return [[grid[1][0], grid[0][0]],
                [grid[1][1], grid[0][1]]]
    elif size == 3:
        return [[grid[1][0], grid[0][0], grid[0][1]],
                [grid[2][0], grid[1][1], grid[0][2]],
                [grid[2][1], grid[2][2], grid[1][2]]]


def find_match(size, input_grid):
    if size == 2:
        rules = two_rules
    elif size == 3:
        rules = three_rules
    else:
        raise AssertionError('bad size {}'.format(size))
    for rule in rules:
        if input_grid == rule[1]:
            return rule[2]
        # rotate
        for rotation in range(4):
            input_grid = rotate_grid(size, input_grid)
            if input_grid == rule[1]:
                return rule[2]

        # flip then rotate again
        input_grid = [x[::-1] for x in input_grid]
        if input_grid == rule[1]:
            return rule[2]
        # rotate
        for rotation in range(4):
            input_grid = rotate_grid(size, input_grid)
            if input_grid == rule[1]:
                return rule[2]
        # flip back... then flip vertical
        input_grid = [x[::-1] for x in input_grid]
        input_grid = input_grid[::-1]

        if input_grid == rule[1]:
            return rule[2]
        # rotate
        for rotation in range(4):
            input_grid = rotate_grid(size, input_grid)
            if input_grid == rule[1]:
                return rule[2]

    print(input_grid)
    raise AssertionError('no match found')


for i in range(18):
    print('-----')
    size = len(grid)
    if size % 2 == 0:
        grid_size = int((size / 2) * 3)
        new_grid = [[0 for x in range(grid_size)] for x in range(grid_size)]
        for row in range(int(size / 2)):
            row_offset = row * 2
            for col in range(int(size / 2)):
                col_offset = col * 2
                sub_grid = [grid[row_offset][col_offset:col_offset + 2]]
                sub_grid.append(grid[row_offset + 1][col_offset:col_offset + 2])
                new_row = row * 3
                new_col = col * 3
                new_sub_grid = find_match(2, sub_grid)
                new_grid[new_row][new_col:new_col + 3] = new_sub_grid[0][:]
                new_grid[new_row + 1][new_col:new_col + 3] = new_sub_grid[1][:]
                new_grid[new_row + 2][new_col:new_col + 3] = new_sub_grid[2][:]
    elif size % 3 == 0:
        grid_size = int((size / 3) * 4)
        new_grid = [[0 for x in range(grid_size)] for x in range(grid_size)]
        for row in range(int(size / 3)):
            row_offset = row * 3
            for col in range(int(size / 3)):
                col_offset = col * 3
                sub_grid = [grid[row_offset][col_offset:col_offset + 3]]
                sub_grid.append(grid[row_offset + 1][col_offset:col_offset + 3])
                sub_grid.append(grid[row_offset + 2][col_offset:col_offset + 3])
                new_row = row * 4
                new_col = col * 4
                new_sub_grid = find_match(3, sub_grid)
                new_grid[new_row][new_col:new_col + 4] = new_sub_grid[0][:]
                new_grid[new_row + 1][new_col:new_col + 4] = new_sub_grid[1][:]
                new_grid[new_row + 2][new_col:new_col + 4] = new_sub_grid[2][:]
                new_grid[new_row + 3][new_col:new_col + 4] = new_sub_grid[3][:]
    else:
        raise AssertionError('Size does not divide 2 or 3...')
    grid = new_grid
    print('step {}'.format(i + 1))
    print_grid()

print('----\npart 1')
sum = 0
for row in grid:
    sum += row.count(1)

print(sum)
