#Function "2sum" - from a list of integers, it finds two numbers that add
#up to desired 'target', and returns indeces of those two numbers.

class Solution:
    def twoSum(self, nums: [int], target: int,) -> [int]:
        complementary = {}
        for i in range(0,len(nums)):
            if target-nums[i] in complementary:
                return [complementary[target-nums[i]], i]
            else:
                complementary[nums[i]] = i
        return None

def main():
    a = Solution()
    test = [1, 4, 7, 11]
    print(a.twoSum(test, 12))

main()
