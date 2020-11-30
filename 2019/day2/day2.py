import operator
import os
op = {
   1: operator.add,
   2: operator.mul,}

with open(os.path.join("day2","input_day2.txt")) as f:
    data = [int(i) for i in f.read().split(",")]
    data_copy = data.copy()
    for i in range(0,100):
        for j in range(0,100):
            data = data_copy.copy()
            data[1] = i
            data[2] = j
            ptr = 0
            while data[ptr] != 99:
                # print(data)
                data[data[ptr+3]] = op[data[ptr]](data[data[ptr+1]],data[data[ptr+2]])
                ptr += 4
            if data[0] == 19690720:
                print("Answer is: {}".format(100 * i + j))
                exit(1)
