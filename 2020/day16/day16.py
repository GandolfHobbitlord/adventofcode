import re
from pathlib import Path
from itertools import chain
from collections import defaultdict
from functools import reduce

def parse_rules(inp):
    rules = {}
    for rule in inp.splitlines():
        name, rule_numbers = rule.split(':')
        lo0,hi0,lo1,hi1 = [int(i) for i in re.search(r'(\d+)-(\d+) or (\d+)-(\d+)',rule_numbers).groups()]
        rules[name] = ({i for i in chain(range(lo0,hi0+1),range(lo1,hi1+1))})
    return rules

def parse_ticket(inp):
    tickets = []
    for ticket in inp.splitlines()[1:]: #avoid first as it is header
        tickets.append([int(num) for num in ticket.split(',')])
    return tickets

def parse_input(inp):
    rules, my_ticket, nearby = inp.split('\n\n')
    rules = parse_rules(rules)
    my_ticket = parse_ticket(my_ticket)[0]
    tickets = parse_ticket(nearby)
    return rules, my_ticket, tickets

def part1(rules, tickets):
    all_valid_numbers = set.union(*rules.values())
    invalid_numbers = []
    for ticket in tickets:
        invalid_numbers.extend([num for num in ticket if num not in all_valid_numbers])
    return sum(invalid_numbers)

def get_valid_tickets(rules,tickets):
    all_valid_numbers = set.union(*rules.values())
    valid_tickets = [ticket for ticket in tickets if all( num in all_valid_numbers for num in ticket)]
    return valid_tickets

def get_ticket_groups(tickets):
    ticket_groups = []
    for i in range(len(tickets[0])):
        ticket_groups.append(set(ticket[i] for ticket in tickets))
    return ticket_groups

# Assumes there is always only one group that can be assigned to a rule. Valid?
# Returns a dict with rule name and position of that class
def assign_rulename_to_group(rules,tickets):
    valid_tickets = get_valid_tickets(rules,tickets)
    ticket_groups = get_ticket_groups(valid_tickets)
    unasigned_groups = [i for i, _ in enumerate(ticket_groups)]
    results = {}
    while unasigned_groups:
        tmp = defaultdict(list)
        for rule_name, rule in rules.items():
            for group_nr in unasigned_groups:
                if ticket_groups[group_nr].issubset(rule):
                    tmp[rule_name].append(group_nr)
        for key, val in tmp.items():
            if len(val) == 1:
                results[key] = val[0]
                unasigned_groups.remove(val[0])
    return results


def run_test():
    inp = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
    rules, my_ticket, tickets = parse_input(inp)
    assert 71 == part1(rules,tickets)
run_test()

with open(Path("2020") / "day16" / "day16_input.txt") as f:
    inp = f.read()

rules, my_ticket, tickets = parse_input(inp)
print(f"Answer part1 {part1(rules,tickets)}")

rule_name_dict = assign_rulename_to_group(rules,tickets)
depature_positions = [val for key, val in rule_name_dict.items() if key.startswith('departure')]
#No numpy this is the easiest way to write product.....
print(f"Answer part2: {reduce(lambda x, y: x*y,[my_ticket[d] for d in depature_positions])}")
