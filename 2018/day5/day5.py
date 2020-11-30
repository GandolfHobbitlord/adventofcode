
alpha = "abcdefghijklmnopqrstuvwxyz"

def removePol(s):
    for c in alpha:
        s = s.replace(c.upper()+c.lower(),"")
        s = s.replace(c.lower()+c.upper(),"")
    return s

def removeReactions(s):
    last_len = len(s)
    new_len = 0
    while last_len != new_len:
        last_len = new_len
        s = removePol(s)
        new_len = len(s)
    return s

f = open(r"day5\input.txt")
input = f.read()

def removeInstance(s, c):
    s = s.replace(c.upper(), "")
    s = s.replace(c.lower(), "")
    return s

#input = "aAbBAba"
ans = {}
for c in alpha:
    partStr = removeInstance(input,c)
    ans[c] = len(removeReactions(partStr))
print(ans)
print(min(ans, key=ans.get))
