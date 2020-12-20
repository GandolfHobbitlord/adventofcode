from collections import defaultdict
from pathlib import Path
import re
def parse_input(inp,part2=False):
    # print(inp)
    rules_raw, msges = inp.split('\n\n')
    # print(rules_raw)
    rules = defaultdict(list)
    for rule in rules_raw.splitlines():
        print(rule)
        rule_nr, ru = rule.split(': ')
        for rule_part in ru.split('|'):
            rules[rule_nr].append(rule_part)
    # print('+++++')
    if part2:
        rules['8'] = ['42 ',' 42 8']
        rules['11']= ['42 31 ','42 11 31 ']
        # rule[]
    # print(rules)
    messages = [line for line in msges.splitlines()]
    return rules,messages

rules_map={}
def generate_regex(rules, key,max_depth=1000, depth = 0):
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
            reg += generate_regex(rules,num,max_depth,depth+1)
        reg += '|'
    final = reg[:-1]+ ')'
    rules_map[key] = final
    return final




def run_test():
    inp = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""
    rules , messages= parse_input(inp)
    reg = generate_regex(rules,'0')
    print([msg for msg in messages if re.fullmatch(r'{}'.format(reg),msg)])

# run_test()

with open(Path("2020") / "day19" / "day19_input.txt") as f:
    inp = f.read()
rules , messages= parse_input(inp,part2=True)
max_len = max([len(msg) for msg in messages])
print(max_len)
reg = generate_regex(rules,'0',max_depth=max_len)
# print(reg)
print(len([msg for msg in messages if re.fullmatch(r'{}'.format(reg),msg)]))