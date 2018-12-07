class Step(object):

    def __init__(self, name):
        self.name = name
        self.predecessors = []
        self.completed = False
        self.predecessors_completed = False
        self.time_to_complete = 61 + int(ord(name) - ord('A'))
        self.start_time = 0
        self.finish_time = 0

    def __eq__(self, other):
        if other:
            if other.name == self.name:
                return True
        return False

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name

    def add_predecessor(self, add_pred_step):
        self.predecessors.append(add_pred_step)

    def are_predecessors_complete(self):
        complete = True
        for pre_step in self.predecessors:
            if not pre_step.completed:
                complete = False
        return complete

    def update_predecessors_complete(self):
        complete = True
        for pre_step in self.predecessors:
            if not pre_step.completed:
                complete = False
        self.predecessors_completed = complete


steps = []
with open('input/day7_in.txt') as file:
    for line in file:
        pred = line.split(' ')[1]
        step = line.split(' ')[7]

        new_step = Step(step)
        new_pred_step = Step(pred)

        if new_step not in steps:
            steps.append(new_step)
        step = steps[steps.index(new_step)]

        if new_pred_step not in steps:
            steps.append(new_pred_step)
        pred_step = steps[steps.index(new_pred_step)]

        step.add_predecessor(pred_step)

all_done = False
step_order = ''
while not all_done:
    # get current available steps
    available_steps = []
    for step in steps:
        step.update_predecessors_complete()
        if step.predecessors_completed and not step.completed:
            available_steps.append(step)

    if len(available_steps) == 0:
        all_done = True
    else:
        available_steps.sort()
        available_steps[0].completed = True
        step_order += available_steps[0].name
        # print(available_steps)

print(f'Part 1: {step_order}')

# reset for part 2
for step in steps:
    step.predecessors_completed = False
    step.completed = False

ELVES_COUNT = 7
timer = 0
all_done = False
working = 0
notworking = 0

steps_in_progress = [None] * ELVES_COUNT
completed_steps = []
while not all_done:
    # see if any steps are complete
    for step in steps_in_progress:
        if step:
            if timer >= step.finish_time:
                completed_steps.append(steps_in_progress[steps_in_progress.index(step)])
                steps_in_progress[steps_in_progress.index(step)] = None
                step.completed = True
                # print(f'Step {step.name} completed at {timer}')

    # get current available steps
    available_steps = []
    all_done = True
    for step in steps:
        step.update_predecessors_complete()
        if step.predecessors_completed and not step.completed and step not in steps_in_progress:
            available_steps.append(step)
        if not step.completed:
            all_done = False
    available_steps.sort()

    # assign available steps to free workers
    while None in steps_in_progress and len(available_steps) > 0:
        steps_in_progress[steps_in_progress.index(None)] = available_steps[0]
        available_steps[0].start_time = timer
        available_steps[0].finish_time = timer + available_steps[0].time_to_complete
        # print(f'Started work on step {available_steps[0].name} at {timer}')
        available_steps.pop(0)

    print_str = ''
    for step in steps_in_progress:
        if step:
            print_str += f'{step.name}'
            working += 1
        else:
            print_str += '.'
            notworking += 1
    print(print_str)
    timer += 1

notworking -= ELVES_COUNT

print(f'Part 2: {timer - 1}')

print(f'Efficiency: {100.0 * working / (notworking + working)}')
