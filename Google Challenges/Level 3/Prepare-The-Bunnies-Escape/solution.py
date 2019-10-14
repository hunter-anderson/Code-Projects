import heapq

#function to return the correct neighbors (no walls)
def neighbors(row_size, col_size, cur, map):
    #create children list and possible moves (NESW)
    children = []
    direction = [(0,1), (1,0), (0,-1), (-1,0)]

    #for each move, check if neighbor is in bound and not a wall
    for move in direction:
        x = cur[0] + move[0]
        y = cur[1] + move[1]
        if x >= 0 and x < row_size:
            if y >= 0 and y < col_size:
                if map[y][x] == 0:
                    #if correct move, append to children
                    children.append((x,y))
    return children

#path returns the total cost of the path from start to end
def path(parent, node):
    count = 2
    while parent[node] != (0,0):
        count += 1
        node = parent[node]
    return count

#returns manhattan distance between two points
def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

#A* algorithm that uses dicts to store info and python built-in minheap
def astar(map):
    #create start and initialize open_node list and dict of pointers to parents
    start = (0,0)
    open = []
    parents = {}

    #get maze dimensions and create start
    row_size = len(map[0])
    col_size = len(map)
    finish = (row_size-1, col_size-1)

    #initialize g and f maps with defaults of infinity
    gscore = {}
    fscore = {}
    for i in range(row_size):
        for j in range(col_size):
            gscore[(i,j)] = float('inf')
            fscore[(i,j)] = float('inf')

    #set start g and f value to 0 (first point, no cost)
    gscore[start] = 0
    fscore[start] = 0

    #create closed_node list and push start onto the minheap
    closed = []
    heapq.heappush(open, (fscore[start], start))

    #while open list isn't empty
    while len(open):
        #grab current node and check if found the end
        cur = heapq.heappop(open)[1]
        if cur == finish:
            return path(parents, cur)

        #add current node to visited nodes
        closed.append(cur)

        #check cost to travel to neighbor
        for neighbor in neighbors(row_size, col_size, cur, map):
            #if neighbor already visited, next iteration
            if neighbor in closed:
                continue

            #calculate new g score for neighbor
            g = gscore[cur] + dist(cur, neighbor)

            #if cost to neighbor is less than previously stored one, add to path
            if g < gscore[neighbor]:
                #store information in each map
                parents[neighbor] = cur
                gscore[neighbor] = g
                fscore[neighbor] = g + dist(cur, finish)

                #if neighbor already in path, continue
                for node in open:
                    if node[1] == neighbor:
                        continue
                heapq.heappush(open, (fscore[neighbor], neighbor))

    #no path could be found, return cost of infinity
    return float('inf')

def solution(map):
    #create temporary map to update walls and list of distances for each solve
    temp = list(map)
    distances = [astar(map)]

    #for every wall in map, break it, see if faster, then put back
    for i in range(len(map[0])):
        for j in range(len(map)):
            if map[j][i] == 1:
                temp[j][i] = 0
                distances.append(astar(temp))
                temp[j][i] = 1

    #return smallest distance
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
