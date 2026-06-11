
def min_cost(cost:list[int])->int :
    if not cost :
        return 0 
    if len(cost) == 1 :
        return cost[0]
    # prev2 , prev1 , current
    prev1 = cost[1]
    prev2 = cost[0]
    
    for i in range(2 , len(cost)) :
        current = cost[i] + min(prev1 , prev2)
        prev2 , prev1 = prev1 , current 
        
    return min(prev1,prev2)
    



cost = [10,15,20]

if __name__ == '__main__':
    print(min_cost(cost))