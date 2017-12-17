skip = 386

buffer = [0]

i = 0
list_loc = 0

while i < 50000000:
    i += 1
    list_loc = (list_loc + skip ) % len(buffer) + 1
    buffer.insert(list_loc, i)
    if (i % 100000) == 0:
        print(i)

index = buffer.index(0)
print(buffer[index + 1])
