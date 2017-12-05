file = open('input.txt', 'r')

input = []

for line in file.readlines():
    row = [int(n) for n in line.split()]
    input.append(row)

checksum = 0


def min(row):
    val = row[0]
    for n in row:
        val = n if n < val else val
    return val


def max(row):
    val = row[0]
    for n in row:
        val = n if n > val else val
    return val


for row in input:
    checksum += abs(min(row) - max(row))

print(checksum)
