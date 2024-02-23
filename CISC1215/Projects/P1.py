################################
#Project 1
#CISC 1215
# Points possible : 30
# Due data: Feb 17th 11:59 Pm
# General Note: All user inputs should have a prompt
################################

'''
Example without user inputs
x is a variable 
y is a expression that increments x
Example run: 
    x=1
    Expected output: For variable 1 the output is 2
'''
x=1
y=x+1
print("For variable {} the output is {}".format(x,y))

'''
Example with user inputs
x is a user input variable 
y is a expression that doubles the value of x
Example run: 
    user inputs 2
    For variable 2 the output is 22
'''
x=input("Please enter the value for x:")
y=x+x
print("For variable {} the output is {}".format(x,y))


"""
[5 Points] Compute area of the circle
radius is a user input variable representing the radius of the circle
pi is a variable representing the value of pi
area is an expression computing the area for r
Example run:
    radius: 2
    Expected output: For radius 2 the computed area is 12.56
Note1: You can approximate pi with 3.14
Note2: You can use mathematical operators, type conversion functions, and format method as needed
"""

#Write your code here
raduis = float(input("Please enter the radius: "))
area = raduis * raduis
pi = 3.14
print("For radius {} the computed area is {}".format(raduis, area * pi))


"""
Mathematical operations
[7 points] Given a five digit integer check if it is a heterogram example: 00000 is not a heterogram and 12345 is
five_digit_number is a user input to obtain the five digit number (10000 to 99999)
Expected output if the number is a heterogram: True
Expected output if the number is not a heterogram: False
Example run:
    five_digit_number: 10342
    Expected output: True
Note1: You can use any mathematical operators, is operator, and any boolean operators
Note2: You are not allowed to use string operators or conditional statements
Note3: You can use type conversion functions as needed
Hint: See if modulo and floor division operators could help
"""

#Write your code here
five_digit_number = int(input("five_digit_number: "))
first_digit = five_digit_number // 10000
second_digit = (five_digit_number // 1000) % 10
third_digit = (five_digit_number // 100) % 10
fourth_digit = (five_digit_number // 10) % 10
fifth_digit = five_digit_number % 10

result = ((first_digit != second_digit) and (first_digit != third_digit) and 
          (first_digit != fourth_digit) and (first_digit != fifth_digit) and 
          (second_digit != third_digit) and (second_digit != fourth_digit) and
          (second_digit != fifth_digit) and (third_digit != fourth_digit) and
          (third_digit != fifth_digit) and (fourth_digit != fifth_digit)) 

print('Heterogram: {}'.format(result))



"""
[5 Points] String operations Pretty printing with Python
input_string is a user input string that a user wants to pretty print
star_count is a user input indicating number of stars (*) to append before and after the string
space_count is a user input indicating number of spaces between the star and the string
Example run:
    input_string: "Hello World"
    star_count: 5
    space_count:2
    Expected output: "*****  Hello World  *****"
Note1: The output should also include double quotes on both the ends     
Note2: You cannot use the format method for this, string operators are allowed (+ and *)
Note3: You can use mathematical operators, len and type conversion functions as needed
"""

#Write your code here
input_string = input("input_string: ")
star_count = int(input("# of stars: "))
space_count = int(input("# of spaces: "))
star_count = "*" * star_count
space_count = " " * space_count
result = '"' + star_count + space_count + input_string + space_count + star_count + '"'
print("Output: ", result)

"""
[8 points] String operations Pretty printing with Python
input_string is a user input string that a user wants to pretty print
star_count is a user input indicating number of stars (*) to append before and after the string
space_count is a user input indicating number of spaces between the star and the string
Example run:
    input_string: "Hello World"
    star_count: 5
    space_count:2
    Expected output: "*****  Hello World  *****"
Note1: The output should also include double quotes on both the ends     
Note2: You should only use the format method for this and string operators are not allowed
Note3: You can use other mathematical operators, len and type conversion functions as needed
"""

#Write your code here
input_string = input("input_string: ")
star_count = int(input("# of stars: "))
space_count = int(input("# of spaces: "))
stars = '{:*^{}}'.format('', star_count)
spaces = '{:^{}}'.format('', space_count)
print('"{}{}{}{}{}"'.format(stars, spaces, input_string, spaces, stars))


"""
[5 Points] Math operations Pretty printing with Python
input_number is a user input indicates the number that a user wants to pretty print
format_type is a user input  indicates format the user wants to use (example f, g, e, etc.) 
precision is a user input indicating the number of decimals after the decimal point
Example run:
    input_number: 12.34345
    format_type: f
    precision:2
    Expected output: 12.34
Note1: You should only use the format method
Note2: You can use type conversion functions as necessary
Note3: No conditional statements or concepts we have not covered in lectures are not allowed
"""

#Write your code here
input_number = float(input("input_number: "))
format_type = input("format_type: ")
precision = int(input("precision: "))
print("Output: {0:.{1}{2}}".format(input_number, precision, format_type))


"""
[3 Points] Extra credit: Numerical substring mathching
You will receive two user inputs:
input_number a five digit number, this will be primary string
substring_number a number from one to five digits, this will be the substring
If you identify the substring as part of the primary string your scipt should output True else False
Note1: You cannot use conditional statements, loops, or any string operations for this
Note2: You can use the len function for this
Note2: You can use mathematical and boolean operators for this
Hint: Solution for the problem 2 could help here
Example run1:
    input_number:34561
    substring_number:34
    Excepted output: True
Example run2:
    input_number:34561
    substring_number:72
    Excepted output: False
"""

#Write your code here
print("Example run1:")
input_number = int(input('input_number: '))
substring_number = int(input('substring_number: '))
substring_length = len(str(substring_number))
substring_divisor = 10 ** (5 - substring_length)
result = (input_number // substring_divisor) == substring_number

print("Output: {}".format(result))

print("\nExample run2:")
input_number = int(input('input_number: '))
substring_number = int(input('substring_number: '))
substring_length = len(str(substring_number))
substring_divisor = 10 ** (5 - substring_length)
result = (input_number // substring_divisor) == substring_number
print("Output: {}".format(result))
