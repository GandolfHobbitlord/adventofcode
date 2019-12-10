import numpy as np
import matplotlib.pyplot as plt
import os

def part1(image):
    max_layer = np.argmax([np.count_nonzero(image[:,:,i]) for i in range(image.shape[-1])])
    l = image[:,:,max_layer]
    return np.count_nonzero(l[l == 1]) *  np.count_nonzero(l[l == 2])

def part2(image):
    decoded_image = image[:,:,0]
    for i in range(image.shape[-1]):
        decoded_image = np.where(decoded_image != 2,decoded_image,image[:,:,i])
    return decoded_image

with open(os.path.join("day8","input_day8.txt")) as f:
    data = [int(i) for i in f.read().strip('\n')]
    image = np.array(data)
    image = np.reshape(image,(25,6,-1),order={'F'})
    
    print("Answer part 1: {}".format(part1(image)))
    decoded_image = part2(image)
    plt.imshow(np.transpose(decoded_image), cmap='gray', vmin=0, vmax=2)
    plt.show()