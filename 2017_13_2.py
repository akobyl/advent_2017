import copy

layers = []
original_layers = []
current_range = -1

# layers: [layer range, depth, scanner location, scanner going down (true) or up (false)]
with open('day13_in.txt') as file:
    for line in file:
        input_range = int(line[:line.find(':')])
        input_depth = int(line[(line.find(':') + 1):])

        current_range += 1
        while current_range < input_range:
            original_layers.append([current_range, 0, None, None])
            current_range += 1

        original_layers.append([current_range, input_depth, 0, True])


def increment_scanner():
    for layer in layers:
        layer_range = layer[0]
        layer_depth = layer[1]
        scan_loc = layer[2]
        scan_down = layer[3]

        if scan_loc is not None:
            if scan_down:
                if (scan_loc + 1) < layer_depth:
                    layer[2] += 1
                else:
                    scan_loc -= 1
                    layer[2] -= 1
                    layer[3] = False
            else:
                if (scan_loc - 1) >= 0:
                    layer[2] -= 1
                else:
                    layer[2] += 1
                    layer[3] = True


hit_by_scanner = True
delay = -1
while hit_by_scanner:
    layers = copy.deepcopy(original_layers[:])
    delay += 1
    hit_by_scanner = False
    packet_loc = -1
    # print('running loop {}'.format(delay))
    # print(layers)

    for i in range(delay):
        increment_scanner()

    for t in range(len(layers)):
        packet_loc += 1
        if layers[packet_loc][2] == 0:
            hit_by_scanner = True
            # print('hit by scanner {}'.format(layers[packet_loc]))
            break
        increment_scanner()

print('-----\npart 2')
print(delay)
