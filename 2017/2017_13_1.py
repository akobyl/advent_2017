layers = []
current_range = -1

# layers: [layer range, depth, scanner location, scanner going down (true) or up (false)]
with open('input/day13_in.txt') as file:
    for line in file:
        input_range = int(line[:line.find(':')])
        input_depth = int(line[(line.find(':') + 1):])

        current_range += 1
        while current_range < input_range:
            layers.append([current_range, 0, None, None])
            current_range += 1

        layers.append([current_range, input_depth, 0, True])


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

packet_loc = -1
severity = 0
for t in range(len(layers)):
    packet_loc += 1
    if layers[packet_loc][2] == 0:
        severity += layers[packet_loc][0]*layers[packet_loc][1]
    increment_scanner()

print('-----\npart 1')
print(severity)
