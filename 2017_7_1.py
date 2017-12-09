class Node(object):
    name = ''  # type: str
    weight = 0  # type: int
    parent = None  # type: Node
    _is_root = False  # type: bool

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return '{} -> {}'.format(self.name, self.parent)


class Tree(object):
    root = None  # type: Node


nodes = []
child_parent = {}

with open('day7_in.txt') as file:
    for line in file:
        line = line.rstrip()
        input = line.split(' ')
        name = input[0]
        weight = int(input[1][1:-1])

        arrow_loc = line.find('->')
        if arrow_loc > 0:
            children_list = line.replace(' ', '')[(arrow_loc):].split(',')
            for child in children_list:
                child_parent[child] = name

        nodes.append(Node(name, weight))

    for child, parent in child_parent.items():
        # attach
        child_node = [x for x in nodes if x.name == child][0]
        parent_node = [x for x in nodes if x.name == parent][0]

        child_node.parent = parent_node
        print(child_node)

# find root
print('-----')
for node in nodes:
    if node.parent is None:
        print(node)
