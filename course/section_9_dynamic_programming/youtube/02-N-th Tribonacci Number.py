memo = {}
def dfs(n:int)->int :
    if n == 0 :
        return 0 
    if n <= 2 :
        return 1
    
    res = dfs(n-1) + dfs(n-2) + dfs(n-3)
    memo[n] = res 
    return res 


def tabular(n:int) ->int :
    if n == 0 :
        return 0 
    if n <= 2 :
        return 1
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3 , n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp [i-3]
    return dp[n]

def tabular2(n:int) ->int :
    if n == 0 :
        return 0 
    if n <= 2 :
        return 1
    dp = [0] * (n+1)
    t0 , t1 , t2 = 0 , 1 ,1 
    for i in range(3, n+1):
        t0 , t1 , t2 = t1, t2 , t0 + t1 + t2 
    return t2

if __name__ == '__main__' :
    print(dfs(10))
    print(tabular(10))
    print(tabular2(10))