from pathlib import Path
s2d = {'2' : 2, '1': 1, '0': 0, '-' : -1, '=' : -2}
d2s = '012=-'

def snafu2dec(snaf):
    ans = 0
    for pos, val in enumerate(reversed(snaf)):
        ans += s2d[val] * 5 ** pos
    return ans

def dec2snafu(dec):
    ans = ""
    while dec !=0:
        ans = d2s[dec % 5] + ans
        dec = (dec + 2) // 5
    return ans


def tests():
    assert snafu2dec('1=-0-2') ==     1747
    assert snafu2dec( '12111') ==      906
    assert snafu2dec(  '2=0=') ==      198
    assert snafu2dec(    '21') ==       11
    assert snafu2dec(  '2=01') ==      201
    assert snafu2dec(   '111') ==       31
    assert snafu2dec( '20012') ==     1257
    assert snafu2dec(   '112') ==       32
    assert snafu2dec( '1=-1=') ==      353
    assert snafu2dec(  '1-12') ==      107
    assert snafu2dec(    '12') ==        7
    assert snafu2dec(    '1=') ==        3
    assert snafu2dec(   '122') ==       37
    assert dec2snafu(11) == '21'
    assert dec2snafu(5) == '10'
    assert dec2snafu(12345) == '1-0---0'
    assert dec2snafu(314159265) == '1121-1110-1=0'
tests()

with open(Path("2022") / "day25" / "day25_input.txt") as f:
    data = f.read().splitlines()

print(dec2snafu(sum([snafu2dec(snaf) for snaf in data])))