import re
from collections import Counter
from pathlib import Path
def part1(inp):
    cont = {}
    c = Counter()
    all_ingr = set()
    for line in inp.splitlines():
        ingr_str, conaminents = line.split(' (contains ')
        ingr = set([ingredient for ingredient in ingr_str.split(' ')])
        all_ingr |= ingr
        c.update(ingr)
        allergens = [c for c in re.findall(r'\w+',conaminents)]
        for allergen in allergens:
            if allergen in cont:
                cont[allergen] = set.intersection(cont[allergen], ingr)
            else:
                cont[allergen] = ingr
    print(all_ingr)
    print(cont)
    print(c)
    no_allergen_ingr = all_ingr - set().union(*cont.values())
    return sum([c[a] for a in no_allergen_ingr])
def run_test():
    inp = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

    assert 5 == part1(inp)
run_test()
with open(Path("2020") / "day21" / "day21_input.txt") as f:
    inp = f.read()
    # print(part1(inp))