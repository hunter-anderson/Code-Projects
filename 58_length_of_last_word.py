"""
Given a string s consists of upper/lower-case alhabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Example:
    Input: "Hello World"
    Output: 5
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        if len(s) > 1:
            return len(s[-1])
        else:
            return 0

def test():
    s = "Hello World, my name is Hunter"
    sol = Solution()
    print(f"Length of last word for \'{s}\' is {sol.lengthOfLastWord(s)}")

test()
