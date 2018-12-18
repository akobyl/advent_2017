from itertools import combinations
from copy import deepcopy

map = []
carts = []

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class Cart(object):
    def __init__(self, x, y, dir):
        self.init_x = x
        self.init_y = y
        self.x = x
        self.y = y
        self.dir = dir
        self.turnlist = [LEFT, None, RIGHT]

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __repr__(self):
        if self.dir == UP:
            dir_str = 'UP'
        if self.dir == DOWN:
            dir_str = 'DOWN'
        if self.dir == RIGHT:
            dir_str = 'RIGHT'
        if self.dir == LEFT:
            dir_str = 'LEFT'
        return f'Cart ({self.x},{self.y}) {dir_str}'

    def make_turn(self):
        turn = self.turnlist[0]

        if turn == LEFT:
            self.dir = (self.dir - 1) % 4
        elif turn == RIGHT:
            self.dir = (self.dir + 1) % 4

        # rotate list
        self.turnlist = self.turnlist[1:] + self.turnlist[:1]
        return self.turnlist[-1]


with open('input/day13_in.txt') as file:
    for line in file:
        row = list(line.rstrip())
        for c in row:
            if c is '>':
                carts.append(Cart(row.index(c), len(map), RIGHT))
                row[row.index(c)] = '-'
            if c is '<':
                carts.append(Cart(row.index(c), len(map), LEFT))
                row[row.index(c)] = '-'
            if c is 'v':
                carts.append(Cart(row.index(c), len(map), DOWN))
                row[row.index(c)] = '|'
            if c is '^':
                carts.append(Cart(row.index(c), len(map), UP))
                row[row.index(c)] = '|'

        map.append(row)

accident = False
tick = 0


def print_map():
    printed = ''
    printed_map = deepcopy(map)
    for cart in carts:
        printed_map[cart.y][cart.x] = 'O'

    for idx, row in enumerate(printed_map):
        printed += f'{idx:03}' + ''.join(row) + '\n'

    print(printed)


while not accident:
    tick += 1
    # advance all carts
    for cart in carts:
        if cart.dir == UP:
            cart.y -= 1
        elif cart.dir == DOWN:
            cart.y += 1
        elif cart.dir == RIGHT:
            cart.x += 1
        elif cart.dir == LEFT:
            cart.x -= 1

        track = map[cart.y][cart.x]
        if track == '/':
            if cart.dir == UP:
                cart.dir = RIGHT
            elif cart.dir == DOWN:
                cart.dir = LEFT
            elif cart.dir == LEFT:
                cart.dir = DOWN
            elif cart.dir == RIGHT:
                cart.dir = UP
        if track == '\\':
            if cart.dir == UP:
                cart.dir = LEFT
            elif cart.dir == DOWN:
                cart.dir = RIGHT
            elif cart.dir == LEFT:
                cart.dir = UP
            elif cart.dir == RIGHT:
                cart.dir = DOWN
        if track == '+':
            turn = cart.make_turn()

    for a, b in combinations(carts, 2):
        if a == b:
            print(f'Collision detected @ {tick}: ({a.x},{a.y})')
            accident = True

    # print_map()

print('done')
