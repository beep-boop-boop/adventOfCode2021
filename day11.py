octopi = [[int(num) for num in line.strip()] for line in open('inputs/day11small.txt').readlines()]
print(octopi)
def get_8_neighbors(board, row, col):
    neighbors = []
    if row - 1 >= 0:
        neighbors.append((row - 1, col))
        if col - 1 >= 0:
            neighbors.append((row - 1, col - 1))
        if col + 1 < len(board[0]):
            neighbors.append((row - 1, col + 1))
    if row + 1 < len(board):
        neighbors.append((row + 1, col))
        if col - 1 >= 0:
            neighbors.append((row + 1, col - 1))
        if col + 1 < len(board[0]):
            neighbors.append((row + 1, col + 1))
    if col - 1 >= 0:
        neighbors.append((row, col - 1))
    if col + 1 < len(board[0]):
        neighbors.append((row, col + 1))
    return neighbors

total_flashes = 0
def flash(octopi, row, col):
    global total_flashes
    global flashed
    if (row, col) in flashed:
        return
    else:
        flashed.append((row, col))
        total_flashes += 1
        octopi[row][col] = 0
        for neighbor in get_8_neighbors(octopi, row, col):
            octopi[neighbor[0]][neighbor[1]] += 1
            if octopi[neighbor[0]][neighbor[1]] > 9 and (neighbor[0], neighbor[1]) not in flashed:
                flash(octopi, neighbor[0], neighbor[1])

    return


for _ in range(2):
    flashed = []
    total_flashes = 0
    for x in range(len(octopi)):
        for y in range(len(octopi[0])):
            octopi[x][y] += 1
    for x in range(len(octopi)):
        for y in range(len(octopi[0])):
            if octopi[x][y] > 9 and (x, y) not in flashed:
                flash(octopi, x, y)
                flashed.append((x, y))
    

    print(total_flashes, flashed)
    for row in octopi:
        print(row)
