import re
from pathlib import Path

def mask_val(mask,val):
    or_mask = mask.replace('X','0')
    print(mask)
    # print(or_mask)
    val = val | int(or_mask,2) # set ones
    and_mask = mask.replace('X','1')
    val = val & int(and_mask,2) # set zeros
    return val

# def mask_ver_2(mask,pos):
#     # print(pos)
#     # print("HELLO")
#     # print(bin(pos))

#     # print("{0:b}".format(pos))
#     masked_mem = pos & mask.replace('X',1)
#     # print("masked mem", masked_mem)
#     x_indices = [x.start() for x in re.finditer(r'X', mask)]
#     # print("X index", x_indices)
#     # [a if C else b for i in items]
#     print('0',"{0:036b}".format(pos))
#     print('1',mask)
#     print('2',masked_mem)
#     print('3',''.join(['X' if pos in x_indices else char for pos, char in enumerate(masked_mem)]))
#     exit(1)
#     return ''.join(['X' if pos in x_indices else char for pos, char in enumerate(masked_mem)])


def update_mem1(mem, mask, pos,val):
    print(f"update position {pos} with {val}")
    mem[pos] = mask_val(mask,val)

def update_mem2(mem, mask, pos, val):
    print("mask", mask)
    if mask.count('X') == 0:
        # print("hello")
        mem_pos = pos | int(mask,2)
        print("{0:036b}".format(mem_pos))
        # print(pos, mask)
        mem[pos | int(mask,2)] = val
    else:
        update_mem2(mem,mask.replace('X','0',1),pos,val)
        update_mem2(mem,mask.replace('X','1',1),pos,val)
    return mem

def parse_input(inp,part2=False):
    mem = {}
    mask = ''
    for line in inp.splitlines():
        print(line)
        command, val = line.split(' = ')
        if command == "mask":
            print(f"set mask to {val}")
            mask = val
        else:
            pos = re.findall(r'\d+',command)[0]
            if part2:
                print("VARIANTS OF MASK")
                print(mask)
                pos_mask = mask_ver_2(mask,int(pos))
                print("{0:036b}".format(int(pos)))
                update_mem2(mem, mask,int(pos), int(val))
                print(mem)
            else:
                update_mem1(mem, mask, int(pos),int(val))
    return mem

def run_test():
    inp = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
    # mem = parse_input(inp)
    # assert 165 == sum(mem.values())
    inp = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
    mem = parse_input(inp,part2=True)
    print(mem)


run_test()
# with open(Path("2020") / "day14" / "day14_input.txt") as f:
#     mem = parse_input(f.read())
#     print(sum(mem.values()))