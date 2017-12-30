grid = [[0, 1, 0], [0, 0, 0], [1, 1, 1]]
rules = []

with open('input/day21_test.txt') as file:
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

for i in range(5):
    print('-----')
    size = len(grid)
    if size % 2 == 0:
        new_grid = [[0] * int((size / 2) * 3)] * int((size / 2) * 3)
        for row in range(int(size / 2)):
            for col in range(int(size / 2)):
                pass
    elif size % 3 == 0:
        new_grid = [[0] * int((size / 3) * 4)] * int((size / 3) * 4)
        for row in range(int(size / 3)):
            for col in range(int(size / 3)):

    else:
        raise AssertionError('Size does not divide 2 or 3...')
    print_grid()
