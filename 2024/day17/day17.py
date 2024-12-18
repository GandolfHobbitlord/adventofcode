from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict



def run(program,A,B=0,C=0):
    idx = 0
    out = []
    val = [0,1,2,3,A,B,C]
    while idx < len(program):
        op = program[idx]
        # print(f'opcode {op}')
        if op == 0:
            combo = program[idx+1]
            val[4] = val[4] >> val[combo]
        elif op == 1:
            literal = program[idx+1]
            val[5] = val[5] ^ literal
        elif op == 2:
            combo = program[idx+1]
            val[5] = val[combo] % 8
        elif op == 3:
            if val[4] != 0:
                literal = program[idx+1]
                idx = literal
                continue
        elif op == 4:
            val[5] = val[5] ^ val[6]
        elif op == 5:
            combo = program[idx+1]
            out.append(val[combo] % 8)
        elif op == 6:
            combo = program[idx+1]
            val[5] = val[4] >> val[combo]
        elif op == 7:
            combo = program[idx+1]
            val[6] = val[4] >> val[combo]
        else:
            RuntimeError("INVALID OP CODE")
        idx +=2
    return out, val

def run_tests():
    o, res =run(program=[2,6],A=0,B=0,C=9)
    assert res[5] == 1
    o, res =run(program=[5,0,5,1,5,4],A=10,B=0,C=9)
    assert o == [0,1,2]
    o, res =run(program=[0,1,5,4,3,0],A=2024,B=0,C=9)
    assert o == [4,2,5,6,7,7,7,7,3,1,0]
    assert res[4] == 0
    o, res =run(program=[1,7],A=2024,B=29,C=9)
    assert res[5] == 26
    o, res =run(program=[4,0],A=2024,B=2024,C=43690)
    assert res[5] == 44354
    o, res =run(program=[0,1,5,4,3,0],A=729,B=0,C=0)
    assert o == [4,6,3,5,6,3,5,2,1,0]
# run_tests()

#Misread and thought B,C mattered so thought i had to do it in correct order. not sure why it isn't functioning though...
# def recursive_solve(program,shifts=0,A=0):
#     if shifts == len(program):
#         print(program)
#         return A
#     for i in range(8):
#         test_a = (i << (3*shifts)) | A
#         out, _ = run(program,test_a)
#         if program[:shifts+1] == out:
#             res = recursive_solve(program,shifts+1,A=test_a)
#             if res:
#                 return res
#     return None

ans = []
#B,C have no effect, just A
def recursive_solve(program,shifts=0,A=0):
    if shifts == len(program):
        ans.append(A)
        return A
    for test in range(8):
        test_a = (A<< 3) | test
        out, _ = run(program, test_a)
        if out == program[-1*(1+shifts):]:
            recursive_solve(program,shifts+1,test_a)

# o, res =run(program=[2,4,1,1,7,5,0,3,1,4,4,0,5,5,3,0],A=32916674,B=0,C=0)
recursive_solve(A=0,program=[2,4,1,1,7,5,0,3,1,4,4,0,5,5,3,0])

# print(o)
#Part 1
o, res =run(program=[2,4,1,1,7,5,0,3,1,4,4,0,5,5,3,0],A=32916674,B=0,C=0)
print( "part 1 "+",".join(str(x) for x in o))
print(f"Part 2 {sorted(ans)[0]}")