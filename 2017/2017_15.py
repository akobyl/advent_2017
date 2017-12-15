GenA = 277
GenB = 349

MultA = 16807
MultB = 48271
divider = 2147483647

sum = 0

for i in range(40000000):
    GenA = (GenA * MultA) % divider
    GenB = (GenB * MultB) % divider

    # compare lower 16 bits
    if (GenA & 0xFFFF) == (GenB & 0xFFFF):
        sum += 1

print('-------\npart 1')
print(sum)

GenA = 277
GenB = 349
sum = 0

for i in range(5000000):
    gen_ready = False
    while not gen_ready:
        GenA = (GenA * MultA) % divider
        if GenA % 4 == 0:
            gen_ready = True

    gen_ready = False
    while not gen_ready:
        GenB = (GenB * MultB) % divider
        if GenB % 8 == 0:
            gen_ready = True

    # compare lower 16 bits
    if (GenA & 0xFFFF) == (GenB & 0xFFFF):
        sum += 1

print('-------\npart 2')
print(sum)
