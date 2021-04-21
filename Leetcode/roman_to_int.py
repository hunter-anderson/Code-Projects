#Leetcode url - https://leetcode.com/problems/roman-to-integer/
#Used a dictionary for constant look up times, with O(n) run-time cost
#to iterate over the string to calculate conversion.
#Date Solved - 10/2/2019
class Solution:
    def romanToInt(self, s: str) -> int:
        conv_table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        prev = ''
        for c in s:
            total += conv_table[c]
            if prev != '':
                if (prev == 'I') and (c == 'V' or c == 'X'):
                    total -= 2
                elif (prev == 'X') and (c == 'L' or c == 'C'):
                    total -= 20
                elif (prev == 'C') and (c == 'D' or c == 'M'):
                    total -= 200
            prev = c
        return total
