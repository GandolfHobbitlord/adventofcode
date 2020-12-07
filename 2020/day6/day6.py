from pathlib import Path
import re

def get_uniques(inp):
    return set(re.findall(r'(\w)',inp))

def get_question_all_answered(group):
    return set.intersection(*(set(person) for person in group.split('\n')))
    # return set.intersection(*map(set,group.split('\n'))) Optional solution

def run_test():
    assert get_uniques('abc') == {'a','b','c'}
    assert get_uniques('a\nb\nc') == {'a','b','c'}
    assert get_uniques('ab\nbc') == {'a','b','c'}
    assert get_uniques('a\na\na') == {'a'}

    assert get_question_all_answered('abc') == {'a','b','c'}
    assert get_question_all_answered('a\nb\nc') == set()
    assert get_question_all_answered('ab\nbc') == {'b'}
    assert get_question_all_answered('a\na\na') == {'a'}
run_test()

with open(Path("2020") / "day6" / "day6_input.txt") as f:
    groups = [line for line in f.read().split("\n\n")]

ans1 = sum([len(get_uniques(g)) for g in groups])
print(f'Part 1: {ans1}')

ans2 = sum([len(get_question_all_answered(g)) for g in groups])
print(f'Part 2: {ans2}')