from pathlib import Path

def get_ID(seat_tuple):
    return seat_tuple[0]*8 + seat_tuple[1]

def get_row_and_column(partition):
    row = int(''.join(['1' if x == 'B' else '0' for x in partition[:7]]),2)
    column = int(''.join(['1' if x == 'R' else '0' for x in partition[7:]]),2)
    return row,column

def find_missing(sorted_ids):
    for id, x in enumerate(sorted_ids,start=sorted_ids[0]):
        if id != x:
            return id

def run_test():
    assert get_row_and_column('FBFBBFFRLR') == (44, 5)
    assert get_row_and_column('BFFFBBFRRR') == (70, 7)
    assert get_row_and_column('FFFBBBFRRR') == (14, 7)
    assert get_row_and_column('BBFFBBFRLL') == (102, 4)
    assert get_ID((44, 5)) == 357

run_test()

with open(Path("2020") / "day5" / "day5_input.txt") as f:
    tickets = [line for line in f.read().splitlines()]
ids = [get_ID(get_row_and_column(ticket)) for ticket in tickets]
ids.sort()
print(f'Max ID is {ids[-1]}')
print(f'Your seat is {find_missing(ids)}')
