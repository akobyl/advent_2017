from collections import deque

skip = 386

buffer = deque([0])

i = 0
list_loc = 0

while i < 50000000:
    i += 1
    buffer.rotate(-skip)
    buffer.append(i)
    if (i % 100000) == 0:
        print(i)

index = buffer.index(0)
print(buffer[index + 1])
