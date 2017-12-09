
class Node(object):
    name = ''  # type: str
    weight = 0  # type: int
    parent = None  # type: Node
    _is_root = False  # type: bool
    children = []   # type: list[Node]

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.children = []

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return '{} -> {}'.format(self.name, self.parent)

    def add_child(self, child: 'Node'):
        self.children.append(child)

    def calc_weight_of_children(self):
        weight_sum = self.weight

        for child in self.children:
            # print('adding weight of node {}'.format(child.name))
            weight_sum += child.calc_weight_of_children()

        return weight_sum

    def children_weights(self):
        children_weights = {}

        for child in self.children:
            children_weights[child.name] = child.calc_weight_of_children()

        return children_weights


class Tree(object):
    root = None  # type: Node


nodes = []  # type: list[Node]
child_parent = {}

with open('day7_in.txt') as file:
# with open('day7_test.txt') as file:
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
        parent_node.add_child(child_node)

# find root
print('-----')
root = None # type: Node
for node in nodes:
    if node.parent is None:
        root = node


for node in nodes:
    # print('{}: {} ({})'.format(node.name, [child.name for child in node.children], node.calc_weight_of_children()))
    # print('\t{}'.format(node.list_children_weights()))
    # print('{}: {}'.format(node.name, hex(id(node.children))))

    if node.children:
        children_weights = [v for k, v in node.children_weights().items()]
        all_children_equal = all(x==children_weights[0] for x in children_weights)

        if not all_children_equal:
            print('unbalanced node: {}'.format(node.name))
            # node_children_names = [child.name for child in node.children]
            # node_children_weights = [value for k, value in node.children_weights().items()]
            # print('{} + ({}) = {} + ({})'.format(node.name, node_children_names, node.weight, node_children_weights))

            for c_node in node.children:
                node_children_names = [child.name for child in c_node.children]
                node_children_weights = [value for k, value in c_node.children_weights().items()]
                total = c_node.calc_weight_of_children()
                print('{} + ({}) = {} + ({}) = {}'.format(c_node.name, node_children_names, c_node.weight, node_children_weights, total))
