from pathlib import Path


with open(Path("2024") / "day9" / "day9_input.txt") as f:
# with open(Path("2024") / "day9" / "day9_test.txt") as f:
    data = [int(c) for c in f.read()]

def print_disk(dd):
    x = [[id]*val for id, val in dd]
    s = ""
    for a in x:
        for b in a:
            if b is None:
                b = "."
            s+=str(b)
    return s

def calc_checksum(dd):
    i = 0
    ans = 0
    for id, num in dd:
        if id:
            for _  in range(num):
                ans += id * i
                i += 1
        else:
            i += num
    return ans

def parse_data(data):
    id = 0
    disk = []

    for i, val in enumerate(data):
        if i % 2 == 0:
            disk.append((id,val))
            id += 1
        else:
            disk.append((None,val))
    return disk

def get_index_of_first_fit(q, num_spaces_needed):
    for i, (id, num_vals) in enumerate(q):
        if id is None and num_spaces_needed <= num_vals:
            return i
    return None

disk = parse_data(data)
right = []
moved = set()
print_disk(disk +list(reversed(right)))
while disk:
    if disk[-1][0] is None:
        #is a space
        right.append(disk.pop())
    else:
        index = get_index_of_first_fit(disk, disk[-1][1])
        if index is None or disk[-1][0] in moved:
            #doesn't fit anywhere or moved
            right.append(disk.pop())
        else:
            moving_file = disk.pop()
            spaces_after = disk[index][1] - moving_file[1]
            disk[index] = moving_file
            disk.insert(index+1,(None, spaces_after))
            disk.insert(-1,(None,moving_file[1]))
            moved.add(moving_file[0])
            # print_disk(disk +list(reversed(right)))

#print_disk(reversed(right))

print(calc_checksum(reversed(right)))
