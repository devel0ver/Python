################################
# Homework 3
# CISC 1215
# Points possible : 23 Points (17 + 5 extra-credit)
# Due data: March 9th 11:59 Pm
# General Note: All user inputs should have a prompt. If a problem requires user input it will be explicitly stated.
#               You are not allowed to import any libraries for this project
#               You can only use concepts discussed in class until Lecture 5
#               The inputs provided are examples, your code should work for any valid input
################################


"""
[3 Points] Remove duplicates
You will write a code that removes duplicates from a list, the list will only contain strings and numbers. You do not have to worry about nested lists.
Example run:
    input_list: [1,2,3,1,1,3,2,2,1]
    Expected output: [1,2,3]
Note1: You are not allowed to use set to accompolish this
Note2: You need to modify the list in place, that is you should not create a new list with duplicates removed. You can veriy this with id(), the list before and after should have the same ID. 
        The print statements before and after your code is to check that you are modifying the list in place. Do not remove them.
Note3: You should accompolish this with a for loop, while loop is not allowed
Note4: You can use list methods count, remove
Note5: You can create any additional lists or variables that you want
Note6: The order of the numbers in the returned list does not matter
"""
input_list=[1,2,3,1,1,3,2,2,1]
print(id(input_list))

#Write your code here

for num in input_list:
    count = input_list.count(num)
    # print("{} is {} times".format(num, count))
    if count > 1:
        for x in range(count - 1):
            input_list.remove(num)

print(input_list)
print(id(input_list))


"""
[5 Points] Comparing lists
You will write code to compare two lists (A and B), after comparison you will output one of the three:
    1) Two lists are equivalent - if they contain exactly same elements in any order
    2) A is a proper subset of B if B contains all the elements in A
    3) B is a proper subset of A if A contains all the elements in B
    4) Two lists are neither equivalent nor one subset of another
Example run:
    A: [[1,2,3],[1,2],3,4,5]
    B:[4,5]
    Expected output: B is a proper subset of A
Note1: You will use loops to solve this
Note2: You can use conditional statements and the membership operator
"""
A=[[1,2,3],[1,2],3,3,4,5]
B=[[1,2,3],[1,2],3,4,5]
#Write your code here
A_Subset_B = True
for num in A:
    if num not in B or len(A) == len(B):
        A_Subset_B = False
        break
if A_Subset_B and len(A) < len(B):
    print("A is a proper subset of B")

B_Subset_A = True
for num in B:
    if num not in A or len(A) == len(B):
        B_Subset_A = False
        break
if B_Subset_A and len(B) < len(A):
    print("B is a proper subset of A")

if not B_Subset_A and not A_Subset_B:
    both_equiv = True
    if len(A) == len(B):
        for num in A:
            if num not in B:
                both_equiv = False
                break
        if both_equiv:
            print("Two lists are equivalent")
        else:
            print("Two lists are neither equivalent nor one subset of another")
    else:
        print("Two lists are neither equivalent nor one subset of another")

        

"""
[5 Points] 2D sorting
You will write code to sort a 2D list conisting of numbers and return a 1D list of sorted numbers
Example run:
    A: [[1,2,3],[1,2],3,4,5]
    Expected output: [1,1,2,2,3,3,4,5]
Note1: You will use loops to solve this
Note2: You can you use the isinstance function to check if an element is a list or a number  https://docs.python.org/3/library/functions.html#isinstance
Note3: You can use any list method to achieve this
Note4: You can create a new list if you want to

"""
A=[[1,2,3],[1,2],3,4,5]
#Write your code here
B = []
for num in A:
    if isinstance(num, list):
        for element in num:
            B.append(element)
    else:
        B.append(num)
B.sort()
print(B)
    


"""
[4 Points] Substring check
You will receive two user inputs one will be the string and the other a substring
You should print True if the substring is in the string False otherwise
The input string and the substring can be of any arbitrary length
If there are multiple occurences of the substring in the string you can return True on the first occurence
Example run:
    string_input= "Hello there"
    substring_input="ll"
    Expected output: True
Note1: You will use for loops to solve this, while loop is not allowed
Note2: You cannot use any string methods to solve this
"""
#Write your code here
string_input = input("Please enter the string: ")
substring_input = input("Please enter the substring: ")
if substring_input in string_input:
    print(True)
else:
    print(False)



"""
[5 points Extra credit] Naive Spell checker
You will receive a sentence as a user input. The sentence will contain multiple words seperated by space
The user might have the following typos in the words:
    1) Additional special characters in a word. The special characters you should be looking for:$%#^* example: appl#e, ca&r, d%ad
    2) Additional numbers in a word. The numbers are from 0-9. Examples: ad4apter, foreig5n, jo5y
    3) More than two consecutive occurences of a character. If there are only two occurences that is a valid word. Examples: Diiisk, Doooot are invalid and Door is valid.
You should correct the typos in each word and output the modified sentence to the user
Example run:
    input_sentence: "Thiiis is a mis3ta%ke, please prrrrint the corr$ect senten5ce"
    Expected output: This is a mistake, please print the correct sentence
"""

#Write your code here
input_sentence = input("Please enter sentence: ")
words = input_sentence.split()

corrected_words = []
for word in words:
    corrected_word = ""
    count = 0
    for char in word:
        if char not in ("$", "%", "#", "^", "*") and not char.isdigit():
            if len(corrected_word) != 0 and char == corrected_word[-1]:
                count += 1
                corrected_word += char
                continue
            if count > 1:
                corrected_word = corrected_word[0:len(corrected_word)-count]
            count = 0
            corrected_word += char
    corrected_words.append(corrected_word)

corrected_sentence = " ".join(corrected_words)
print(corrected_sentence)