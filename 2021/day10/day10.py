from pathlib import Path
import statistics
match = {
         ')' : '(',
         '>' : '<',
         ']' : '[',
         '}' : '{'}

openers = set(match.values())

def get_invalid_char(input):
    stack = []
    for char in input:
        if char in openers:
            stack.append(char)
        else:
            if stack.pop() != match[char]:
                return char #invalid closer
    return ''

def find_matching_chars(chars):
    closers = {v : k for k, v in match.items()}
    v = [closers[char] for char in reversed(chars)]
    return ''.join(v)

def get_closers(inp):
    stack = []
    for char in inp:
        if char in openers:
            stack.append(char)
        else:
            if stack.pop() != match[char]:
                raise Exception('Corrupted line!')
    return find_matching_chars(stack)

def score2(chars):
    scorer = {
        ')' : 1,
        ']' : 2,
        '}' : 3,
        '>' : 4}

    score = 0
    for char in chars:
        score = score*5 + scorer[char]
    return score

def score1(char):
    scorer = {
        '' : 0,
         ')' : 3,
         ']' : 57,
         '}' : 1197,
         '>' : 25137}
    return scorer[char]

def run_tests():
    assert ''  == get_invalid_char('(((((((((())))))))))')
    assert '}' == get_invalid_char('{([(<{}[<>[]}>{[]{[(<()>')
    assert ')' == get_invalid_char('[[<[([]))<([[{}[[()]]]')
    assert ']' == get_invalid_char('[{[{({}]{}}([{[{{{}}([]')
    assert  '}}]])})]' == get_closers('[({(<(())[]>[[{[]{<()<>>')
    assert  '])}>' == get_closers('<{([{{}}[<[[[<>{}]]]>[]]')
    assert score2('])}>') == 294


run_tests()

def part1(lines):
    return sum([score1(get_invalid_char(line)) for line in lines])

def part2(lines):
    incomplete = [line for line in lines if not get_invalid_char(line)]
    return statistics.median([score2(get_closers(line)) for line in incomplete])

with open(Path("2021") / "day10" / "day10_input.txt") as f:
   lines = [line for line in f.read().splitlines()]

print(f"Answer part 1 {part1(lines)}")
print(f"Answer part 1 {part2(lines)}")
