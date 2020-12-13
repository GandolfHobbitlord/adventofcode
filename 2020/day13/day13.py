import numpy as np
def parse_input1(inp):
    timestamp, busses = inp.splitlines()
    busses = [int(bus) for bus in busses.split(',') if bus != 'x']
    return int(timestamp), busses

def parse_input2(inp):
    _, busses = inp.splitlines()
    return [(offset, int(bus)) for offset, bus in enumerate(busses.split(',')) if bus != 'x']

def find_next_depart(time,busses):
    while True:
        for bus in busses:
            if time % bus == 0:
                return time, bus
        time +=1

def part2(busses):
    step = 1
    time = 0
    for offset, bus in busses:
        while((time+offset) % bus != 0):
            time +=step
        step = np.lcm(bus,step)
    return(time)

def run_test():
    inp =  '939\n7,13,x,x,59,x,31,19'
    t,b = parse_input1(inp)
    dep_time, dep_bus = find_next_depart(t,b)
    assert (dep_time-t)*dep_bus == 295

    assert part2(parse_input2(inp)) == 1068781
    inp = '0\n67,x,7,59,61'
    print("passed1")
    assert part2(parse_input2(inp)) == 779210
    inp = '0\n67,7,x,59,61'
    assert part2(parse_input2(inp)) == 1261476
    print("passed2")
    inp = '0\n1789,37,47,1889'
    assert part2(parse_input2(inp)) == 1202161486
    print("passed3")
run_test()

inp = '1002394\n13,x,x,41,x,x,x,37,x,x,x,x,x,419,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,29,x,421,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17'
time,busses = parse_input1(inp)
dep_time, dep_bus = find_next_depart(time,busses)
print(f"Part1 ans: {(dep_time-time)*dep_bus}")
print(f"Part2 ans: {part2(parse_input2(inp))}")