def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = list(set(ranked))
    ranked.sort(reverse=True)
    result = []
    l = len(ranked)
    
    for score in player:
        while (l > 0) and (score >= ranked[l-1]):
            l -= 1
        result.append(l+1)
    return result
    
    
print(climbingLeaderboard([100,100,50,40,40,20,10], [5,25,50,120]))