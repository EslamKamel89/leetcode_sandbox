def pr[T](val: T, debug: bool = True, t="") -> T:
    if debug:
        print(t, val)
    return val


def count_subarrays_with_target(nums: list[int], k: int, target: int):
    current_sum = sum(nums[:k])
    count = 1 if current_sum == target else 0
    print("nums = ", nums)
    print("initial count = ", count)
    for i in range(k, len(nums)):
        print("------------------")
        print("i = ", i)
        current_sum += pr(nums[i], t="append")
        current_sum -= pr(nums[i - k], t="remove")
        print("current_sum = ", current_sum)
        if current_sum == target:
            count += 1
        print("count = ", count)
    return count


result = count_subarrays_with_target(
    nums=[2, 3, 2, 2, 3, 1, 3, 8, 5, 0, 2, 4], k=3, target=7
)
print("===========================================")
print("result = ", result)
