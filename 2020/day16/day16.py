import re
from pathlib import Path
from itertools import chain

def parse_rules(inp):
    rules = {}
    for rule in inp.splitlines():
        print(rule)
        name, rule_numbers = rule.split(':')
        lo0,hi0,lo1,hi1 = [int(i) for i in re.search(r'(\d+)-(\d+) or (\d+)-(\d+)',rule_numbers).groups()]
        print(name)
        rules[name] = ({i for i in chain(range(lo0,hi0+1),range(lo1,hi1+1))})
    return rules

def parse_nearby_tickets(inp):
    tickets = []
    for ticket in inp.splitlines()[1:]: #avoid first late
        tickets.append([int(num) for num in ticket.split(',')])
    return tickets

def parse_input(inp):
    rules, my_ticket, nearby = inp.split('\n\n')
    rules = parse_rules(rules)
    tickets = parse_nearby_tickets(nearby)
    return rules, my_ticket , tickets

def part1(rules, tickets):
    print(rules)
    all_valid_numbers = set.union(*rules.values())
    invalid_numbers = []
    for ticket in tickets:
        invalid_numbers.extend([num for num in ticket if num not in all_valid_numbers])
    return sum(invalid_numbers)

def get_valid_tickets(rules,tickets):
    all_valid_numbers = set.union(*rules.values())
    valid_tickets = [ticket for ticket in tickets if all( num in all_valid_numbers for num in ticket)]
    print("VALID TICKETS", valid_tickets)
    return valid_tickets

def get_ticket_groups(tickets):
    ticket_groups = []
    for i in range(len(tickets[0])):
        ticket_groups.append(set(ticket[i] for ticket in tickets))
    print(ticket_groups)
    return ticket_groups

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
    valid_tickets = get_valid_tickets(rules,tickets)

    ticket_groups = get_ticket_groups(tickets)

run_test()
# with open(Path("2020") / "day16" / "day16_input.txt") as f:
#     inp = f.read()
# rules, my_ticket, tickets = parse_input(inp)
# print(f"Answer part1 {part1(rules,tickets)}")
