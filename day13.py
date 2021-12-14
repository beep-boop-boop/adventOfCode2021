file = open('inputs/day13.txt').readlines()
points = []
folds = []
for line in file:
    if 'fold' in line:
        folds.append([line.strip().split(" ")[2].split('=')[0], int(line.strip().split(" ")[2].split('=')[1])])
    elif line != ('\n'):
        points.append(tuple([int(num) for num in line.strip().split(',')]))

def part_1(points, command):
    if command[0] == 'x': # folding to the left, x variable changing
        for i in range(len(points)):
            if points[i][0] > command[1]:
                points[i] = (command[1] - (points[i][0] - command[1]), points[i][1])
    else:
        for i in range(len(points)):
            if points[i][1] > command[1]:
                points[i] = (points[i][0], command[1] - (points[i][1] - command[1]))
    return list(set(points))

print(f"part one: {len(part_1(points, folds[1]))}")
for fold in folds:
    points = part_1(points, fold)
max_x = max(point[0] for point in points)
max_y = max(point[1] for point in points)
grid = []
for _ in range(max_y + 1):
    grid.append(['  '] * (max_x + 1))

for x in range(max_x + 1):
    for y in range(max_y + 1):
        if (x, y) in points:
            grid[y][x] = '\u2B1C'
print('part two: ', end = '\n')
for row in grid:
    print("".join(row))

