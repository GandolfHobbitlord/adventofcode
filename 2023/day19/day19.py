from pathlib import Path

# This years dirty eval!
def parse_part(part):
    for val in 'xmas':
        part = part.replace(f'{val}=',f'"{val}":')
    return eval(part)

def parse_workflow(wf):
    key, rest = wf.split('{')
    rules = rest[:-1].split(',')
    out_rules = []
    for rule in rules[:-1]:
        e, dest = rule.split(':')
        val = e[0]
        #Prepare for more eval fun!
        e = e.replace(f'{val}',f'part["{val}"]')
        out_rules.append((e,dest))
    out_rules.append(('True', rules[-1]))
    return key, out_rules

def get_next(part,rules):
    for rule, dest in rules:
        if eval(rule):
            return dest

with open(Path("2023") / "day19" / "day19_input.txt") as f:
# with open(Path("2023") / "day19" / "day19_test.txt") as f:
    wfs, parts  = f.read().split('\n\n')
parts = [parse_part(part) for part in parts.splitlines()]
wfs = dict([parse_workflow(wf) for wf in wfs.splitlines()])
ans = 0
for part in parts:
    loc = 'in'
    while not (loc == 'A' or loc == 'R'):
        loc = get_next(part, wfs[loc])
    if loc == 'A':
        ans += sum(part.values())

print(ans)