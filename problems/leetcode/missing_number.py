from typing import List


def missingNumber(nums: List[int]) -> int:
    n = len(nums)

    sum_of_n = n * (n + 1) // 2
    sum_of_nums = 0

    for i in nums:
        sum_of_nums += i

    return sum_of_n - sum_of_nums


print(missingNumber([3, 0, 1]))
