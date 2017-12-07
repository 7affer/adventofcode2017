from functools import reduce

file = open('day2/input.txt', 'r')
input = [[int(n) for n in row.split()] for row in file.readlines()]

checksum = sum([abs(min(row) - max(row)) for row in input])

print(checksum)
