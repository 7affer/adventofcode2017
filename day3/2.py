def sum_surrounding(x, y, collection):
    sum = 0
    surrounding = [
        [-1, -1],
        [-1, 1],
        [1, 1],
        [1, -1],
        [0, -1],
        [-1, 0],
        [0, 1],
        [1, 0]
    ]
    for item in surrounding:
        key = '{},{}'.format(x + item[0], y + item[1])
        sum += collection[key] if key in collection else 0
    return sum


def find_number(number):
    x = 0
    y = 0
    step = 1
    side = 0
    head = 1
    collection = {'{},{}'.format(0, 0): 1}

    while head < number:
        for i in range(step):
            x += 1 if (side + 4) % 4 == 0 else 0
            y -= 1 if (side + 5) % 4 == 0 else 0
            x -= 1 if (side + 6) % 4 == 0 else 0
            y += 1 if (side + 7) % 4 == 0 else 0
            head = sum_surrounding(x, y, collection)
            collection['{},{}'.format(x, y)] = head
            if head >= number:
                return head
        side += 1
        step += 1 if side % 2 == 0 else 0
    return [0, 0]


print(find_number(312051))
