import operator
import os
import math
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
        elif op == 3: #input
            #data[read(data,ptr+1,get_mode(instr,1))] = input_val
            data[data[ptr+1]] = input_val
            ptr +=2
        elif op == 4: #output
            output = read(data,ptr+1,get_mode(instr,1))
            print(output)
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

with open(os.path.join("day5","input_day5.txt")) as f:
    data = [int(i) for i in f.read().split(",")]
    #data = [1002,4,3,4,33]
   # data = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
   # data =[3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    #data = [3,9,8,9,10,9,4,9,99,-1,8]
    out = run(data,5)