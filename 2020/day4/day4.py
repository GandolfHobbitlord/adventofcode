from pathlib import Path
import re

def check_height(x):
    ret = re.match(r'(\d{2,4})(cm|in)',x)
    if ret is None:
        return False
    height, unit = ret.groups()
    if unit == 'cm':
        return 150 <= int(height) <= 193
    elif unit == 'in':
        return 59 <= int(height) <= 76
    return False

valid = {
'byr' : lambda x : len(x) == 4 and 1920 <= int(x) <= 2002,
'iyr' : lambda x : len(x) == 4 and 2010 <= int(x) <= 2020,
'eyr' : lambda x : len(x) == 4 and 2020 <= int(x) <= 2030,
'hgt' : check_height,
'hcl' : lambda x : re.match(r'#[0-9a-f]{6}',x) != None,
'ecl' : lambda x : re.match(r'(amb|blu|brn|gry|grn|hzl|oth)$',x) != None,
'pid' : lambda x : re.match(r'\d{9}$',x) != None,
'cid' : lambda x : True,
}

def is_passport_valid(passport):
    # print(passport)
    if len(passport) == 8:
        return True
    elif len(passport) == 7 and "cid" not in passport.keys():
        return True
    else:
        return False

def valid_part2(passport):
    return all(valid[k](v) for k,v in passport.items())

def parse_passport(raw_passport):
    entries = re.split(r"\s",raw_passport)
    return dict(e.split(":") for e in entries)

def run_tests():
    with open(Path("2020") / "day4" / "day4_test.txt") as f:
        passports = [line for line in f.read().split("\n\n")]
    count = 0
    ans1 = [is_passport_valid(parse_passport(p)) for p in passports]
    assert ans1 == [True, False, True, False]

    assert valid["byr"]('2002')
    assert not valid["byr"]('2003')

    assert valid['hgt']('60in')
    assert valid['hgt']('190cm')
    assert not valid['hgt']('190in')
    assert not valid['hgt']('190')

    assert valid['hcl']('#123abc')
    assert not valid['hcl']('#123abz')
    assert not valid['hcl']('123abc')

run_tests()

with open(Path("2020") / "day4" / "day4_input.txt") as f:
    raw_passports = [line for line in f.read().split("\n\n")]

passports = [parse_passport(p) for p in raw_passports]
valid_pass = [p for p in passports if is_passport_valid(p)]

print(f"Part 1 Number of valid passports {len(valid_pass)}")
print(f"Part 2 Number of valid passports {sum([valid_part2(p) for p in valid_pass])}")