with open('input/day11_in.txt') as file:
    INPUT = file.read().rstrip()

steps = INPUT.split(',')

class HexCube(object):
    """
    Hex cube inspired by blog post: https://www.redblobgames.com/grids/hexagons/
    """
    x = 0
    y = 0
    z = 0

    def move_direction(self, move):
        if move == 'n':
            self.y += 1
            self.z -= 1
        elif move == 'ne':
            self.x += 1
            self.z -= 1
        elif move == 'se':
            self.x += 1
            self.y -= 1
        elif move == 's':
            self.y -= 1
            self.z += 1
        elif move == 'sw':
            self.x -= 1
            self.z += 1
        elif move == 'nw':
            self.x -= 1
            self.y += 1
        else:
            raise AssertionError('unknown direction')

    def print_coordinates(self):
        print('({}, {}, {})'.format(self.x, self.y, self.z))

    def distance_to_origin(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) / 2

hc = HexCube()

max_distance = 0

for step in steps:
    hc.move_direction(step)
    if hc.distance_to_origin() > max_distance:
        max_distance = hc.distance_to_origin()

print('-----\npart1')
print(hc.distance_to_origin())

print('-----\npart2')
print(max_distance)
