with open('input/day8_in.txt') as file:
    numbers = file.readline().split(' ')

# numbers = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split(' ')
numbers = [int(i) for i in numbers]


class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.children_count = 0
        self.metadata = []
        self.metadata_len = 0

    def __repr__(self):
        return self.name

    def calculate_value(self):
        if self.children_count == 0:
            value = sum(self.metadata)
        else:
            value = 0
            for addr in self.metadata:
                if self.children_count >= addr > 0:
                    value += self.children[addr - 1].calculate_value()
        return value


CHILD_COUNT = 1
METADATA_COUNT = 2
METADATA_READ = 3

node_list = []
state_current = CHILD_COUNT
node_stack = []
metadata_sum = 0

for number in numbers:
    if state_current == CHILD_COUNT:
        new_node = Node(f'node{len(node_list)}')
        # new_node = Node(chr(ord('A') + len(node_list)))
        new_node.children_count = number

        if len(node_stack) > 0:
            node_stack[-1].children.append(new_node)
        node_list.append(new_node)
        node_stack.append(new_node)

        state_current = METADATA_COUNT

    elif state_current == METADATA_COUNT:
        assert number >= 1, "meta data len == 0"
        node_stack[-1].metadata_len = number

        # read any child nodes...
        if node_stack[-1].children_count > 0:
            state_current = CHILD_COUNT
        else:
            state_current = METADATA_READ

    elif state_current == METADATA_READ:
        node_stack[-1].metadata.append(number)
        metadata_sum += number

        if len(node_stack[-1].metadata) == node_stack[-1].metadata_len:
            # need to think about this transition...
            if len(node_stack) > 1:
                if len(node_stack[-2].children) == node_stack[-2].children_count:
                    state_current = METADATA_READ
                else:
                    state_current = CHILD_COUNT

            node_stack.pop(-1)
    else:
        assert True, "unknown parse state"
print(f'Part 1: {metadata_sum}')

result2 = node_list[0].calculate_value()

print(f'Part 2: {result2}')

print('done')
