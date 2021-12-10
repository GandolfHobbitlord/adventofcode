from pathlib import Path
import statistics
openers = set('([<{')
closers = set(')]>}')
match = {
         ')' : '(',
         '>' : '<',
         ']' : '[',
         '}' : '{'}

def get_invalid_char(inp):
    stack = []
    for char in inp:
        if char in openers:
            stack.append(char)
        elif char in closers:
            if stack[-1] != match[char]:
                return char #invalid closer
            stack.pop()
    return ''

def _get_closers(chars):
    closers = {v : k for k, v in match.items()}
    v = [closers[char] for char in reversed(chars)]
    return ''.join(v)

def get_closers(inp):
    stack = []
    for char in inp:
        if char in openers:
            stack.append(char)
        elif char in closers:
            if stack[-1] != match[char]:
                return char #invalid closer
            stack.pop()
    return _get_closers(stack)

def score2(chars):
    match = {
        ')' : 1,
        ']' : 2,
        '}' : 3,
        '>' : 4}
    score = 0

    for char in chars:
        score = score*5 + match[char]
    return score

def score1(char):
    match = {
        '' : 0,
         ')' : 3,
         ']' : 57,
         '}' : 1197,
         '>' : 25137}
    return match[char]
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
    print(len(incomplete))
    return statistics.median([score2(get_closers(line)) for line in incomplete])
with open(Path("2021") / "day10" / "day10_input.txt") as f:
   lines = [line for line in f.read().splitlines()]
print(part1(lines))
print(part2(lines))
