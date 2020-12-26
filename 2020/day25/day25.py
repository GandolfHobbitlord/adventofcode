def get_loop_size(key):
    ans = 1
    loop_size = 0
    while ans != key:
        loop_size +=1
        ans *= 7
        ans %= 20201227
    return loop_size


def encrypt(key,loop_size):
    return pow(key,loop_size,20201227)

def run_test():
    inp = 5764801
    assert get_loop_size(inp) == 8
    inp = 17807724
    assert get_loop_size(inp) == 11
    assert encrypt(inp,8) == 14897079

run_test()
card_key = 5099500
door_key = 7648211
print(encrypt(card_key,get_loop_size(door_key)))