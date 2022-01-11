# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30
print(x)
print(students)
print(sports_directory)
print(z)


# 2. Iterate Through a List of Dictionaries
students = [
        {
            'first_name':  'Michael',
            'last_name' : 'Jordan'
        },
        {
            'first_name' : 'John', 
            'last_name' : 'Rosales'
        },
        {
            'first_name' : 'Mark', 
            'last_name' : 'Guillen'
        },
        {
            'first_name' : 'KB', 
            'last_name' : 'Tonel'
        }
    ]

def iterateDictionary(some_list):
    new_str = ""
    for i in range(0, len(some_list), 1):
        new_str += "first_name - " + some_list[i]['first_name'] + ","
        for j in range(1, len(some_list[i]), 1):
            new_str += " last_name - " + some_list[i]['last_name'] + "\n"
    return new_str
print(iterateDictionary(students))



# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list), 1):
        print(some_list[i][key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
print("\n-------------")



# 4. Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    print(str(7) + " LOCATIONS")
    for i in range(0, len(some_dict['locations']), 1):
        print(some_dict['locations'][i])
    print("\n-------------")
    print(str(8) + " INSTRUCTORS")
    for i in range(0, len(some_dict['instructors']), 1):
        print(some_dict['instructors'][i])

printInfo(dojo)