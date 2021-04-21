#Valid Parentheses
from typing import List
class Solution:
    def isValid(self, s:str) -> bool:
        if len(s) == 0:
            return True
        stack = [s[0]]
        complementary = {')': '(', ']': '[', '}': '{'}
        for c in s[1:]:
            if (len(stack)):
                if (c in complementary and complementary[c] == stack[-1]):
                    stack.pop()
                    continue
            stack.append(c)
        if (len(stack)):
            return False
        return True

################################################################################
#   Faster solution?
    def isValid_v2(self, s:str) -> bool:
        stack = []
        complementary = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if (c in complementary):
                stack.append(c)
            else:
                if (len(stack) == 0 or complementary[stack.pop()] != c):
                    return False
        return len(stack) == 0

################################################################################
#Testing Time
test1 = "()[]{}" #True
test2 = "{[()]}" #True
test3 = "{{{{{{)))}}}}}}" #False
test4 = "((()(())))" #True
test5 = "][][][][][][][][][][" #False
tests = [test1, test2, test3, test4, test5]
a = Solution()
for test in tests:
    print(a.isValid(test))
