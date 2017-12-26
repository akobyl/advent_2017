import queue
import threading
import time

instructions = []
with open('input/day18_in.txt') as file:
    for line in file:
        instructions.append(line.rstrip().split(' '))


class Duet(object):
    rx_queue = queue.Queue()
    rx_buffer = []
    send_target = None
    tx_queue = None  # type: queue.Queue
    rx_status = False
    status_lock = threading.Lock()

    def __init__(self, pid):
        self.id = pid
        self.registers = {}
        self.registers['p'] = self.id
        self.send_count = 0

    def start(self):
        th1 = threading.Thread(target=self.run_program)
        th1.setDaemon(True)
        th1.start()

    def get_register(self, reg):
        if reg not in self.registers:
            self.registers[reg] = 0

        return self.registers[reg]

    def get_int_or_reg_val(self, in_str):
        try:
            val = int(in_str)
        except ValueError:
            val = self.get_register(in_str)
        return val

    def run_program(self):
        rx_buffer = []
        pc = 0
        while pc < len(instructions):
            instruction = instructions[pc]
            cmd = instruction[0]
            cmd_reg = instruction[1]
            if self.id == 0:
                print('p{}: pc {}: {}'.format(self.id, pc, instruction))

            if cmd == 'snd':
                self.tx_queue.put(self.get_register(cmd_reg))
                self.send_count += 1
                if self.id == 0:
                    print('\tp{} sent {} [{}]'.format(self.id, self.get_int_or_reg_val(cmd_reg), self.send_count))
                pc += 1
            elif cmd == 'set':
                self.registers[cmd_reg] = self.get_int_or_reg_val(instruction[2])
                pc += 1
            elif cmd == 'add':
                self.registers[cmd_reg] = self.get_register(cmd_reg) + self.get_int_or_reg_val(instruction[2])
                pc += 1
            elif cmd == 'mul':
                self.registers[cmd_reg] = self.get_register(cmd_reg) * int(instruction[2])
                pc += 1
            elif cmd == 'mod':
                self.registers[cmd_reg] = self.get_register(cmd_reg) % self.get_int_or_reg_val(instruction[2])
                pc += 1
            elif cmd == 'rcv':
                if self.rx_queue.empty():
                    with self.status_lock:
                        self.rx_status = True
                        print('\tp{} empty rx'.format(self.id))
                self.registers[cmd_reg] = self.rx_queue.get()
                self.rx_buffer.append(self.registers[cmd_reg])
                # print('p{} received {}'.format(self.id, self.rx_buffer[-1]))
                with self.status_lock:
                    self.rx_status = False
                pc += 1
            elif cmd == 'jgz':
                if self.get_register(cmd_reg) > 0:
                    pc += self.get_int_or_reg_val(instruction[2])
                else:
                    pc += 1
            if self.id == 0:
                print('\tp{}reg: {}'.format(self.id, self.registers))

    def get_rx_status(self):
        with self.status_lock:
            return self.rx_status


print('-----\npart 2')

p0 = Duet(0)
p1 = Duet(1)
p0.tx_queue = p1.rx_queue
p1.tx_queue = p0.rx_queue

p0.start()
p1.start()

while (not p1.get_rx_status()) and (not p0.get_rx_status()):
    time.sleep(0.1)

print('p1 send count: {}'.format(p1.send_count))
