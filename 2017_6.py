# INPUT = '0\t2\t7\t0'
INPUT = '14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4'

banks = [int(i) for i in INPUT.split('\t')]
print(banks)

match_found = False
results = []
cycles = 0

while not match_found:
    max_value = max(banks)
    max_loc = banks.index(max_value)
    cycles += 1

    # print('------')
    print('\ncycle: {}'.format(cycles))
    # print(' banks: {}'.format(banks))
    # print('max value: {} loc: {}'.format(max_value, max_loc))

    banks[max_loc] = 0
    while max_value != 0:
        position = (max_loc + 1) % len(banks)
        banks[position] += 1
        max_value -= 1
        max_loc += 1

    # print('distributed banks: {}'.format(banks))
    # print('results is now: {}'.format(results))

    for result in results:
        if banks == result:
            match_found = True
            print('match found!')

    # must copy list by value not reference
    results.append(banks[:])

print('------')
print(cycles)


# part 2
cycles = [i for i, result in enumerate(results) if result == banks]
print(cycles[1] - cycles[0])
