circ_list = list(range(256))
INPUT = [3, 4, 1, 5]
INPUT = [129, 154, 49, 198, 200, 133, 97, 254, 41, 6, 2, 1, 255, 0, 191, 108]

list_position = 0
skip_size = 0
positions = [0, 0]

for length in INPUT:
    if length > 0:
        start = list_position
        end = ((list_position + length) % len(circ_list))

        if start < end:
            swap_list = circ_list[start:end]
        else:
            swap_list = circ_list[start:] + circ_list[:end]

        swap_list.reverse()

        if start < end:
            circ_list[start:end] = swap_list
        else:
            swap_back = swap_list[:(len(circ_list) - start)]
            circ_list[start:] = swap_back

            swap_front = swap_list[(len(circ_list) - start):]

            circ_list[:end] = swap_front

    list_position = (list_position + length + skip_size) % len(circ_list)
    skip_size += 1

print(circ_list)

print('-----\npart 1')
print(circ_list[0] * circ_list[1])
