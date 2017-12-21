instructions = []
with open('input/day18_in.txt') as file:
    for line in file:
        instructions.append(line.rstrip().split(' '))


def get_register(registers_dict, reg):
    if reg not in registers_dict:
        registers_dict[reg] = 0

    return registers_dict[reg]


def get_int_or_reg_val(registers_dict, in_str):
    try:
        val = int(in_str)
    except ValueError:
        val = get_register(registers_dict, in_str)
    return val


registers = {}
sounds = []
recover = 0
pc = 0
while pc < len(instructions):
    instruction = instructions[pc]
    cmd = instruction[0]
    cmd_reg = instruction[1]

    if cmd == 'snd':
        sounds.append(get_register(registers, cmd_reg))
        pc += 1
    elif cmd == 'set':
        registers[cmd_reg] = get_int_or_reg_val(registers, instruction[2])
        pc += 1
    elif cmd == 'add':
        registers[cmd_reg] = get_register(registers, cmd_reg) + get_int_or_reg_val(registers, instruction[2])
        pc += 1
    elif cmd == 'mul':
        registers[cmd_reg] = get_register(registers, cmd_reg) * get_int_or_reg_val(registers, instruction[2])
        pc += 1
    elif cmd == 'mod':
        registers[cmd_reg] = get_register(registers, cmd_reg) % get_int_or_reg_val(registers, instruction[2])
        pc += 1
    elif cmd == 'rcv':
        if get_register(registers, cmd_reg) != 0:
            recover = sounds[-1]
            break
        pc += 1
    elif cmd == 'jgz':
        if get_register(registers, cmd_reg) > 0:
            pc += int(instruction[2])
        else:
            pc += 1

print('-----\npart 1')
print(recover)
