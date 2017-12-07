file = open('day2/input.txt', 'r')
input = [[int(n) for n in row.split()] for row in file.readlines()]

checksum = 0

for row in input:
    for x in row:
        for y in row:
            checksum += (x / y if x != y and x % y == 0 else 0)

print(checksum)
