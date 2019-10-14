#A* implementation with a custom priority queue
import heapq
import random

def neighbors(row_size, col_size, cur, map):
    children = []
    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    for move in direction:
        x = cur[0] + move[0]
        y = cur[1] + move[1]
        if x >= 0 and x < row_size:
            if y >= 0 and y < col_size:
                if map[y][x] == 0:
                    children.append((x,y))
    return children

def path(parent, node):
    count = 2
    while parent[node] != (0,0):
        count += 1
        node = parent[node]
    return count

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(map):
    start = (0,0)
    open = []
    parents = {}

    row_size = len(map[0])
    col_size = len(map)
    finish = (row_size-1, col_size-1)

    gscore = {}
    fscore = {}
    for i in range(row_size):
        for j in range(col_size):
            gscore[(i,j)] = float('inf')
            fscore[(i,j)] = float('inf')

    gscore[start] = 0
    fscore[start] = 0

    closed = []
    heapq.heappush(open, (fscore[start], start))


    while len(open):
        cur = heapq.heappop(open)[1]
        if cur == finish:
            return path(parents, cur)

        closed.append(cur)

        for neighbor in neighbors(row_size, col_size, cur, map):
            if neighbor in closed:
                continue
            g = gscore[cur] + dist(cur, neighbor)
            if g < gscore[neighbor]:
                parents[neighbor] = cur
                gscore[neighbor] = g
                fscore[neighbor] = g + dist(cur, finish)
                for node in open:
                    if node[1] == neighbor:
                        break
                heapq.heappush(open, (fscore[neighbor], neighbor))

    return float('inf')

def solution(map):
    temp = list(map)
    distances = [astar(map)]
    for i in range(len(map[0])):
        for j in range(len(map)):
            if map[j][i] == 1:
                temp[j][i] = 0
                distances.append(astar(temp))
                temp[j][i] = 1
    return min(distances)

test = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(solution(test))
