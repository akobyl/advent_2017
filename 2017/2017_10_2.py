circ_list = list(range(256))
INPUT_SUFFIX = [17,31,73,47,23]
INPUT = '129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108'
input = []
for char in INPUT:
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

print(dense_hash)
print(('{:02x}' * 16).format(*dense_hash))

print('-----\npart 2')
