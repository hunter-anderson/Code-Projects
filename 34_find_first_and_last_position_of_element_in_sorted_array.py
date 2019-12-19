"""
Given an array of integers nums sorted in ascending order, find the starting
and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found, return [-1, -1]

Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
"""
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        leftIndex, rightIndex = -1, -1

        while left <= right:
            mid = left + (right - left)//2
            if target == nums[mid]:
                leftIndex = self.searchLeft(nums, target, left, mid)
                rightIndex = self.searchRight(nums, target, mid, right)
                break
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1

        return [leftIndex, rightIndex]

    def searchLeft(self, nums: List[int], target: int, left: int, right: int) -> int:
        while left <= right:
            mid = left + (right - left)//2
            if target == nums[mid]:
                if mid == 0 or nums[mid-1] != target:
                    return mid
                else:
                    right = mid-1
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return -1

    def searchRight(self, nums: List[int], target: int, left: int, right: int) -> int:
        while left <= right:
            mid = left + (right - left)//2
            if target == nums[mid]:
                if mid == len(nums)-1 or nums[mid+1] != target:
                    return mid
                else:
                    left = mid+1
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return -1

    def testSolution(self):
        input = [5,5,5,5,5,5,5,5,5,5,5,5]
        target = 25
        print(f"Input: {input}\nOutput: {self.searchRange(input, target)}")


def main():
    a = Solution()
    a.testSolution()

if __name__ == "__main__":
    main()
