import re
from pathlib import Path

def mask_val_v1(mask,val):
    val = val | int(mask.replace('X','0'),2) # set ones
    val = val & int(mask.replace('X','1'),2) # set zeros
    return val

def mask_val_v2(mask,pos):
    pos = pos | int(mask.replace('X','0'),2) #force ones from mask
    pos_str = "{0:036b}".format(pos) # to binary string
    #force X positions and return string
    return ''.join(['X' if mask_char == 'X' else pos_char for mask_char, pos_char in zip(mask,pos_str)])

def possible_addr(mask_addr):
    if mask_addr.count('X') == 0:
        yield int(mask_addr,2)
    else:
        yield from possible_addr(mask_addr.replace('X','0',1))
        yield from possible_addr(mask_addr.replace('X','1',1))

def parse_input(inp,part2=False):
    mem = {}
    mask = ''
    for line in inp.splitlines():
        command, val = line.split(' = ')
        if command == "mask":
            mask = val
        else:
            pos = re.findall(r'\d+',command)[0]
            if part2:
                for addr in possible_addr(mask_val_v2(mask,int(pos))):
                    mem[addr] = int(val)
            else:
                mem[int(pos)] = mask_val_v1(mask,int(val))
    return mem

def run_test():
    inp = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
    mem = parse_input(inp)
    assert 165 == sum(mem.values())
    inp = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
    mem = parse_input(inp,part2=True)
    assert 208 == sum(mem.values())


run_test()
with open(Path("2020") / "day14" / "day14_input.txt") as f:
    inp = f.read()
mem = parse_input(inp)
print(sum(mem.values()))
mem = parse_input(inp,part2=True)
print(sum(mem.values()))