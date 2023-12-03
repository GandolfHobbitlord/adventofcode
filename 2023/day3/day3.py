from pathlib import Path
checked_numbers = []
def is_valid(data,curr_number,row,col):
    checked_numbers.append(int(curr_number))
    valid = True
    for y in [-1,0,1]:
        for x in range(len(curr_number)+2):
            yy = row + y
            xx = col - x
            if yy < 0 or yy >= height:
                continue
            if xx < 0 or xx >= width:
                continue
            if not data_copy[yy][xx].isdigit():
                data_copy[yy][xx] = 'x'
            if data[yy][xx] != '.' and not data[yy][xx].isdigit():
                valid = False
    return valid
with open(Path("2023") / "day3" / "day3_input.txt") as f:

    data = [list(x) for x in f.read().splitlines()]
data_copy = [x[:] for x in data]

width = len(data[0])
height = len(data)
curr_number = ''
valids = []

for row in range(height):
    curr_number = ''
    for col in range(width):
        if data[row][col].isdigit():
            curr_number += data[row][col]
        else:
            if curr_number and not is_valid(data, curr_number,row,col):
                valids.append(int(curr_number))
            curr_number = ''
        if col == width-1:
            if curr_number and not is_valid(data, curr_number,row,col+1): # This took forever to find
                valids.append(int(curr_number))
            curr_number = ''

print(valids)
print(sum(valids))