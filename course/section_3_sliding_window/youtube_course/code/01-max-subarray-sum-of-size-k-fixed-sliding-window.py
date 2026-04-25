def pr[T](value: T, title="") -> T:
    print(title, value)
    return value


def max_subarray_sum1(nums: list[int], k: int):
    current_sum = sum(nums[:k])
    max_sum = current_sum
    print("nums = ", nums)
    for i in range(k, len(nums)):
        print("----------------------------")
        current_sum += nums[i]
        current_sum -= nums[i - k]
        print("window = ", nums[i - k + 1 : i + 1])
        max_sum = max(current_sum, max_sum)
        print("current_sum = ", current_sum)
        print("max_sum = ", max_sum)
    return max_sum


def max_subarray_sum(nums: list[int], k: int):
    max_sum = float("-inf")
    # print("nums = ", nums)
    for i in range(0, len(nums) - k + 1):
        # print("-----------------------------")
        # current_sum = pr(sum(pr(nums[i : i + k], "window")), "current_sum")
        current_sum = sum(nums[i : i + k])
        # max_sum = pr(max(max_sum, current_sum), "max_sum")
        max_sum = max(max_sum, current_sum)
    return max_sum


# result = max_subarray_sum1(nums=[1, 4, 1, 10, 25, 3, 5], k=4)
result = max_subarray_sum(nums=[1, 4, 1, 10, 25, 3, 5], k=4)
print(result)
