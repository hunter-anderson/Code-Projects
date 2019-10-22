import math
def solution(n):
    n = int(n)
    count = 0
    if n == 0:
        return count+1
    while n > 1:
        if n%2 == 0:
            n = n//2
        else:
            if (n == 3 or n%4 == 1):
                n -= 1
            else:
                n += 1

        #increment count
        count += 1
    return count
