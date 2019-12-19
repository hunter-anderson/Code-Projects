"""
Given an array nums of n integers, are there elements a,b,c in nums such that
a+b+c=0? Find all unique triplets in the array which gives the sum of zero.

Note: Unique means solution must not contain duplicate triplets.

Example:
    Input: [-1, 0, 1, 2, -1, -4]
    Output: [[-1, 0, 1] [-1, -1, 2]]
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        for i in range(len(nums)-2):
            target = nums[i]
            if target > 0:
                break
            if i > 0 and nums[i-1] == target:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                total = target + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    sol.append([target, nums[left], nums[right]])
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while right > left and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
        return sol

    def testSolution(self):
        input = [-1, 0, 1, 2, -1, -4]
        print(f"Input: {input}\nOutput: {self.threeSum(input)}")


"""
unique = []
sol = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                a = [nums[i], nums[j], nums[k]]
                if set(a) not in unique:
                    unique.append(set(a))
                    sol.append(a)
return sol
"""

def main():
    a = Solution()
    a.testSolution()

if __name__ == "__main__":
    main()
