from pathlib import Path
import re
import networkx as nx
import math
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

def graph(modules):
    #Used to see that there are 4 loop running into the end
    edges = []
    for name, module in modules.items():
        edges +=[(name, out) for out in module.outputs]
    print(edges)
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.DiGraph()
    G.add_edges_from(edges)
    black_edges = G.edges()
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 500)
    nx.draw_networkx_labels(G, pos)
    # nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True)
    plt.show()

graph(modules)

press = 0
#these four modules come from separate parts. All need to be False at the same time
# Count when they become false. Saw it takes the same number of button presses each time.
seen ={'vq' : False, 'tf' : False, 'ln' : False, 'db' : False}
while True:
    curr_signals = [('button', 'broadcaster', False)]
    press += 1
    while curr_signals:
        sender, mod_name, signal = curr_signals.pop(0)
        if mod_name in seen and signal == False and seen[mod_name] == False:
            print(f'button press at {press}', signal)
            seen[mod_name] = press
        if mod_name not in modules:
            continue
        if all(seen.values()):
            print("All values seen")
            print(seen.values())
            print(math.prod(seen.values()))
            exit()
        curr_signals += modules[mod_name].send(sender,signal)
