coordinates = {}
x_max = 0
y_max = 0
coordinate_id = 0
with open('input/day6_in.txt') as file:
    for line in file:
        x = int(line.split(',')[0])
        y = int(line.split(',')[1])
        name = f'{coordinate_id}'
        coordinate_id += 1
        size = 0
        on_edge = False
        coordinates[name] = [x, y, size, on_edge]
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y

grid = [[0 for x in range(x_max)] for y in range(y_max)]

for x_pos in range(x_max):
    for y_pos in range(y_max):
        distances = []
        for name, coordinate_info in coordinates.items():
            distance = abs(x_pos - coordinate_info[0]) + abs(y_pos - coordinate_info[1])
            distances.append([name, distance])
        distances.sort(key=lambda dist: dist[1])
        coord_name = distances[0][0]

        if distances[0][1] == distances[1][1]:
            grid[y_pos][x_pos] = None
        else:
            grid[y_pos][x_pos] = coord_name
            coordinates[coord_name][2] += 1

        if x_pos == 0 or x_pos == x_max or y_pos == 0 or y_pos == y_max:
            # set on edge to true
            coordinates[coord_name][3] = True

area_list = []
for name, coordinate in coordinates.items():
    if coordinate[3] == False:
        area_list.append(coordinate[2])

area_list.sort(reverse=True)
print(f'Part 1: {area_list[0]}')

# Fun graphical visualization
from PIL import Image, ImageDraw, ImageColor

cnames = [
    'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 'blue',
    'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk',
    'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkkhaki', 'darkmagenta',
    'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue',
    'darkslategray', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dodgerblue', 'firebrick',
    'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green',
    'greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush',
    'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgreen',
    'lightgray', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightsteelblue',
    'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid',
    'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred',
    'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab',
    'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip',
    'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown',
    'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'snow',
    'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white',
    'whitesmoke', 'yellow', 'yellowgreen']

im = Image.new('RGB', (x_max, y_max))
im_draw = ImageDraw.Draw(im)

for x_pos in range(x_max):
    for y_pos in range(y_max):
        if grid[y_pos][x_pos] == None:
            color = 'black'
        else:
            color = cnames[int(grid[y_pos][x_pos])]
        im_draw.point((x_pos, y_pos), color)

for name, info in coordinates.items():
    im_draw.point((info[0], info[1]), 'black')

im.save('day6_1.png', 'png')

grid2 = [[0 for x in range(x_max)] for y in range(y_max)]
safe_area_size = 0
min_distance = 100000
max_distance = 0
for x_pos in range(x_max):
    for y_pos in range(y_max):
        distances = []
        distance = 0
        for name, coordinate_info in coordinates.items():
            distance += abs(x_pos - coordinate_info[0]) + abs(y_pos - coordinate_info[1])

        grid2[y_pos][x_pos] = distance

        if distance > max_distance:
            max_distance = distance
        if distance < min_distance:
            min_distance = distance
        if distance < 10000:
            safe_area_size += 1

print(f'Part 2: {safe_area_size}')

im = Image.new('RGB', (x_max, y_max))
im_draw = ImageDraw.Draw(im)

for x_pos in range(x_max):
    for y_pos in range(y_max):
        distance = grid2[y_pos][x_pos]
        if distance < 10000:
            color = int((distance - min_distance) * 255 / (10000 - min_distance))
            color = (color, 255, color)
        if distance > 10000:
            color = int(255 - (distance - 10000) * 255 / (max_distance - 10000))
            color = (color, 0, 0)

        if (10000 + 30) > distance > (10000 - 30):
            color = 'yellow'
        im_draw.point((x_pos, y_pos), color)

for name, info in coordinates.items():
    im_draw.point((info[0], info[1]), 'black')

im.save('day6_2.png', 'png')

print('done')
