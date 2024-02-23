# def reverseString(str):
#     new_arr = []
#     for i in range(0,len(str), 1):
#         new_arr.append(str[i])
    
#     if len(str) < 1:
#         print("string is too short!")
    
#     return new_arr
# print(reverseString("hello"))
# print(reverseString(""))
# def loopList():
#     my_list = ["1", ["list", "in", "a", "walk"], 987]
    
#     for i in range(0, len(my_list), 1):
#         for j in  range(0, len(my_list), 1):
#             print(my_list[j])

# loopList()

# weekend = {"Sun": "Sunday", "Sat": "Saturday"}
# capitals = {}
# capitals["deu"] = "Berlin"
# capitals["12"] = "22"
# capitals["rma"] = "Real Madrid"

# print(weekend["Sat"])

# context = {
#     'questions': [
#         {
#             'id': 1, 
#             'content': 'Why is there light in the fridge and not in the freezer'
#         },
#         {
#             'id': 2, 
#             'content': 'Why don\'t sheep shrink when it rains'
#         },
#         {
#             'id': 3, 
#             'content': 'Why are they called apartments when they are all stuck together'
#         },
#         {
#             'id': 4, 
#             'content': 'Why do cars drive on the parkway and park on the driveway'
#         }
#     ]
# }
# print(context['questions'][2]['content'])

# def count():
#     # for(int i = 0; i < 101; i++)
#     for i in range(1, 101, 1):
    
#         if (i % 10 == 0):
#             print("Rma")
#         elif (i % 5 == 0):
#             print("Real")
#         else:
#             print(i)

# count()

friends = [
    {
        'first_name': 'Shaya', 
        'last_name': 'Ahmed',
        'pets': 
            [
                {
                    'name': 'Squigs', 
                    'type': 'turtle'
                },
                {
                    'name': 'Spike', 
                    'type': 'Dog'
                }
            ]
    },
    {
        'first_name': 'Eman', 
        'last_name': 'Mohammed', 
        'pets': 
            [
                {
                    'name':'Sqwuak', 
                    'type': 'Parrot'
                },
                {
                    'name': 'Oreo', 
                    'type': 'Cat'
                }
            ]
    }
]

def print_friend_info(dir):
    new_str = ""
    for i in range(0, len(dir), 1):
        # print(dir[i]['first_name']) 
        new_str += "\n\n" + dir[i]['first_name'] + " - "
        for j in range(0, len(dir[i]['pets']), 1):
            for key, val in dir[i]['pets'][j].items():
                new_str += f"\n{key} : {val} "
    return new_str
print(print_friend_info(friends))