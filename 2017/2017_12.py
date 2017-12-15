groups = []     # type: list[int]
connections = []    # type: list[int]

with open('input/day12_in.txt') as file:
    for line in file:
        program = int(line[:line.find('<')])
        links = [int(i) for i in line[line.find('>') + 1:].split(',')]
        if program not in links:
            links.append(program)
        connections.append(links)

matches_found = True

def any_shared(a, b):
    return any(i in a for i in b)

while matches_found:
    matches_found = False
    for i, connection in enumerate(connections):
        index = connections.index(connection)
        compare_lists = connections[:]
        del compare_lists[i]
        for compare in compare_lists:
            if any_shared(connection, compare):
                matches_found = True
                for element in compare:
                    if element not in connection:
                        connection.append(element)
                index = connections.index(compare)
                # connections.remove(compare)
                del connections[index]

print('-------\npart 1')
for connection in connections:
    if 0 in connection:
        print(connection)
        print(len(connection))
print('-------\npart 2')
print(len(connections))
