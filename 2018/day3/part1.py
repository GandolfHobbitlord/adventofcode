import numpy as np

SIZE = 10000

def parse_claim(claim):
    id_hash, _, coords, size = claim.split(" ")
    id=id_hash
    x,y = map(int, coords[:-1].split(","))
    w,h = map(int, size.split("x"))
    #print(id, x, y, w, h)
    return id, x, y, w, h

#f = open("input.txt")
#input = f.read().strip().splitlines()
#blanket = np.zeros((SIZE,SIZE))
#for claim in input:
#    ident, x,y,w,h = parse_claim(claim)
#    blanket[x:x+w,y:y+h] +=1
#clashes = 0
#for i in range(0,SIZE):
#    for j in range(0,SIZE):
#        if(blanket[i,j] > 1):
#            clashes +=1
#print("CLASHES", clashes)

f = open("input.txt")
input = f.read().strip().splitlines()
blanket = np.zeros((SIZE,SIZE))
for claim in input:
    ident, x,y,w,h = parse_claim(claim)
    blanket[x:x+w,y:y+h] +=1

for claim in input:
    ident, x,y,w,h = parse_claim(claim)
    if np.all(blanket[x:x+w,y:y+h] == 1):
        print("Identity: ", ident)
        break