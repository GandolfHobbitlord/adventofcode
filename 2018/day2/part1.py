from collections import Counter


def count_occurences(inp):
    num2 = 0
    num3 = 0
    for i in inp:
        res = Counter(i)
        if 2 in res.values():
            num2 += 1
        if 3 in res.values():
            num3 += 1
    return num2, num3

def get_matches(inp):
    for word1 in inp:
        for word2 in inp:
            diff = 0
            for ch1, ch2 in zip(word1,word2):
                if(ch1 != ch2):
                    diff +=1
                    if(diff > 1):
                        break
            if diff == 1:
                return(word1, word2)


f = open(r"day2\input.txt")
inp = [str(line).rstrip('\n') for line in f.readlines()]

#part1
twos, threes =count_occurences(inp)
print("Ans part1:",twos, "*", threes, "=", twos*threes)

#part2
word1, word2 = get_matches(inp)
ans = ""
for ch1, ch2 in zip(word1,word2):
    if ch1 == ch2:
        ans += ch1
print("Answer part2: ", ans)