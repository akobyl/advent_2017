INPUT = 'hwlqcszp'


def generate_hash(input_str):
    circ_list = list(range(256))
    INPUT_SUFFIX = [17, 31, 73, 47, 23]
    input = []
    for char in input_str:
        input.append(ord(char))

    input += INPUT_SUFFIX
    list_position = 0
    skip_size = 0

    for loop in range(64):
        for length in input:
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

    # calculate dense hash by XOR operations
    dense_hash = []
    for loc, element in enumerate(circ_list):
        dense_id = int(loc / 16)
        if loc % 16 == 0:
            dense_hash.append(element)
        else:
            dense_hash[dense_id] ^= element

    return dense_hash


used_squares = 0
for i in range(128):
    string = '{}-{}'.format(INPUT, i)
    output = generate_hash(string)

    used_squares += ('{:08b}' * 16).format(*output).count('1')

print('-------\npart 1')
print(used_squares)

print('-------\npart 2')
memory = []
for i in range(128):
    string = '{}-{}'.format(INPUT, i)
    output = generate_hash(string)

    memory.append([i for i in ('{:08b}' * 16).format(*output)])


def flood_fill(x, y, match_id, fill_id, increment_id):
    if x < 0 or x >= len(memory):
        return False
    if y < 0 or y >= len(memory[0]):
        return False
    if memory[x][y] != match_id:
        return False

    fill_txt = str(fill_id)
    memory[x][y] = fill_txt

    flood_fill(x + 1, y, match_id, fill_id, False)
    flood_fill(x - 1, y, match_id, fill_id, False)
    flood_fill(x, y + 1, match_id, fill_id, False)
    flood_fill(x, y - 1, match_id, fill_id, False)

    return True


region_count = 0
fill_id = 2
fill_regions = 0
for x in range(len(memory)):
    for y in range(len(memory[0])):
        if flood_fill(x, y, '1', fill_id, True):
            fill_id += 1
            fill_regions += 1

print(fill_regions)
