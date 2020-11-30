import numpy as np
import math
SERIAL_NUM = 1308
SIZE = 300
def calc_power(x,y, serial=SERIAL_NUM):
    rack_ID = (x+1) + 10
    power_level = rack_ID*(y+1)
    power_level +=serial
    power_level = power_level * rack_ID
    power_level = np.floor(power_level / 100) % 10 -5
    return power_level

assert(calc_power(2,4,8) == 4)
assert(calc_power(121,78,57) == -5)
assert(calc_power(216,195,39) == 0)
assert(calc_power(100,152,71) == 4)
def get_maximum(width):
        s=np.fromfunction(calc_power,((SIZE,SIZE)))
        res = np.zeros((SIZE,SIZE))
        for y in range(SIZE-width):
                for x in range(SIZE-width):
                        res[x,y]=sum(sum(s[x:x+width,y:y+width]))
        #print(s[19:19+5,59:59+5].transpose())
        maximum_val=res.max().max()
        location = np.where(maximum_val==res)
        print(width, maximum_val, location[0][0] + 1, location[1][0] + 1)
for i in range(1,300):
        get_maximum(i)