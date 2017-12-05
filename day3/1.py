import math
import string

number = 312051
# number = 12
matrix_side = math.ceil(number ** 0.5) * 2

matrix = []
for i in range(matrix_side):
    matrix.append([0 for x in range(matrix_side)])

head = 1
midx = math.floor(matrix_side / 2)
midy = math.floor(matrix_side / 2)
x = midx
y = midy
result = []
step = 1
matrix[x][y] = head


def inc_head(x, y, head, number):
    matrix[x][y] = head
    if head == number:
        return True
    return False


while head < number:
    matrix[x][y] = head
    # right
    for i in range(step):
        x += 1
        head += 1
        result = [x,y] if inc_head(x, y, head, number) else result
    # top
    for i in range(step):
        y -= 1
        head += 1
        result = [x,y] if inc_head(x, y, head, number) else result
    step += 1
    # left
    for i in range(step):
        x -= 1
        head += 1
        result = [x,y] if inc_head(x, y, head, number) else result
    # down
    for i in range(step):
        y += 1
        head += 1
        result = [x,y] if inc_head(x, y, head, number) else result
    step += 1

# for row in matrix:
#     str_row = '\t'.join([str(x) for x in row])
#     print(str_row)

print(abs(midx - result[0]) + abs(midy - result[1]))
