INPUT = 289326

print('Solving puzzle 2017 day 3 part 1!')

# get ring ID
ring_id = 0
ring_start = 2
ring_width = 1
last_ring_start = 2

while INPUT > ring_start:
    ring_id += 1
    # the number of elements increments 1,3,5 plus 4 corners
    ring_count = ring_width * 4 + 4

    print('ring id: {}, first: {}, count: {}'.format(ring_id, ring_start, ring_count))
    last_ring_start = ring_start
    ring_start += ring_count
    ring_width += 2

print('{} is in ring id {}'.format(INPUT, ring_id))

# find the location of the element in the ring.  The first element is always the bottom right up 1
# Find the # of steps to the x or y center of the ring
max_offset = int((ring_width - 1) / 2)
print('ring width: {}, max offset: {}'.format(ring_width, max_offset))

# create list of offsets, starting at max offset - 1
offset = max_offset - 1
num = last_ring_start
rising = False

print('starting offset finding. input: {} start: {}'.format(INPUT, num))
while INPUT > num:
    if rising:
        offset += 1
        if offset == max_offset:
            rising = False
    else:
        offset -= 1
        if offset == 0:
            rising = True
    num += 1
    print('number: {}, rising: {}, offset: {}'.format(num, rising, offset))

print('offset: {}'.format(offset))
print('ring id: {}'.format(ring_id))

print('solution: \n{}'.format(offset + ring_id))