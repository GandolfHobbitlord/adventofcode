from collections import defaultdict

def getTime(line):
    words = line.split(" ")
    date = words[0][1:]
    time = words[1][:-1].split(":")[1]
    return int(time)

def getGuard(line):
    return int(line.split(" ")[3][1:])

f = open(r"day4\input.txt")
input = sorted(f.read().strip().splitlines())
guardOnDuty = 0
asleepFrom = 0
guardSleepingTime = defaultdict(int)
guardPopularSleepingTime = defaultdict(lambda:[0]*60)
for line in input:
    if "begins shift" in line:
        guardOnDuty = getGuard(line)
        print("Guard begins ", guardOnDuty)
    elif "falls asleep" in line:
        asleepFrom = getTime(line)
        print("asleep from ", asleepFrom)
    elif "wakes up" in line:
        wakesUp = getTime(line)
        guardSleepingTime[guardOnDuty] += wakesUp-asleepFrom
        print("wake up ", wakesUp)
        for i in range(asleepFrom,wakesUp):
            guardPopularSleepingTime[guardOnDuty][i] +=1

laziestGuard = max(guardSleepingTime, key=guardSleepingTime.get)
tmp = max(guardPopularSleepingTime[laziestGuard])
most_asleep_min = guardPopularSleepingTime[laziestGuard].index(tmp))
print(most_asleep_min, "*",laziestGuard,"=",most_asleep_min*laziestGuard)

#part 2
freqGuard, _ = max(guardPopularSleepingTime.items(), key=lambda kv: max(kv[1]))
tmp = max(guardPopularSleepingTime[freqGuard])
most_asleep_min = guardPopularSleepingTime[freqGuard].index(tmp)
print(most_asleep_min, "*",freqGuard,"=",most_asleep_min*freqGuard)
