import numpy

with open('input/day16_in.txt') as file:
    steps = file.read()

steps = steps.rstrip().split(',')
programs = list('abcdefghijklmnop')
programs = numpy.array(programs)

def dance(programs):
    for step in steps:
        if step[0] == 's':
            spin = int(step[1:])
            # programs = programs[-spin:] + programs[:-spin]
            programs = numpy.roll(programs, spin)
        if step[0] == 'x':
            split = step.index('/')
            loc1 = int(step[1:split])
            loc2 = int(step[split+1:])
            programs[loc1], programs[loc2] = programs[loc2], programs[loc1]
        if step[0] == 'p':
            split = step.index('/')
            p1 = step[1:split]
            p2 = step[split+1:]
            loc1 = numpy.where(programs == p1)
            loc2 = numpy.where(programs == p2)
            programs[loc1] = p2
            programs[loc2] = p1
    return programs

print('------\npart1')
print(''.join(programs))

programs = list('abcdefghijklmnop')

outputs = []
print('------\npart2')
for cycles in range(1000000000):
    programs = dance(programs)
    output = ''.join(programs)
    if output in outputs:
        print('found a match {}'.format(cycles))
        break
    outputs.append(output)

remainder = 1000000000 % cycles

programs = list('abcdefghijklmnop')
for i in range(remainder):
    programs = dance(programs)

print(''.join(programs))
