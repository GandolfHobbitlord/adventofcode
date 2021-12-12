from collections import defaultdict

def create_connection_from_input(input):
    connections = defaultdict(list)
    for line in input.splitlines():
        src, dest = line.split('-')
        connections[src].append(dest)
        connections[dest].append(src)
    return connections

#path just for debug
def get_numb_ways(conn, src = 'start', visited = None, part1 = True, path = None):
    if not path:
        path = []
    if not visited:
        visited = []
    total = 0
    path.append(src)
    if src.islower():
        visited.append(src)
    for dest in conn[src]:
        if dest == 'start':
            continue
        elif dest == 'end':
            path.append(dest)
            total +=1
        else:
            if dest in visited:
                if part1:
                    continue
                else:
                    total += get_numb_ways(conn, dest, visited.copy(), True, path.copy())
            else:
                total += get_numb_ways(conn, dest, visited.copy(), part1, path.copy())
    return total

def part1(input):
    conn = create_connection_from_input(input)
    return get_numb_ways(conn)

def part2(input):
    conn = create_connection_from_input(input)
    return get_numb_ways(conn, part1=False)

def run_tests():
    input = 'start-A\nstart-b\nA-c\nA-b\nb-d\nA-end\nb-end'
    conn = create_connection_from_input(input)
    #assert 10 == get_numb_ways(conn)
    assert 36 == part2(input)
    input = 'dc-end\nHN-start\nstart-kj\ndc-start\ndc-HN\nLN-dc\nHN-end\nkj-sa\nkj-HN\nkj-dc'
    conn = create_connection_from_input(input)
    assert 19 == get_numb_ways(conn)

run_tests()
input = 'start-kc\npd-NV\nstart-zw\nUI-pd\nHK-end\nUI-kc\npd-ih\nih-end\nstart-UI\nkc-zw\nend-ks\nMF-mq\nHK-zw\nLF-ks\nHK-kc\nih-HK\nkc-pd\nks-pd\nMF-pd\nUI-zw\nih-NV\nks-HK\nMF-kc\nzw-NV\nNV-ks'
print(part1(input))
print(part2(input))
