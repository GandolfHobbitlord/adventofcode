import re
from collections import Counter
from pathlib import Path
def part1(inp):
    cont = {}
    ingr_counter = Counter()
    all_ingr = set()
    for line in inp.splitlines():
        ingr_str, contaminets = line.split(' (contains ')
        ingr = set([ingredient for ingredient in ingr_str.split(' ')])
        all_ingr |= ingr
        ingr_counter.update(ingr)
        allergens = [allergen for allergen in re.findall(r'\w+',contaminets)]
        for allergen in allergens:
            if allergen in cont:
                cont[allergen] = set.intersection(cont[allergen], ingr)
            else:
                cont[allergen] = ingr
    no_allergen_ingr = all_ingr - set().union(*cont.values())
    return sum([ingr_counter[ingredient] for ingredient in no_allergen_ingr])

def part2(inp):
    cont = {}
    all_ingr = set()
    for line in inp.splitlines():
        ingr_str, contaminets = line.split(' (contains ')
        ingr = set([ingredient for ingredient in ingr_str.split(' ')])
        all_ingr.update(ingr)
        allergens = [c for c in re.findall(r'\w+',contaminets)]
        for allergen in allergens:
            if allergen in cont:
                cont[allergen] = set.intersection(cont[allergen], ingr)
            else:
                cont[allergen] = ingr
    answers = []
    taken = set()
    # Real part2 here. The stuff before is copy paste from part1, to lazy to clean today
    while len(taken) != len(cont.keys()):
        for allergen, ingr in cont.items():
            remaining = ingr - taken
            if len(remaining) == 1:
                elem = remaining.pop()
                answers.append((allergen,elem))
                taken.add(elem)
    answers.sort(key=lambda x:x[0])
    return ','.join([ingr for _, ingr in answers])

def run_test():
    inp = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

    assert 5 == part1(inp)
    assert part2(inp) == 'mxmxvkd,sqjhc,fvjkl'
run_test()
with open(Path("2020") / "day21" / "day21_input.txt") as f:
    inp = f.read()
print(f'Answer part 1: {part1(inp)}')
print(f'Answer part 2: {part2(inp)}')