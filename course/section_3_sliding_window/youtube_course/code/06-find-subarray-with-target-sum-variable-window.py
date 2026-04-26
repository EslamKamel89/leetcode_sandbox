def find_subarray_sum(nums: list[int], target: int):
    start = 0
    window_sum = 0
    for end in range(len(nums)):
        window_sum += nums[end]
        if window_sum == target:
            return (start, end)
        while window_sum > target:
            window_sum -= nums[start]
            start += 1
    return None


result = find_subarray_sum(nums=[3, 1, 4, 9, 2, 1, 7, 3], target=10)
print(result)
