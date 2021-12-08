import re
from pathlib import Path
from typing import Counter


def create_id_dict():
    #Each number will have a unique frequency id, eg number of occurences for each letter
    numbers_key =  {
    '0' : "abcefg",
    '1' : "cf",
    '2' : "acdeg",
    '3' : "acdfg",
    '4' : "bcdf",
    '5' : "abdfg",
    '6' : "abdefg",
    '7' : "acf",
    '8' : "abcdefg",
    '9' : "abcdfg"
    }
    frequency = Counter()
    for val in numbers_key.values():
        frequency.update(val)

    id = {}
    for val, string_id in numbers_key.items():
        list_id = sorted([frequency[letter] for letter in string_id])
        list_str_id = ''.join(str(num) for num in list_id)
        id[list_str_id] = val
    return id

ID = create_id_dict()

def get_output_number(input_patterns, output_patterns):
    frequency = Counter()
    for val in input_patterns:
        frequency.update(val)

    output = ""
    for num in output_patterns:
        list_id = sorted([frequency[letter] for letter in num])
        list_str_id = ''.join(str(num) for num in list_id)
        output += ID[list_str_id]
    return int(output)

def find_unique(outputs):
    ans = 0
    for o in outputs:
        if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7:
            ans +=1
    return ans


def parse_line(line):
    pattern, output = line.split('|')
    input_patterns = re.findall('\w+',pattern)
    output_patterns = re.findall('\w+', output)
    return input_patterns, output_patterns

def part1(nums):
    return sum([find_unique(out_pattern) for _, out_pattern in nums])

def part2(nums):
    return sum([get_output_number(inp_patterns, out_patterns) for inp_patterns, out_patterns in nums])

def run_tests():
    with open(Path("2021") / "day8" / "day8_test.txt") as f:
        nums =  [parse_line(line) for line in f.read().splitlines()]
    assert part1(nums) == 26
    inp = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    inp_pattern, output_nums = parse_line(inp)
    assert get_output_number(inp_pattern, output_nums) == 5353
    assert part2(nums) == 61229


run_tests()

with open(Path("2021") / "day8" / "day8_input.txt") as f:
    nums =  [parse_line(line) for line in f.read().splitlines()]

print(f"Answer part 1 {part1(nums)}")
print(f"Answer part 2 {part2(nums)}")