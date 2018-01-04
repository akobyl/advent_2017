from collections import deque

steps = 12481997
tape = [0] * steps
tape = deque(tape)


state = 'A'
# rotate to right: -1, left: 1

for i in range(steps):
    val = tape[0]
    if state == 'A':
        if val == 0:
            tape[0] = 1
            tape.rotate(-1)
            state = 'B'
        else:
            tape[0] = 0
            tape.rotate(1)
            state = 'C'
    elif state == 'B':
        if val == 0:
            tape[0] = 1
            tape.rotate(1)
            state = 'A'
        else:
            tape[0] = 1
            tape.rotate(-1)
            state = 'D'
    elif state == 'C':
        if val == 0:
            tape[0] = 0
            tape.rotate(1)
            state = 'B'
        else:
            tape[0] = 0
            tape.rotate(1)
            state = 'E'
    elif state == 'D':
        if val == 0:
            tape[0] = 1
            tape.rotate(-1)
            state = 'A'
        else:
            tape[0] = 0
            tape.rotate(-1)
            state = 'B'
    elif state == 'E':
        if val == 0:
            tape[0] = 1
            tape.rotate(1)
            state = 'F'
        else:
            tape[0] = 1
            tape.rotate(1)
            state = 'C'
    elif state == 'F':
        if val == 0:
            tape[0] = 1
            tape.rotate(-1)
            state = 'D'
        else:
            tape[0] = 1
            tape.rotate(-1)
            state = 'A'
    else:
        raise Exception('bad state!')


print(sum(tape))