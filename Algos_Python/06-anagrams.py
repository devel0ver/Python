# Define a function with two arguments str1, str2
def anagram(str1, str2):
    # Create an empty dictionary 
    # EX: dictionary = {'a': 1, 'p':2, 'l':1, 'e':1}
    anagram_dict = {}
    # Declare a variable is_anagram and set it to False
    is_anagram = False
    
    # if len(str1) not equal len(str2)
    if len(str1) != len(str2):
        # return is_anagram(False)
        return is_anagram
    
    # loop through one of the strings
    for char in str1:
        # store the letter in the dictionary with the count of times it occurs
        anagram_dict[char] = anagram_dict.get(char, 0) + 1
        
    # loop through the other string 
    for char in str2:
        # check if the letter is in the dictionary
        if char in anagram_dict:
            # decrement the value of the key by 1
            anagram_dict[char] -= 1
            # If the values are below 0 (more char in str2 than str1), return false
            if anagram_dict[char] < 0:
                return is_anagram

        # otherwise := (if the letter is not in the dictionary)
        else:
            return is_anagram
    is_anagram = True
    # return is_anagram
    return is_anagram

print(anagram('go ', 'dog')) # False
print(anagram('tab', 'bat')) # True
print(anagram('app#le', 'p@aple')) # False