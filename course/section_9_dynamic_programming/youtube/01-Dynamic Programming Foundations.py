

memo = {}
count = 0
def ways_dfs(n:int)->int:
    global count 
    count += 1 
    if n == 1 : return 1 
    if n == 2 : return 2 
    if n in memo : return memo[n]
    res = ways_dfs(n-1) + ways_dfs(n-2)
    memo[n] = res
    return res 

def ways_tabulation(n:int)->int:
    if n == 1 :
        return 1
    dp = [0]*(n+1)
    dp[1] = 1 
    dp[2] = 2 
    for i in range(3 , n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    return dp[n]
     

if __name__ == '__main__' :
    print(ways_dfs(8))
    print(ways_tabulation(8))