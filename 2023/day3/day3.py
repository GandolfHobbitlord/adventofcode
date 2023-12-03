from pathlib import Path

# Next time I'm going to use a dict of tuples as i always do and not have to check limits.... or line brakes,

def is_part_number(data,curr_number,row,col):
    valid = False
    for y in [-1,0,1]:
        for x in range(len(curr_number)+2):
            yy = row + y
            xx = col - x
            if yy < 0 or yy >= height or  xx < 0 or xx >= width:
                continue
            if data[yy][xx] != '.' and not data[yy][xx].isdigit():
                valid = True
    return valid

def get_number(data,row,col):
    pos = col
    number = ''
    number_positions = set()
    # lets look to the right
    while pos >=0 and pos < width and data[row][pos].isdigit():
        number += data[row][pos]
        number_positions.add((row,pos))
        pos += 1
    pos = col-1
    # and to the left
    while pos >=0 and pos < width and data[row][pos].isdigit():
        number = data[row][pos] + number
        number_positions.add((row,pos))
        pos -= 1
    return int(number), number_positions

def get_gear_ratios(data):
    gear_ratios = []
    for row in range(height):
        for col in range(width):
            if data[row][col] == '*':
                neighbors = []
                uniques = set()
                for y in [row -1, row, row + 1]:
                    for x in [col -1, col, col +1]:
                        if y < 0 or y >= height or x < 0 or x >= width:
                            continue
                        if data[y][x].isdigit():
                            num, positions = get_number(data,y,x)
                            if not positions & uniques:
                                # we haven't seen these positions before ie. not the same number
                                neighbors.append(num)
                                uniques |= positions
                if len(neighbors) == 2:
                    gear_ratios.append(neighbors[0] * neighbors[1])
    return gear_ratios

with open(Path("2023") / "day3" / "day3_input.txt") as f:
    data = [list(x) for x in f.read().splitlines()]

width = len(data[0])
height = len(data)
curr_number = ''

def get_part_numbers(data):
    valids = []

    for row in range(height):
        curr_number = ''
        for col in range(width):
            if data[row][col].isdigit():
                curr_number += data[row][col]
            else:
                if curr_number and is_part_number(data, curr_number,row,col):
                    valids.append(int(curr_number))
                curr_number = ''
            if col == width-1:
                if curr_number and is_part_number(data, curr_number,row,col+1): # This took forever to find, never again
                    valids.append(int(curr_number))
                curr_number = ''
    return valids

ans1 = sum(get_part_numbers(data))
ans2 = sum(get_gear_ratios(data))
print(ans1)
print(ans2)