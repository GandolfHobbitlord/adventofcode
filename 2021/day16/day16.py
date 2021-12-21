from pathlib import Path
bin_parse ={ '0' : '0000',
'1' : '0001',
'2' : '0010',
'3' : '0011',
'4' : '0100',
'5' : '0101',
'6' : '0110',
'7' : '0111',
'8' : '1000',
'9' : '1001',
'A' : '1010',
'B' : '1011',
'C' : '1100',
'D' : '1101',
'E' : '1110',
'F' : '1111' }

version_sum = 0

def run(data, pos=0):
    global version_sum
    if pos == 0:
        version_sum = 0
    version = data[pos:pos+3]
    version_sum += int(version,2)
    pos += 3
    typeID = int(data[pos:pos+3],2)
    pos += 3
    if typeID == 4:
        val = ''
        while True:
            # print(data[1:5])
            is_end = data[pos] == '0'
            pos += 1
            val += data[pos:pos+4]
            pos += 4
            if is_end:
                print(f'literal value {int(val,2)}')
                return pos
        # print(val)
    else:
        len_id = data[pos]
        pos += 1
        if len_id == '0':
            bit_len = 15
            tot_len = int(data[pos:pos+bit_len],2)
            pos += bit_len
            end_point = pos + tot_len
            while end_point > pos:
                pos = run(data, pos)
            return pos
        else:
            bit_len = 11
            num_of_packets = int(data[pos:pos+bit_len],2)
            pos += bit_len
            print(f'num of subpackets {num_of_packets}')
            for _ in range(num_of_packets):
                print('sub_packet')
                pos = run(data,pos)
            return pos

def parse_line(line):
    return "".join([bin_parse[char] for char in line])

def run_tests():
    inp = 'D2FE28'
    bin = parse_line(inp)
    # assert bin == '110100101111111000101000'
    # run(bin)
    # run(parse_line('38006F45291200'))
    # run(parse_line('EE00D40C823060'))
    # run(parse_line('8A004A801A8002F478'))
    # assert version_sum == 16

    run(parse_line('620080001611562C8802118E34'))
    assert version_sum == 12

    run(parse_line('C0015000016115A2E0802F182340'))
    assert version_sum == 23

    run(parse_line('A0016C880162017C3686B18A3D4780'))
    assert version_sum == 31
run_tests()

with open(Path("2021") / "day16" / "day16_input.txt") as f:
    bin = parse_line(f.read())
run(bin)
print(version_sum)