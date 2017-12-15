INPUT = 289326
current_sum = 1
answer_found = False
last_ring = [1]
current_ring = []
ring_width = 1

ring_id = 1
spiral = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]


def convert_xy_to_spiral(x, y, ring_width):
    center = int(ring_width / 2)
    return center + x, center + y


while not answer_found:
    # create a new ring
    ring_count = ring_width * 4 + 4
    ring_width += 2

    new_spiral = [[0] * (2 + ring_width)]
    for row in spiral:
        new_spiral.append([0, *row, 0])
    new_spiral.append([0] * (2 + ring_width))
    spiral = new_spiral

    # step through ring and add sums
    max_offset = int((ring_width - 1) / 2)
    dx = 0
    dy = 1

    current_x = ring_id
    current_y = -1 * (max_offset - 1)
    for i in range(ring_count):
        x, y = convert_xy_to_spiral(current_x, current_y, ring_width + 2)
        spiral[y][x] += spiral[y][x + 1]
        spiral[y][x] += spiral[y][x - 1]
        spiral[y][x] += spiral[y + 1][x + 1]
        spiral[y][x] += spiral[y + 1][x - 1]
        spiral[y][x] += spiral[y - 1][x + 1]
        spiral[y][x] += spiral[y - 1][x - 1]
        spiral[y][x] += spiral[y + 1][x]
        spiral[y][x] += spiral[y - 1][x]

        current_sum = spiral[y][x]

        if spiral[y][x] >= INPUT and not answer_found:
            print('answer found: {}'.format(spiral[y][x]))
            answer_found = True

        if abs(current_x) == max_offset and dx != 0:
            if dx == 1:
                dy = 1
            elif dx == -1:
                dy = -1

            dx = 0

        elif abs(current_y) == max_offset and dy != 0:
            if dy == 1:
                dx = -1
            elif dy == -1:
                dx = 1

            dy = 0

        current_x += dx
        current_y += dy

    ring_id += 1
