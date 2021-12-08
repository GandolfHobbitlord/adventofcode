import re
from pathlib import Path
from collections import defaultdict
from typing import Counter

NUM_KEY =  {
    '0' : set("abcefg"),
    '1' : set("cf"),
    '2' : set("acdeg"),
    '3' : set("acdfg"),
    '4' : set("bcdf"),
    '5' : set("abdfg"),
    '6' : set("abdefg"),
    '7' : set("acf"),
    '8' : set("abcdefg"),
    '9' : set("abcdfg")
}
FREQ = Counter()
for val in NUM_KEY.values():
    FREQ.update(val)

ID = {}
for val, string_id in NUM_KEY.items():
    list_id = sorted([FREQ[letter] for letter in string_id])
    list_str_id = ''.join(str(num) for num in list_id)
    # print(list_str_id)
    ID[list_str_id] = val
print(ID)


def part2(input, ouput_nums):
    line_frequency = Counter()
    ans = ""
    for val in input:
        line_frequency.update(val)
    for num in ouput_nums:
        list_id = sorted([line_frequency[letter] for letter in num])
        list_str_id = ''.join(str(num) for num in list_id)
        print(ID[list_str_id])
        ans += ID[list_str_id]
    return int(ans)

def parse_line(line):
    pattern, output = line.split('|')
    pattern_set = [set(p) for p in re.findall('\w+',pattern)]
    output_set = [set(p) for p in re.findall('\w+',output)]

    return pattern_set, output_set

def find_valid_part1(outputs):
    ans = 0
    for o in outputs:
        if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7:
            print(o, "is valid")
            ans +=1
    return ans

def run_tests():
    with open(Path("2021") / "day8" / "day8_test.txt") as f:
        nums =  [parse_line(line) for line in f.read().splitlines()]
    # assert sum([find_valid_part1(n[1]) for n in nums]) == 26
    inp = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    inp_pattern, output_nums = parse_line(inp)
    part2(inp_pattern, output_nums) == 5353



with open(Path("2021") / "day8" / "day8_input.txt") as f:
    nums =  [parse_line(line) for line in f.read().splitlines()]
    print(sum([part2(n[0], n[1]) for n in nums]))

run_tests()
# part1(data)