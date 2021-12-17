from queue import PriorityQueue
grid = [[int(num) for num in line.strip()] for line in open('inputs/day15.txt').readlines()]

MAX_COL = len(grid[0]) - 1
MAX_ROW = len(grid) - 1
GOAL = (MAX_ROW, MAX_COL)

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
            neighbors.append([row + delta[0], col + delta[1]])
    return neighbors
def in_board(board, row, col):
    return row in range(0, len(board)) and col in range(0, len(board[0]))

def h_cost(coords): # the estimated (heuristic) cost between the current point and the goal
    return abs(MAX_COL - coords[1]) + abs(MAX_ROW - coords[0])

def g_cost(coords): # the cost to move to a particular node
    return grid[coords[0]][coords[1]]

def f_cost(coords):
    return g_cost(coords) + h_cost(coords)

def a_star(start):
    open_list = [start]
    g_costs = {start : 0}
    f_costs = {start : h_cost(start)}
    path = {}
    while len(open_list) != 0:
        current = open_list.pop(0)
        if current == GOAL:
            break
        path[tuple(current)] = []
        for neighbor in get_4_neighbors(grid, current[0], current[1]):
            potential_cost = g_costs[tuple(current)] + g_cost(neighbor)
            if potential_cost < g_costs.get(tuple(neighbor), float('inf')):
                path[tuple(current)] = neighbor
                g_costs[tuple(neighbor)] = potential_cost
                f_costs[tuple(neighbor)] = potential_cost + h_cost(neighbor)
                
                if neighbor not in open_list:
                    open_list.append(neighbor)
                    open_list = sorted(open_list, key = lambda x : f_cost(x))
    return g_costs[GOAL]

print(a_star((0, 0)))



