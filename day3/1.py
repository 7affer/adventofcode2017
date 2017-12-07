def find_number(number):
    x = 0
    y = 0
    step = 1
    side = 0
    head = 1
    while head < number:
        for i in range(step):
            x += 1 if (side + 4) % 4 == 0 else 0
            y -= 1 if (side + 5) % 4 == 0 else 0
            x -= 1 if (side + 6) % 4 == 0 else 0
            y += 1 if (side + 7) % 4 == 0 else 0
            head += 1
            if head == number:
                return [x, y]
        side += 1
        step += 1 if side % 2 == 0 else 0
    return [0, 0]


#result = find_number(12)
result = find_number(312051)

print(abs(result[0]) + abs(result[1]))
