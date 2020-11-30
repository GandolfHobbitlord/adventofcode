f = open(r"day12\input.txt")
input = [l.rstrip('\n') for l in f]
#print(input)
recipe = set()
for line in input[2:]:
    if line[-1] == '#':
        print(line)
        recipe.add(line[:5])
print(recipe)