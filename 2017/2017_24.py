connections = []

with open('input/day24_in.txt') as file:
    for line in file:
        connections.append((int(line[0:line.find('/')]), int(line.rstrip()[line.find('/') + 1:])))

bridges = []

def find_link(match, available_links, strength, length):
    match_links = []
    for link in available_links:
        if match in link:
            match_links.append(link)

    # print('match {}: {}'.format(match, match_links))
    if len(match_links) == 0:
        bridges.append((strength, length))

    for link in match_links:
        new_length = length + 1
        new_strength = strength + link[0] + link[1]
        available_links_new = available_links[:]
        available_links_new.remove(link)
        # print('\t{} <== {}'.format(link, available_links_new))
        match_index = link.index(match)
        if match_index == 0:
            value = link[1]
        else:
            value = link[0]
        find_link(value, available_links_new, new_strength, new_length)


links = connections[:]
find_link(0, links, 0, 0)

print('--------\npart 1')
strengths = [x[0] for x in bridges]
print(max(strengths))

print('--------\npart 2')
max_length = max([x[1] for x in bridges])
print(max_length)

max_length_bridges = [x for x in bridges if x[1] == max_length]
max_strength = max([x[0] for x in max_length_bridges])
print(max_strength)
