def hurdleRace(k, height):
    # Write your code here
    dose = 0
    maxnum = max(height)
    if k < maxnum:
        dose = maxnum - k
    # for num in height:
    #     if k < num:
    #         currmax = num
    #     maxnum = max(maxnum, currmax)
    #     dose = maxnum - k
    return dose
    
print(hurdleRace(7, [2,5,8,4,5,2]))

