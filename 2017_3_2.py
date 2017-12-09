INPUT = 12
current_sum = 1

last_ring = [1]
current_ring = []
ring_width = 1

ring_id = 0

while INPUT > current_sum:
    ring_id += 1
    ring_count = ring_width * 4 + 4
    ring_width += 2
    current_ring = []
    current_loc = 0
    while current_loc < ring_count:

        current_loc += 1
