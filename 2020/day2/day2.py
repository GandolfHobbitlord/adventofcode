import re
from pathlib import Path

def parse_line(line):
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

def get_valid_pass_part1(input):
    valid_pass = []
    for line in input:
        lo, hi, char, password = parse_line(line)
        count = password.count(char)
        if count <= hi and count >= lo:
            valid_pass.append(password)
    return valid_pass

def get_valid_pass_part2(input):
    valid_pass = []
    for line in input:
        lo, hi, char, password = parse_line(line)
        count = 0
        if password[lo-1] == char:
            count +=1
        if password[hi-1] == char:
            count +=1
        if count == 1:
            valid_pass.append(password)
    return valid_pass

def run_tests():
    input = ["1-3 a: abcde","1-3 b: cdefg", "2-9 c: ccccccccc"]
    ans = get_valid_pass_part1(input)
    assert ans == ["abcde", "ccccccccc"]
    ans = get_valid_pass_part2(input)
    assert ans == ["abcde"]

run_tests()
with open(Path("2020") / "day2" / "day2_input.txt") as f:
    numbers = f.read().splitlines()
    valid = get_valid_pass_part1(numbers)
    print(f"Number of valid passwords for part 1 is {len(valid)}")
    valid = get_valid_pass_part2(numbers)
    print(f"Number of valid passwords for part 2 is {len(valid)}")