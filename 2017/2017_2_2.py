checksum = 0

with open('input/day2_in.txt') as file:
    for line in file:
        data = line.split('\t')
        data = [int(i) for i in data]

        dividers_found = False
        while not dividers_found:
            for loc1, d1 in enumerate(data):
                for loc2, d2 in enumerate(data):
                    result = d1 / d2
                    if result - int(result) == 0 and loc1 != loc2:
                        print('Dividers found: {}/{}'.format(d1,d2))
                        checksum += result
                        dividers_found = True


print(checksum)
