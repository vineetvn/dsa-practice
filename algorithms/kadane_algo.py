# Kadane’s Algorithm is a dynamic programming approach used to find the maximum sum
# of a contiguous subarray in an array of numbers. It efficiently tracks a running sum,
# resetting it when negative, while keeping track of the highest sum encountered, all in O(n) time complexity.

def max_sub_array_sum(arr):
    if not arr:
        return 0

    max_sum = float('-inf')
    current_sum = 0  # Stores the sum of the current sub-array

    for num in arr:
        current_sum += num  # Add the current element to current_sum

        if current_sum > max_sum:
            max_sum = current_sum  # Update max_sum if current_sum is greater

        if current_sum < 0:
            current_sum = 0  # Reset current_sum to 0 if it goes negative

    return max_sum


# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum sub-array sum:", max_sub_array_sum(arr))  # Output: 6
