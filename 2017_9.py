# part 1 tests
INPUT = '{{{}}}'
INPUT = '{{<ab>},{<ab>},{<ab>},{<ab>}}'
INPUT = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
INPUT = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
# part 2 tests
INPUT = '<random characters>'
INPUT = '<!!!>>'
INPUT = '<{o"i!a,<{i<a>'

with open('day9_in.txt') as file:
    INPUT = file.read()

score = 0
current_level = 0
in_garbage = False
skip_next = False
garbage_removed = 0

for c in INPUT:
    if not skip_next:
        if not in_garbage:
            if c == '{':
                current_level += 1
                score += current_level
            if c == '}':
                current_level -= 1
        else:
            if c != '>' and c != '!':
                garbage_removed += 1

        if c == '!':
            skip_next = True
        if c == '<':
            in_garbage = True
        if c == '>':
            in_garbage = False
    else:
        skip_next = False

print('-----\npart 1')
print(score)
print('-----\npart 2')
print(garbage_removed)
