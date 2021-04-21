#Leetcode url - https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#Straight forward - keep track of the previous non-duplicate, and keep increasing
#                   until the end of the array.
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        j = 1
        temp = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == temp:
                continue
            else:
                nums[j] = nums[i]
                temp = nums[j]
                j += 1
        return j

################################################################################
test = [0,0,1,1,1,2,2,3,3,4]
a = Solution()
print(a.removeDuplicates(test))
