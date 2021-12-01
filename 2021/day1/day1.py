from pathlib import Path
with open(Path("2021") / "day1" / "day1_input.txt") as f:
   num = [int(x) for x in f.read().splitlines()]

increase = 0
decrease = 0
# for i in range(1,len(num)):
#    if num[i-1] < num[i]:
#       increase += 1
#    else:
#       decrease += 1

for i in range(3,len(num)):
   prev = sum(num[i-3:i])
   now = sum(num[i-2:i+1])
   if prev < now:
      increase += 1
   else:
      decrease += 1
print(increase)