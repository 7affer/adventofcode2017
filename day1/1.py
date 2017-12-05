#input = '1111'
#input = '1122'
#input = '1234'
input = '91212129'

sum = 0

for i, val in enumerate(input):
    sum += int(val) if input[i] == input[i - 1] else 0

print(sum)
