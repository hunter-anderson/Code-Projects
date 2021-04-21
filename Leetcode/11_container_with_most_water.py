"""
Given n non-negative integers a1, a2, ..., an, where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:
    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_water = 0
        left = 0
        right = len(height)-1
        while left != right:
            area = min(height[left], height[right]) * (right - left)
            if area > most_water:
                most_water = area
            if left < right:
                left += 1
            else:
                right -= 1
        return most_water

    def testSolution(self):
        input = [1,8,6,2,5,4,8,3,7]
        print(f"Input: {input}\nOutput: {self.maxArea(input)}")

"""
O(n^2) Solution
def maxArea(self, height: List[int]) -> int:
    most_water = 0
    for left in range(len(height)-1):
        for right in range(left, len(height)):
            area = min(height[left], height[right]) * (right - left)
            if area > most_water:
                most_water = area
    return most_water
"""

def main():
    a = Solution()
    a.testSolution()

if __name__ == "__main__":
    main()
