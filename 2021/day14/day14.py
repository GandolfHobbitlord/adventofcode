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

def step(string_template, rules, steps=1):
    next = Counter()
    chars = Counter(string_template)
    template = string2counter(string_template)
    for key, val in template.items():
        if key in rules:
            added_letter = rules[key]
            next[key[0] + added_letter] += val
            next[added_letter + key[1]] += val
            chars.update(added_letter)
        else:
            next[key] += val
    return next

def run_tests():
    with open(Path("2021") / "day14" / "day14_test.txt") as f:
        template, rules = parse_data(f.read())
    step1 = step(template, rules)
    assert step1 == string2counter('NCNBCHB')
    # step2 = step(template, rules)
    # assert step == string2counter('NBCCNBBBCBHCB')
run_tests()
