freq_list = []

with open('input/day1_in.txt') as file:
    for line in file:
        freq_list.append(int(line))

match_found = False
sum_list = [0]
sum = 0
freq_location = 0

while not match_found:
    sum = sum_list[-1] + freq_list[freq_location % len(freq_list)]

    if sum in sum_list:
        print(f'Found a match: {sum}')
        match_found = True
    else:
        sum_list.append(sum)
        freq_location += 1

print("done")
