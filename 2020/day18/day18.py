import re
from pathlib import Path
class x:
    def __init__(self,val):
        self.val = int(val)

    def __add__(self,o):
        return x(self.val + o.val)

    def __sub__(self,o):
        return x(self.val * o.val)

    def __mul__(self,o):
        return x(self.val + o.val)

#Tactic: wrap all digits in class which redifines operators so that order of operations still match
def solve_line1(line):
    #wrap all digits in x class ie 2 + 3 * 3 -> x(2) + x(3) * x(3)
    line = re.sub(r'(\d+)',r'x(\1)',line)
    # replace all * with - and define - operator for class as multiplication, same order of operation :)
    line = line.replace('*','-')
    return eval(line).val

def solve_line2(line):
    line = re.sub(r'(\d+)',r'x(\1)',line)
    line = line.replace('*','-')
    #now + has higher order so give it a * instead which has higher order
    line = line.replace('+','*')
    return eval(line).val

def run_test():
    inp = '1 + 2 * 3 + 4 * 5 + 6'
    assert 71 == solve_line1(inp)
    assert 231 == solve_line2(inp)
    assert 13632 == solve_line1('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
run_test()

with open(Path("2020") / "day18" / "day18_input.txt") as f:
    inp = f.read()
    ans1 = sum([solve_line1(line) for line in inp.splitlines()])
    print(f"Answer part 1: {ans1}")
    ans2 = sum([solve_line2(line) for line in inp.splitlines()])
    print(f"Answer part 2: {ans2}")