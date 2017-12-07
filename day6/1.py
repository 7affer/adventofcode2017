from functools import reduce

#input_string = '0 2 7 0'
input_string = '5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6'

input = [int(x) for x in input_string.split()]


def rearange_max(input):
    bank = max(enumerate(input), key=lambda x: x[1])
    input[bank[0]] = 0
    for i in range(bank[1]):
        index = (i + bank[0] + 1) % len(input)
        input[index] += 1
    return input

def get_key(input):
    return ' '.join([str(i) for i in input])

def rearange_array(input):
    history = [get_key(input)]
    step = 0
    while True:
        step += 1
        input = rearange_max(input)
        key = get_key(input)
        if key in history:
            return step
        history.append(key)
    return -1

print(rearange_array(input))