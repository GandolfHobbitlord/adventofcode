import os

def traverse(wire):
    directions = {'R' : [1,0], 'L' : [-1,0], 'U' : [0,1], 'D' : [0,-1]}
    x,y,steps = 0,0,1
    pos = {}
    for cmd in wire:
        d = directions[cmd[0]]
        for _ in range(int(cmd[1:])):
            x += d[0]
            y += d[1]
            steps += 1
            pos[(x,y)] = steps
    return pos
 
with open(os.path.join("day3","input.txt")) as f:
    wires =  [wire.split(",") for wire in f.read().split("\n")]
    #wires = [['R8','U5','L5','D3'], ['U7','R6','D4','L4']] #tests
    w_pos = []
    w0_pos = traverse(wires[0])
    w1_pos = traverse(wires[1])

    crossings = set(w0_pos.keys()).intersection(set(w1_pos.keys()))

    ans1 = min([abs(x) + abs(y) for x,y in crossings])
    ans2 = min([w0_pos[k] + w1_pos[k] for k in crossings])
    print("Answer part 1 is {}, answer part 2 is {}".format(ans1,ans2))