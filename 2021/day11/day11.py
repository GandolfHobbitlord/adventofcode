import numpy as np
from scipy import signal
def to_matrix(inp):
    lines = [line for line in inp.splitlines()]
    mat=[]
    for line in lines:
        mat.append([int(char) for char in line])
    return np.array(mat)
    # return np.pad(np.array(mat), 1, mode='constant', constant_values=-np.Infinity)

def step(ener):
    flashes = 0
    already_flashed = np.zeros(ener.shape,dtype=bool)
    neigbors = np.ones((3,3),dtype=int)
    ener = ener + 1
    while True:
        new_flashes = (ener > 9) & (~already_flashed)
        flashes +=np.sum(new_flashes)
        new_increases = signal.convolve2d(new_flashes,neigbors,mode='same')
        ener = ener + new_increases
        already_flashed += new_flashes
        if not np.any(new_flashes):
            ener[ener>9]=0
            return ener, flashes

def get_flashes(ener,num_steps):
    tot_flashes = 0
    for _ in range(num_steps):
        ener, flashes = step(ener)
        tot_flashes += flashes
    return tot_flashes
def get_first_all_flashes(ener):
    flashes = 0
    steps = 0
    all_dumbos = ener.shape[0] * ener.shape[1]
    while flashes != all_dumbos:
        steps +=1
        ener, flashes = step(ener)
    return steps
def run_tests():
    inp = "11111\n19991\n19191\n19991\n11111"
    energies = to_matrix(inp)
    energies_after_1, flashes = step(energies)
    assert np.all(to_matrix('34543\n40004\n50005\n40004\n34543') == energies_after_1)
    energies_after_2, flashes = step(energies_after_1)
    assert np.all(energies_after_2 == to_matrix("45654\n51115\n61116\n51115\n45654"))
    assert flashes == 0

    inp = "5483143223\n2745854711\n5264556173\n6141336146\n6357385478\n4167524645\n2176841721\n6882881134\n4846848554\n5283751526"
    ener = to_matrix(inp)
    assert get_flashes(ener,num_steps=10) == 204
    assert get_flashes(ener,num_steps=100) == 1656
    assert get_first_all_flashes(ener) == 195
run_tests()

input= '4585612331\n5863566433\n6714418611\n1746467322\n6161775644\n6581631662\n1247161817\n8312615113\n6751466142\n1161847732'
mat = to_matrix(input)
print(get_flashes(mat,num_steps=100))
print(get_first_all_flashes(mat))

