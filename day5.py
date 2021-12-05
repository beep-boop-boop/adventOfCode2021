file = open('inputs/day5.txt', 'r')
lines = [line.strip().split(' -> ') for line in file.readlines()]
lines = [
    [
        [int(num) for num in line[0].split(",")], 
        [int(num) for num in line[1].split(",")]
    ]
    for line in lines
    ]

lines_hor = [line for line in lines if line[0][1] == line[1][1]]
lines_vert = [line for line in lines if line[0][0] == line[1][0]]


row = [0] * 1000
field = []
for _ in range(1000):
    field.append(row.copy())

for line in lines_hor:
    delta_x = line[1][0] - line[0][0]
    for d in range(min(line[0][0], line[1][0]), min(line[0][0], line[1][0]) + abs(delta_x) + 1):
        field[d][line[0][1]] += 1

for line in lines_vert:
    delta_y = line[1][1] - line[0][1]
    for f in range(min(line[0][1], line[1][1]), min(line[0][1], line[1][1]) + abs(delta_y) + 1):
        field[line[0][0]][f] += 1

over2 = 0
for row in field:
    for cell in row:
        if cell >= 2:
            over2 += 1

print(over2)

lines_diag = []

for line in lines:
    try:
        gradient = (line[1][0] - line[0][0]) / (line[1][1] - line[0][1])
        intercept = line[0][1] - (gradient * line[0][0])
        if gradient == 1 or gradient == -1:
            lines_diag.append([line, (gradient, intercept)])
    except ZeroDivisionError:
        continue

for line in lines_diag:
    x1, x2 = line[0][0][0], line[0][1][0]
    gradient, intercept = line[1]
    for i in range(min(x1, x2), max(x1, x2) + 1):
        field[i][int((i * gradient) + intercept)] += 1

over2 = 0
for row in field:
    for cell in row:
        if cell >= 2:
            over2 += 1

print(over2)



    
