from pathlib import Path
import re
from collections import Counter

def string2counter(string):
    counter = Counter()
    for match in re.findall(r'(?=(\w\w))', string):
        counter.update([match])
    return counter

def parse_data(input):
    counter = input.splitlines()[0]
    rules = {key:add for key, add in re.findall('(\w+) -> (\w)', input)}
    return counter, rules

def do_steps(string_template, rules, steps):
    chars = Counter(string_template)
    template = string2counter(string_template)
    for _ in range(steps):
        next = Counter()
        for key, val in template.items():
            if key in rules:
                added_letter = rules[key]
                next[key[0] + added_letter] += val
                next[added_letter + key[1]] += val
                chars[added_letter] += val
            else:
                next[key] += val
        template = next.copy()
    return next, chars
def score(chars):
    return max(chars.values()) - min(chars.values())

def run_tests():
    with open(Path("2021") / "day14" / "day14_test.txt") as f:
        template, rules = parse_data(f.read())
    step1, chars1 = do_steps(template, rules, steps=1)
    assert step1 == string2counter('NCNBCHB')
    assert chars1 == Counter('NCNBCHB')
    step2, chars2 = do_steps(template, rules, steps=2)
    assert step2 == string2counter('NBCCNBBBCBHCB')
    assert chars2 == Counter('NBCCNBBBCBHCB')
    _, chars = do_steps(template, rules, steps=10)
    assert score(chars) == 1588

run_tests()

def part1(template, rules):
    _, chars = do_steps(template, rules, steps=10)
    return score(chars)

def part2(template, rules):
    _, chars = do_steps(template, rules, steps=40)
    return score(chars)

with open(Path("2021") / "day14" / "day14_input.txt") as f:
    template, rules = parse_data(f.read())
    print(part1(template,rules))
    print(part2(template,rules))
