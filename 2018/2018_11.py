import numpy as np

serial_number = 9110
grid = np.zeros((300, 300), np.int32)

for index, data in np.ndenumerate(grid):
    x_addr = index[0] + 1
    y_addr = index[1] + 1
    rack_id = x_addr + 10
    power_level = rack_id * y_addr + serial_number
    power_level *= rack_id
    # get the 100's digit only
    power_level = int(power_level / 100) % 10
    power_level -= 5
    grid[index[0]][index[1]] = power_level

largest_power = -999999
largest_xy = None
for index, data in np.ndenumerate(grid):
    if index[0] < 298 and index[1] < 298:
        fuelcell = grid[index[0]:index[0] + 3, index[1]:index[1] + 3]
        power = np.sum(fuelcell)
        if power > largest_power:
            largest_power = power
            largest_xy = (index[0] + 1, index[1] + 1)

print(f'Part 1: {largest_xy}')

largest_power = -999999
largest_xys = None

for size in np.arange(1, 301):
    print(f'size: {size}')
    for index, data in np.ndenumerate(grid):
        if index[0] < (301 - size) and index[1] < (301 - size):
            fuelcell = grid[index[0]:index[0] + size, index[1]:index[1] + size]
            power = np.sum(fuelcell)
            if power > largest_power:
                largest_power = power
                largest_xys = (index[0] + 1, index[1] + 1, size)

print(f'Part 2: {largest_xys}')
print('done')
