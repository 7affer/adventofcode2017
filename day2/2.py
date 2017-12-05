file = open('input.txt', 'r')

input = []

for line in file.readlines():
    row = [int(n) for n in line.split()]
    input.append(row)

checksum = 0


def even_divide(x, y):
    res = x / y
    return res - int(res) == 0


for row in input:
    for x in row:
        for y in row:
            checksum += (x / y if x != y and even_divide(x, y) else 0)

print(checksum)
