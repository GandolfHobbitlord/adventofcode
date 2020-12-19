import re
from pathlib import Path
from itertools import chain
def parse_rules(inp):
    rules = []
    for rule in inp.splitlines():
        print(rule)
        lo0,hi0,lo1,hi1 = [int(i) for i in re.search(r'(\d+)-(\d+) or (\d+)-(\d+)',rule).groups()]
        rules.append({i for i in chain(range(lo0,hi0+1),range(lo1,hi1+1))})
    return rules

def parse_nearby_tickets(inp):
    tickets = []
    for ticket in inp.splitlines()[1:]: #avoid first late
        tickets.append([int(num) for num in ticket.split(',')])
    return tickets

def part1(rules, tickets):
    all_valid_numbers = set.union(*rules)
    invalid_numbers = []
    for ticket in tickets:
        print(ticket)
        invalid_numbers.extend([num for num in ticket if num not in all_valid_numbers])
    return sum(invalid_numbers)
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
    with open(Path("2020") / "day16" / "day16_input.txt") as f:
        inp = f.read()
    rules, my_ticket, nearby = inp.split('\n\n')
    rules = parse_rules(rules)
    invalid_numbers = []
    all_valid_numbers = set.union(*rules)
    tickets = parse_nearby_tickets(nearby)
    print(part1(rules,tickets))

run_test()