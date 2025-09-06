#1) Implement reverseString(str) that takes in a String, and then returns a string of the same length, but with the characters reversed.

# Example: "creature" ---> "erutaerc"

# ** Don't use the built-in reverse() method!

def reverseString(str):
    newArr = []
    # Loop through the string to access each letter, from end to start
    for letter in range(len(str)-1, -1, -1):
        newArr.append(str[letter])
        
    return "".join(newArr)

    
print(reverseString('Hello')) # 'olleH'

print(reverseString('creature')) # 'erutaerc'