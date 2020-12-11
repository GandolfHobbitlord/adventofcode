
def run_tests():
    inp = [16,10,15,5,1,11,7,19,6,12,4]
    inp.append(0)
    inp.sort()
    inp.append(inp[-1]+3)
    print(inp)

run_tests()
