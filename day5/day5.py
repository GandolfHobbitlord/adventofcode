import operator
import os
op = {
   1: operator.add,
   2: operator.mul,}

def read(data, ptr, immediate_mode):
    if immediate_mode:
        return data[ptr]
    else:
        return data[data[ptr]]

def get_mode(instr,arg):
    return (instr // pow(10,arg+1)) % 10


def run(data, input_val):
    ptr = 0
    output = 0
    steps = 0
    while data[ptr] != 99:
        steps +=1
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
        elif op == 3:
            #data[read(data,ptr+1,get_mode(instr,1))] = input_val
            data[data[ptr+1]] = input_val
            ptr +=2
        elif op == 4:
            output = read(data,ptr+1,get_mode(instr,1))
            print(output)
            ptr +=2
        else:
            raise Exception("Invalid operation {}".format(op))
    return output

with open(os.path.join("day5","input_day5.txt")) as f:
    data = [int(i) for i in f.read().split(",")]
    #data = [1002,4,3,4,33]
    out = run(data,1)