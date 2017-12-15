checksum = 0

with open('input/day2_in.txt') as file:
    for line in file:
        data = line.split('\t')
        data = [int(i) for i in data]
        data_min = min(data)
        data_max = max(data)
        print("data: {}, min: {}, max: {}".format(data, data_min, data_max))
        row_checksum = data_max - data_min
        checksum += row_checksum

print(checksum)
