def longest_subarray_sum(nums, target):
    start = 0
    max_len = -1
    current_sum = 0
    for end in range(len(nums)):
        current_sum += nums[end]
        while current_sum > target:
            current_sum -= nums[start]
            start += 1
        if current_sum == target:
            length = end - start + 1
            max_len = max(max_len, length)
    return max_len


result = longest_subarray_sum(nums=[4, 3, 3, 2, 1, 5, 2, 3, 5, 10, 1], target=10)
print(result)
