import numpy as np
from scipy import signal

def to_matrix(inp):
    lines = [line for line in inp.splitlines()]
    mat=[]
    for line in lines:
        mat.append([int(char) for char in line])
    return np.array(mat)

def step(dumbos):
    flashes = 0
    already_flashed = np.zeros(dumbos.shape, dtype=bool)
    neigbors = np.ones((3, 3), dtype=int)
    dumbos = dumbos + 1
    while True:
        new_flashes = (dumbos > 9) & ~already_flashed
        flashes +=np.sum(new_flashes)
        new_increases = signal.convolve2d(new_flashes, neigbors, mode='same')
        dumbos = dumbos + new_increases
        already_flashed += new_flashes
        if not np.any(new_flashes):
            dumbos[dumbos > 9] = 0
            return dumbos, flashes

def get_flashes(dumbos,num_steps):
    tot_flashes = 0
    for _ in range(num_steps):
        dumbos, flashes = step(dumbos)
        tot_flashes += flashes
    return tot_flashes

def get_first_all_flashes(dumbos):
    flashes = 0
    steps = 0
    all_dumbos = dumbos.shape[0] * dumbos.shape[1]
    while flashes != all_dumbos:
        steps +=1
        dumbos, flashes = step(dumbos)
    return steps

def run_tests():
    inp = "11111\n19991\n19191\n19991\n11111"
    dumbos = to_matrix(inp)
    dumbos_after_1, flashes = step(dumbos)
    assert np.all(to_matrix('34543\n40004\n50005\n40004\n34543') == dumbos_after_1)
    dumbos_after_2, flashes = step(dumbos_after_1)
    assert np.all(dumbos_after_2 == to_matrix("45654\n51115\n61116\n51115\n45654"))
    assert flashes == 0

    inp = "5483143223\n2745854711\n5264556173\n6141336146\n6357385478\n4167524645\n2176841721\n6882881134\n4846848554\n5283751526"
    dumbos = to_matrix(inp)
    assert get_flashes(dumbos,num_steps=10) == 204
    assert get_flashes(dumbos,num_steps=100) == 1656
    assert get_first_all_flashes(dumbos) == 195
run_tests()

input= '4585612331\n5863566433\n6714418611\n1746467322\n6161775644\n6581631662\n1247161817\n8312615113\n6751466142\n1161847732'
dumbos = to_matrix(input)

print(f'Answer part 1 {get_flashes(dumbos, num_steps=100)}')
print(f'Answer part 2 {get_first_all_flashes(dumbos)}')

