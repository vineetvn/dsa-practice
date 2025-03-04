def findClosestNumber(nums):
    closest = nums[0]

    for n in nums:
        if abs(n) < abs(closest):
            closest = n

    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    else:
        return closest


print(findClosestNumber([2, -1, 1]))
