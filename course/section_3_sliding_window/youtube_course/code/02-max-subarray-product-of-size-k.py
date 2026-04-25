def pr[T](value: T, debug: bool = True) -> T:
    if debug:
        print(value)
    return value


def max_subarray_product(nums: list[int], k: int):
    current_product = 1
    for i in range(0, k):
        current_product *= nums[i]
    max_product = current_product
    print("nums = ", nums)
    for i in range(k, len(nums)):
        current_product *= nums[i]
        current_product /= nums[i - k]
        max_product = max(current_product, max_product)
    return max_product


result = max_subarray_product(nums=[1, 4, 1, 6, -3, 3, -5, 2, 26], k=4)
print(result)
