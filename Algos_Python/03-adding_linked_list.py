list1 = [9, 9]
list2 = [9, 24]
# list1 = [6, 2, 9, 1, 3]
# list2 = [5, 2, 7, 8]
# create an array
output = []
# store the length of array with the most elements
lonest_arr = max(len(list1), len(list2))
carry = 0
# iterating through both arrays untill the next node of each is null
for i in range(lonest_arr):
    val1 = list1[i] if i < len(list1) else list2[i]
    val2 = list2[i] if i < len(list2) else list1[i]
    
    sum = val1 + val2 + carry
    carry = sum // 10
    output.append(sum % 10)
    
if carry:
    output.append(carry)

print(output)
