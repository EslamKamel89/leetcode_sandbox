def rob(nums:list[int]):
    if not nums :
        return 0 
    if len(nums) <= 2 :
        return max(nums)
    # prev2 , prev1 , curr 
    prev2 = nums[0]
    prev1 = max(nums[0] , nums[1])
    for i in range(2 , len(nums)) : 
        curr = max(prev1 , prev2+ nums[i])
        prev2 , prev1 = prev1 , curr 
    return prev1



if  __name__ == '__main__' :
    print(rob([2,7,9,3,1]))