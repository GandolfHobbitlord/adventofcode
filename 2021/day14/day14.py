from pathlib import Path
import re
from collections import Counter
def string2counter(string):
    counter = Counter()
    for match in re.findall(r'(?=(\w\w))', string):
        counter.update([match])
    return counter
def parse_data(input):
    counter = string2counter(input.splitlines()[0])
    rules = {key:add for key, add in re.findall('(\w+) -> (\w)', input)}
    return counter, rules

def step(template, rules):
    next = Counter()
    for key, val in template.items():
        if key in rules:
            added_letter = rules[key]
            next[key[0] + added_letter] += val
            next[added_letter + key[1]] += val
        else:
            next[key] += val
    print(next)
    return next

def score(counter):
    scorer = Counter()
    for key, val in counter.items():
        for char in key:
            scorer[char] += val
    print(scorer)

def run_tests():
    with open(Path("2021") / "day14" / "day14_test.txt") as f:
        template, rules = parse_data(f.read())
    step1 = step(template, rules)
    assert step1 == string2counter('NCNBCHB')
    step2 = step(step1, rules)
    assert step2 == string2counter('NBCCNBBBCBHCB')
    score(string2counter('NCNBCHB'))

run_tests()
