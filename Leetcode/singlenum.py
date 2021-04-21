def singleNumber(nums):
    for i in range(1, len(nums)):
        nums[0] ^= nums[i]
    return nums[0]


test = [2,4,1,1,2]
print(singleNumber(test))
