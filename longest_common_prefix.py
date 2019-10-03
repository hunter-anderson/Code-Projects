#Longest Common Prefix
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while len(prefix):
                if prefix == s[:len(prefix)]:
                    break
                else:
                    prefix = prefix[:-1]
        return prefix


test1= ["flower", "flow", "flame"]
test2 = ["dog", "abcdef", "dig"]
test3 = ["caa", "cag", "aca"]
tests = [test1, test2, test3]
a = Solution()
for test in tests:
    print(a.longestCommonPrefix(test))
