def solution(n):
    if n == 0:
        return count+1
    while n > 0:
        #if not divisible by 2
        count += 1
        if (n%2):
            n -= 1
        else:
            n = n//2
    return count
