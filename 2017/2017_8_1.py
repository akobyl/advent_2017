registers = {}
max_value_ever = 0

with open('input/day8_in.txt') as file:
    for line in file:
        print(line.rstrip())
        instruction = line.rstrip().split(' ')
        target_register = instruction[0]
        command = instruction[1]
        command_count = int(instruction[2])

        query_register = instruction[4]
        query_comparison = instruction[5]
        query_count = int(instruction[6])

        # make sure query and command registers exist
        if target_register not in registers:
            registers[target_register] = 0

        if query_register not in registers:
            registers[query_register] = 0

        condition = False
        if query_comparison == '>':
            if registers[query_register] > query_count:
                condition = True
        elif query_comparison == '<':
            if registers[query_register] < query_count:
                condition = True
        elif query_comparison == '<=':
            if registers[query_register] <= query_count:
                condition = True
        elif query_comparison == '>=':
            if registers[query_register] >= query_count:
                condition = True
        elif query_comparison == '==':
            if registers[query_register] == query_count:
                condition = True
        elif query_comparison == '!=':
            if registers[query_register] != query_count:
                condition = True
        else:
            raise AssertionError

        old_val = registers[target_register]
        if condition:
            if command == 'inc':
                registers[target_register] += command_count
            elif command == 'dec':
                registers[target_register] -= command_count
            else:
                raise AssertionError

            if registers[target_register] > max_value_ever:
                max_value_ever = registers[target_register]

        print('register {}: {} -> {}'.format(target_register, old_val, registers[target_register]))

# find largest value
print(registers)
max_register = max([v for k, v in registers.items()])
print('--------')
print('part 1')
print(max_register)

print('------')
print('part 2')
print(max_value_ever)