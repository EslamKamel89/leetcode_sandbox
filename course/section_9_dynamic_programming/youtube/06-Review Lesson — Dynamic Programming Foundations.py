

def visualize_tribonacci(n):
    t0 , t1 , t2 = 0 , 1 , 1
    print(f"{t0=}, {t1=}, {t2=}")
    for step in range(3 , n+1):
        nxt = t0 + t1 + t2
        print(
            f"step = {step}",
            f"next = {nxt}"
        )
        t0 , t1 , t2 = t1 , t2 , nxt
        print(
            f"window -> "
            f"{t0}, {t1}, {t2}"
        )
    
    
# visualize_tribonacci(10)

def min_cost_visualize(cost:list[int]) :
    prev2 = cost[0]
    prev1= cost[1]
    print(f"{cost=}")
    print(f"{prev2=} , {prev1=}")
    for i in range(2 , len(cost)) :
        curr = cost[i] + min(prev2 , prev1)
        print(
            f"stair={i}",
            f"cost={curr}"
        )
        prev2, prev1 = prev1 , curr
    

# min_cost_visualize(
#     [1,100,1,1,100,1]
# )


def house_robber(nums:list[int]):
    print(f"{nums=}")
    prev2 = nums[0]
    prev1 = max(nums[0] , nums[1])
    print(f"house0={prev2}")
    print(f"house1={prev1}")
    for i in range(2 , len(nums)) :
        take = prev2 + nums[i]
        skip = prev1 
        curr = max(take , skip)
        print(
            f"house={i}",
            f"take={take}",
            f"skip={skip}",
            f"winner={curr}"
        )
        prev2 , prev1 = prev1 , curr
        
    
# house_robber([2,7,9,3,1])
def unique_paths(m:int, n:int):
    dp = [[1]* n for _ in range(m)]
    print(f"{dp=}")
    for r in range(1 , m):
        for c in range(1, n):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    for row in dp:
        print(row)
    return dp[-1][-1]

print(unique_paths(3,3))