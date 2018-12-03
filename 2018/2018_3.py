# Part 1


fabric_size = 1000
fabric = [[0 for x in range(fabric_size)] for y in range(fabric_size)]

claims = []
# with open('input/day3_test.txt') as file:
with open('input/day3_in.txt') as file:
    for line in file:
        c = line.split(' ')
        claim = {'id': int(c[0][1:])}
        coordinates = c[2].split(',')
        claim['coordinate'] = (int(coordinates[0]), int(coordinates[1][:-1]))
        size = c[3].split('x')
        claim['size'] = (int(size[0]), int(size[1]))

        claims.append(claim)

for claim in claims:
    x = claim['coordinate'][0]
    y = claim['coordinate'][1]
    x_size = claim['size'][0]
    y_size = claim['size'][1]
    for x_pos in range(x_size):
        for y_pos in range(y_size):
            fabric[x + x_pos][y + y_pos] += 1

greater_than_one_list = [j for sublist in fabric for j in sublist if j > 1]
print('Part 1:')
print(len(greater_than_one_list))


print('Part 2')
for claim in claims:
    clean_claim = True
    x = claim['coordinate'][0]
    y = claim['coordinate'][1]
    x_size = claim['size'][0]
    y_size = claim['size'][1]
    for x_pos in range(x_size):
        for y_pos in range(y_size):
            if fabric[x + x_pos][y + y_pos] > 1:
                clean_claim = False

    if clean_claim:
        print(f'Clean claim found: {claim["id"]}')
        break

print('done')
