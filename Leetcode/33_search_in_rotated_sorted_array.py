"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to
you beforehand.

(i.e., [0,1,2,3,4,5,6,7] might become [4,5,6,7,0,1,2,3])

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicates exists in the array.

Search complexity must be O(log(n))

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid

            if (target > nums[0]) != (nums[mid] > nums[0]):
                #if target and mid are not on same sorted side
                if target > nums[0]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                #same sorted side
                if target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
        return -1

    def testSolution(self):
        input = [12,13,14,15,16,17,0,1,2,3,4,5,6,7]
        target = 7
        print(f"Input: {input}\nOutput: {self.search(input, target)}")


def main():
    a = Solution()
    a.testSolution()

if __name__ == "__main__":
    main()
