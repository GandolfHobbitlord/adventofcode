import re
from collections import defaultdict
from pathlib import Path

def parse_rules(inp):
    children = defaultdict(list)
    parents = defaultdict(set)
    for line in inp.splitlines():
        bag = re.match(r'\w+ \w+',line).group()
        for num, containing_color in re.findall(r'(\d+) (.+?) bag', line):
            children[bag].append((int(num),containing_color))
            parents[containing_color].add(bag)
    return parents, children

def num_containing_bags(bag, bag_rules):
    count = 0
    for num, bag_type in bag_rules[bag]:
        count += num + num * num_containing_bags(bag_type, bag_rules)
    return count

def has_gold(bag_type,rules,contains_item):
    for bag in rules[bag_type]:
        contains_item.add(bag)
        has_gold(bag, rules, contains_item)

with open(Path('2020') / 'day7' / 'day7_input.txt') as f:
    inp = f.read()
parents, children = parse_rules(inp)

bags_containing_gold = set()
has_gold('shiny gold' , parents, bags_containing_gold) # Everything in python is refs, this is ugly though. hashtag no globals
print(f'Number of bag types containing golden bag {len(bags_containing_gold)}')
print(f"Number of bags in a shiny golden bag {num_containing_bags('shiny gold', children)}")
