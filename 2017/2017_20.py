class Point(object):
    acceleration = [0,0,0]

points = []  # type: List(Point)
with open('input/day20_in.txt') as file:
    for line in file:
        points.append(Point())
        accel = [int(i) for i in line[line.find('a') + 3:-2].split(',')]
        points[-1].acceleration = accel


print('-----\npart 1')

lowest_accel = 10000000000000
for i, point in enumerate(points):
    accel = pow(pow(point.acceleration[0], 2) + pow(point.acceleration[1], 2) + pow(point.acceleration[2], 2), 0.5)
    if accel < lowest_accel:
        lowest_accel = accel
        print('new lowest!!: {}'.format(i))
