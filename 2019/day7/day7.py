import os
import itertools

def read(data, ptr, immediate_mode):
        if immediate_mode:
            return data[ptr]
        else:
            return data[data[ptr]]

def get_mode(instr,arg):
        return (instr // pow(10,arg+1)) % 10
    
class Machine:
    def __init__(self,code, input=[]):
        self.code = code.copy()
        self.ptr = 0
        self.input = input

    def add_input(self, inp):
        self.input.append(inp)

    def run(self):
        return self._run(self.code)


    def _run(self, data):
        ptr = self.ptr
        while data[ptr] != 99:        
            instr = data[ptr]
            op = instr % 100
            if op == 1: #add
                val1 = read(data, ptr+1,get_mode(instr,1))
                val2 = read(data, ptr+2,get_mode(instr,2))
                data[data[ptr+3]] = val1 + val2
                ptr += 4
            elif op == 2:
                val1 = read(data, ptr+1,get_mode(instr,1))
                val2 = read(data, ptr+2,get_mode(instr,2))
                data[data[ptr+3]] = val1 * val2
                ptr += 4
            elif op == 3: #input
                if not self.input:
                    return
                data[data[ptr+1]] = self.input.pop(0)
                ptr +=2
            elif op == 4: #output
                output = read(data,ptr+1,get_mode(instr,1))
                #print(output)
                ptr +=2
            elif op == 5:
                val1 = read(data, ptr+1,get_mode(instr,1))
                val2 = read(data, ptr+2,get_mode(instr,2))
                if val1 != 0:
                    ptr = val2
                else:
                    ptr +=3
            elif op == 6:
                val1 = read(data, ptr+1,get_mode(instr,1))
                val2 = read(data, ptr+2,get_mode(instr,2))
                if 0 == val1:
                    ptr = val2
                else:
                    ptr +=3
            elif op == 7:
                val1 = read(data, ptr+1,get_mode(instr,1))
                val2 = read(data, ptr+2,get_mode(instr,2))
                if val1 < val2:
                    data[data[ptr+3]] = 1
                else:
                    data[data[ptr+3]] = 0
                ptr +=4
            elif op == 8:
                val1 = read(data, ptr+1,get_mode(instr,1))
                val2 = read(data, ptr+2,get_mode(instr,2))
                if val1 == val2:
                    data[data[ptr+3]] = 1
                else:
                    data[data[ptr+3]] = 0
                ptr +=4
            else:
                raise Exception("Invalid operation {}".format(op))
        return output

def part1(data):
    phase__sequences = itertools.permutations(range(0, 5))
    max_output = 0
    for phases in phase__sequences:
        machines = [Machine(data,[phase]) for phase in phases]
        output = 0
        for m in machines:
            m.add_input(output)
            output = m.run()
        if output > max_output:
            max_output = output
            print("New max {} from phases {}".format(output, phases))

with open(os.path.join("day7","input_day7.txt")) as f:
    data = [int(i) for i in f.read().split(",")]
    #data = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    #phases = [4,3,2,1,0]
    part1(data)