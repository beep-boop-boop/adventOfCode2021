import numpy as np
from collections import Counter
edges = [line.strip().split("-") for line in open('inputs/day12.txt')]
for node in [line.strip().split("-") for line in open('inputs/day12.txt')]:
    edges.append([node[1], node[0]])
nodes = set(np.ravel(edges))

def is_small_cave(node):
    return (node.lower() == node)

paths = 0
visited = {}
for node in nodes:
    visited[node] = 0

def count_paths(start, finish, visited, max_visits_per_small_cave):
    global paths
    if is_small_cave(start):
        visited[start] += 1
    if start == finish:
        paths += 1
    else:
        neighbors = [edge for edge in edges if edge[0] == start]
        for neighbor in neighbors:
            if is_small_cave(neighbor[1]):
                if visited[neighbor[1]] == 0:
                    count_paths(neighbor[1], finish, visited, max_visits_per_small_cave)
                elif (visited[neighbor[1]] == 1) and (neighbor[1] not in ['start', 'end']): # cannot visit start and end more than once
                    if max_visits_per_small_cave not in list(visited.values()):
                       count_paths(neighbor[1], finish, visited, max_visits_per_small_cave) 
            else:
                count_paths(neighbor[1], finish, visited, max_visits_per_small_cave)
    if is_small_cave(start):
        visited[start] -= 1

count_paths('start', 'end', visited, 1)
print(paths)
paths = 0
count_paths('start', 'end', visited, 2)
print(paths)
