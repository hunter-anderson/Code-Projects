def maxSubArray(nums):
    total = nums[0]
    temp = nums[0]
    for i in range(1, len(nums)):
        if temp + nums[i] < nums[i]:
            temp = nums[i]
            total = temp
        else:
            temp += nums[i]
            if temp > total:
                total = temp
    return total

def v2(nums):
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)

test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(test))
print(v2(test))
