def solution(x, y):
    m = int(x) if int(x) > int(y) else int(y)
    f = int(x) if int(x) < int(y) else int(y)
    gen = 0
    if m < 1 or f < 1:
        return "impossible"
    while (m-f) > 0:
        if (m%f == 0):
            #f must be a factor or 1, if factor it's impossible
            if f == 1:
                return str(gen + m - 1)
            else:
                return "impossible"
        else:
            #set m as remainder of m/f and correct gen
            gen += m // f
            m = m % f
            #update m and f
            if (m < f):
                temp = m
                m = f
                f = temp
    if m == 1 and f == 1:
        return str(gen)
    else:
        return "impossible"

for i in range(1, 10):
    for j in range(1, 10):
        print(solution(i, j))
