from pathlib import Path
checked_numbers = []

# Next time I'm going to use a dict of tuples as i always do and not have to check limits....

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

def get_number(data,row,col):
    pos = col
    number = ''
    number_positions = set()
    while pos >=0 and pos < width and data[row][pos].isdigit():
        number += data[row][pos]
        number_positions.add((row,pos))
        pos += 1
    pos = col-1
    while pos >=0 and pos < width and data[row][pos].isdigit():
        number = data[row][pos] + number
        number_positions.add((row,pos))
        pos -= 1
    return int(number), number_positions

def find_gears(data):
    gear_ratios = []
    for row in range(height):
        for col in range(width):
            if data[row][col] == '*':
                neighbors = []
                uniques = set()
                for y in [row -1, row, row + 1]:
                    for x in [col -1, col, col +1]:
                        if y < 0 or y >= height:
                            continue
                        if x < 0 or x >= width:
                            continue
                        if data[y][x].isdigit():
                            num, positions = get_number(data,y,x)
                            if not positions & uniques:
                                neighbors.append(num)
                                uniques |= positions
                if len(neighbors) == 2:
                    gear_ratios.append(neighbors[0] * neighbors[1])
                print(neighbors)
    print(gear_ratios)
    print(sum(gear_ratios))
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

find_gears(data)
print(valids)
print(sum(valids))