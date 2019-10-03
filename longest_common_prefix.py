#Leetcode url - https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while (prefix not in strs[i]):
                prefix = prefix[:-1]
                if not len(prefix):
                    return ""
        return prefix
