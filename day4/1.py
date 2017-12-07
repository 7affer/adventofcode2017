from functools import reduce


def validate_string(value):
    words = sorted(value.split())
    lastword = ''
    for word in words:
        if word == lastword:
            return False
        lastword = word
    return True


print(validate_string('aa bb cc dd'))
print(validate_string('aa bb cc aa'))
print(validate_string('aa bb cc aaa'))

file = open('day4/input.txt', 'r')

counter = sum([(1 if validate_string(y) else 0) for y in file.readlines()])

print(counter)
