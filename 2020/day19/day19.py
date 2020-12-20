from collections import defaultdict
from pathlib import Path
import re

def parse_input(inp,part2=False):
    rules_raw, msges = inp.split('\n\n')
    rules = defaultdict(list)
    for rule in rules_raw.splitlines():
        rule_nr, ru = rule.split(': ')
        for rule_part in ru.split('|'):
            rules[rule_nr].append(rule_part)
    if part2:
        rules['8'] = ['42 ',' 42 8']
        rules['11']= ['42 31 ','42 11 31 ']
    messages = [line for line in msges.splitlines()]
    return rules,messages

def generate_regex(rules,key,rules_map=None,max_depth=1000, depth = 0):
    if rules_map == None:
        rules_map = {}
    if key in rules_map:
        return rules_map[key]
    elif rules[key] == ['\"a\"']:
        return 'a'
    elif rules[key] == ['\"b\"']:
        return 'b'
    elif depth >= max_depth:
        #Stop looking we are in too deep
        return 'c'
    reg = "("
    for rule in rules[key]:
        for num in re.findall(r'\d+', rule):
            reg += generate_regex(rules,num,rules_map,max_depth,depth+1)
        reg += '|'
    final = reg[:-1]+ ')'
    rules_map[key] = final
    return final

def is_message_valid(reg,msg):
    return re.fullmatch(r'{}'.format(reg),msg) != None

with open(Path("2020") / "day19" / "day19_input.txt") as f:
    inp = f.read()
rules , messages= parse_input(inp)
max_len = max([len(msg) for msg in messages])
# print(max_len)
reg = generate_regex(rules,'0',max_depth=max_len)
print(f"Number of valid messages part1: {sum([is_message_valid(reg,msg) for msg in messages])}")

rules , messages= parse_input(inp,part2=True)
reg = generate_regex(rules,'0',max_depth=max_len)
print(f"Number of valid messages part2: {sum([is_message_valid(reg,msg) for msg in messages])}")
