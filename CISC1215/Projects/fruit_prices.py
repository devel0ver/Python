# file_name = 'Fruit prices 2020.csv'
# file_obj = open(file_name)
# file_obj.writable()
# print(file_obj.read())

# def func(x,y):
#   try:
#     return x/y    
#   except ZeroDivisionError:
#     print("Some error occurred")
#     return y

# func(1,0)

# Recursive
def find_string_length(string):
    if string == "":
        return 0
    else:
        return 1+find_string_length(string[:-1])
    
# Iteritive    
def find_string_length(string):
    length = 0
    while string != "":
        length += 1
        string = string[:-1]
        return length
print(find_string_length('Hello'))