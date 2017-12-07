from functools import reduce

def min(row):
    return reduce(lambda x, y: x if x < y else y, row)

def max(row):
    return reduce(lambda x, y: x if x > y else y, row)

file = open('day2/input.txt', 'r')
input = [[int(n) for n in row.split()] for row in file.readlines()]

checksum = sum([abs(min(row) - max(row)) for row in input])

print(checksum)
