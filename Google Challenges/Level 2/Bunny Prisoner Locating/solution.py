def solution(x, y):
    #id_start is sum for k=1 to x of k
    #id_end is sum for k=x to x+y-2 of k
    id_start = int(x * (x + 1) / 2)
    id_end = int((y - 1) * (2*x + y - 2) / 2)
    return str(id_start  + id_end)

print(solution(100000,100000))
