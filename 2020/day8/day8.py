import re
from pathlib import Path
import copy

class Program():
    def __init__(self,inp):
        self.pos = 0
        self.accumulator = 0
        self.program = inp
        self.ops = {
            'acc' : self.acc,
            'jmp' : self.jump,
            'nop' : self.nop,
        }
        self.seen_position = set()

    def acc(self, num):
        self.accumulator += num
        self.pos += 1

    def jump(self, num):
        self.pos += num

    def nop(self, _):
        self.pos += 1

    def get_next_input(self):
        self.seen_position.add(self.pos)
        return self.program[self.pos]

    def run(self):
        while(True):
            if self.pos in self.seen_position:
                # Failure
                return None
            if self.pos == len(self.program):
                # Successfully exited
                return self.accumulator
            op, num = self.get_next_input()
            self.ops[op](num)

def parse_input(inp):
    t = [re.match(r'(\w+) (.+)',line).groups() for line in inp.splitlines()]
    return [[x, int(w)] for x,w in t] # improvement: Use named tuple

with open(Path('2020') / 'day8' / 'day8_input.txt') as f:
    inp = f.read()
program_input = parse_input(inp)

p = Program(program_input[:])
p.run()
print(f"Part 1: Accumulator is {p.accumulator}")

for i in range(len(program_input)):
    next_input = copy.deepcopy(program_input) #yeah copy does not mean deep
    if next_input[i][0] == 'nop':
        next_input[i][0] = 'jmp'
    elif next_input[i][0] == 'jmp':
        next_input[i][0] = 'nop'
    else:
        pass
    p = Program(next_input)
    if(p.run()):
        #Completed
        print(f"Part 2: Successfully exited with accumulator {p.accumulator}")
        break