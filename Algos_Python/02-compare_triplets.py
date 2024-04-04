def compareTriplets(a, b):
    # Write your code here
    length = len(a) if len(a) == len(b) else None
    alice_score = 0
    bob_score = 0
    for i in range(length):
        if a[i] > b[i]:
            alice_score += 1
        elif b[i] > a[i]:
            bob_score += 1
        else:
            continue
    scores = [alice_score, bob_score]
    return scores

print(compareTriplets([1,1,3], [3,2,1]))
            
