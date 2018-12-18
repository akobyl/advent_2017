plant_padding = 10
plants = [False] * plant_padding
rules = []
generation_count = 20

with open('input/day12_in.txt') as file:
    # with open('input/day12_test.txt') as file:
    initial_str = file.readline().rstrip().split(' ')[2]
    for c in initial_str:
        if c is '.':
            plants.append(False)
        elif c is '#':
            plants.append(True)
        else:
            assert True, "unexpected character"
    plants += [False] * plant_padding

    file.readline()
    for line in file:
        rule_strs = line.rstrip().split(' ')
        rule_compare = []
        for c in rule_strs[0]:
            if c is '.':
                rule_compare.append(False)
            elif c is '#':
                rule_compare.append(True)
            else:
                assert True, "unexpected character"

        if rule_strs[2] is '.':
            rule_output = False
        elif rule_strs[2] is '#':
            rule_output = True
        else:
            assert True, "unexpected character"

        rules.append([rule_compare, rule_output])

part2_plants = plants
generation = 0
offset = 0

for generation in range(generation_count):
    # out_str = ''.join(['#' if p else '.' for p in plants])
    # print(f'{generation}: {out_str}')

    new_generation = [False] * 2
    for index, plant in enumerate(plants):
        if (len(plants) - 2) > index > 1:
            plant_neighborhood = plants[index - 2:index + 3]
            for rule in rules:
                if plant_neighborhood == rule[0]:
                    new_generation.append(rule[1])
                    break
    new_generation += [False] * 2
    plants = new_generation
    if True not in plants[:3]:
        plants.pop(0)
        offset += 1
    if True in plants[-5:]:
        plants += [False]

score = 0
for index, plant in enumerate(plants):
    if plant:
        score += offset + index - plant_padding
print(f'Part 1: {score}')


plants = part2_plants
generation = 0
offset = 0
final_generation = 50000000000
# final_generation = generation_count

for generation in range(final_generation):

    new_generation = [False] * 2
    for index, plant in enumerate(plants):
        if (len(plants) - 2) > index > 1:
            plant_neighborhood = plants[index - 2:index + 3]
            for rule in rules:
                if plant_neighborhood == rule[0]:
                    new_generation.append(rule[1])
                    break
    new_generation += [False] * 2
    last_generation = plants
    plants = new_generation
    if True not in plants[:3]:
        plants.pop(0)
        offset += 1
    if True in plants[-5:]:
        plants += [False]

    out_str = ''.join(['#' if p else '.' for p in plants])
    print(f'{generation} ({offset}): {out_str}')

    # final_offset = offset

    if plants == last_generation:
        print(f'final pattern found: {generation}')
        final_offset = offset + final_generation - generation - 1
        break
    else:
        final_offset = offset


score = 0
for index, plant in enumerate(plants):
    if plant:
        p_score = final_offset + index - plant_padding
        score += p_score
        # score += final_offset + index - plant_padding
print(f'Part 2: {score}')




print('done')
