#Given a 32-bit SIGNED integer, reverse the digits.
#Return 0 if overflow.
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s2 = ""
        flag = 1
        for i in s[::-1]:
            if (i == '-'):
                flag = -1
                break
            s2 += i
        if (int(s2) > 2**31-1 or int(s2) < -2**31):
            return 0
        return flag * int(s2)


def main():
    a = Solution()
    test = 123
    print(a.reverse(120))

main()
