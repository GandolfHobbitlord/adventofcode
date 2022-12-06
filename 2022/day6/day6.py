from pathlib import Path

with open(Path("2022") / "day6" / "day6_input.txt") as f:
    data = f.read()

def start_msg(data, start_len):
    for i in range(start_len,len(data)):
        if len(set(data[i-start_len:i])) == start_len:
            return i

print(f"Answer part 1: {start_msg(data, 4)}")
print(f"Answer part 2: {start_msg(data, 14)}")
