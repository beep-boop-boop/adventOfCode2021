from PIL import Image
board = [[int(num)for num in line.strip()] for line in open('inputs/day9.txt').readlines()]
sum_risks = 0
def in_board(board, row, col):
    return row in range(0, len(board)) and col in range(0, len(board[0]))
def get_4_neighbors(board, row, col):
    neighbors = []
    deltas = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1]
    ]
    for delta in deltas:
        if in_board(board, row + delta[0], col + delta[1]):
            neighbors.append(board[row + delta[0]][col + delta[1]])
    return neighbors
def is_low_point(board, row, col):
    return sum([1 if neighbor > board[row][col] else 0 for neighbor in get_4_neighbors(board, row, col)]) == len(get_4_neighbors(board, row, col))

def grow_basin(board, row, col, basin_num):
    if board[row][col] == 9:
        return 
    else:
        if row - 1 >= 0:
            if board[row - 1][col] > board[row][col]:
                board[row - 1][col] = basin_num
                grow_basin(board, row - 1, col, basin_num)
        if row + 1 < len(board):
            if board[row + 1][col] > board[row][col]:
                board[row + 1][col] = basin_num
                grow_basin(board, row + 1, col, basin_num)
        if col - 1 >= 0:
            if board[row][col - 1] > board[row][col]:
                board[row][col - 1] = basin_num
                grow_basin(board, row, col - 1, basin_num)
        if col + 1 < len(board[0]):
            if board[row][col + 1] > board[row][col]:
                board[row][col + 1] = basin_num
                grow_basin(board, row, col + 1, basin_num)
low_points = []
for row in range(len(board)):
    for col in range(len(board[0])):
        if is_low_point(board, row, col):
            sum_risks += board[row][col] + 1
            low_points.append([row, col])
print(sum_risks)
basins = board
basin_num = 10
for low_point in low_points:
    basins = grow_basin(board, low_point[0], low_point[1], basin_num)
    basins[low_point[0]][low_point[1]] = basin_num
    basin_num += 1

import numpy as np
import math
sizes = []
for num in range(10, len(low_points)):
    sizes.append(np.count_nonzero(np.ravel(basins) == num))

print(sorted(sizes, reverse = True))