def moveZeros(nums):
    count = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[count] = nums[count], nums[i]
            count += 1


array = [0, 3, 2, 0, 1, 0, 4, 0, 5, 6, 7]
moveZeros(array)
print(array)
