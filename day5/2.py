def maze_runner(maze):
    steps = 0
    position = 0
    while position >= 0 and position < len(maze):
        lastPosition = position
        offset = maze[position]
        position += offset
        maze[lastPosition] += 1 if offset < 3 else -1
        steps += 1
    return steps

file = open('day5/input.txt', 'r')
input = [int(x) for x in file.readlines()]

print(maze_runner([0, 3, 0, 1, -3]))
print(maze_runner(input))
