from pathlib import Path
import re
from collections import defaultdict

class Broadcaster:
    def __init__(self,name,outputs):
        self.name = name
        self.outputs = outputs
        self.inputs = set()

    def send(self, sender, signal):
        return [(self.name, output, signal) for output in self.outputs]

class FlipFlop:
    def __init__(self,name,outputs):
        self.name = name
        self.saved = False
        self.outputs = outputs
        self.inputs = set()

    def send(self, sender, signal):
        if signal:
            return []
        self.saved = not self.saved
        return [(self.name, output, self.saved) for output in self.outputs]

class Conjugation:
    def __init__(self,name,outputs):
        self.name = name
        self.saved = {}
        self.outputs = outputs
        self.inputs = set()
        self.initilized = False

    def send(self, sender, signal):
        if not self.initilized:
            for input in self.inputs:
                self.saved[input] = False
            self.initilized = True
        self.saved[sender] = signal
        out_signal = not all(self.saved.values())
        return [(self.name, output, out_signal) for output in self.outputs]

def parse_line(line):
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

def factory(line):
    part, output = line.split('->')
    type = part[0]
    outputs = re.findall(r'\w+',output)
    print(part,outputs)
    if part.startswith('%'):
        name = part[1:].strip()
        print('FlipFlop:' + name)
        ff = FlipFlop(name,outputs)
        return name,ff
    elif part.startswith('&'):
        name = part[1:].strip()
        conj = Conjugation(name,outputs)
        print('Conjugation')
        return name,conj
    elif part.startswith('broadcaster'):
        name = 'broadcaster'
        broad = Broadcaster(name,outputs)
        print('Broadcaster')
        return name,broad
    raise RuntimeError('Unknown class')

def print_module(module):
    print(vars(module))

with open(Path("2023") / "day20" / "day20_input.txt") as f:
# with open(Path("2023") / "day20" / "day20_test.txt") as f:
    data = [line for line in f.read().split('\n')]
    # data = [parse_line(line) for line in f.read().split('\n')]

modules = dict([factory(line) for line in data])

for name, module in modules.items():
    for output in module.outputs:
        if output in modules:
            modules[output].inputs.add(name)

for m in modules.values():
    print_module(m)

nr_false, nr_true = (0,0)
for _ in range(1000):
    print('-------------')
    curr_signals = [('button', 'broadcaster', False)]
    while curr_signals:
        sender, mod_name, signal = curr_signals.pop(0)
        if signal:
            nr_true += 1
        else:
            nr_false += 1
        # print(f'{sender}-> {signal} -> {mod_name}')
        if mod_name not in modules:
            continue
        curr_signals += modules[mod_name].send(sender,signal)
print(nr_false,nr_true)
print(nr_true * nr_false)
# print(f)