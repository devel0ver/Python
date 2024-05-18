################################
#Project 3
# CISC 1215
# Points possible : 30 + 5
# Due date: May 4th 11:59 Pm
################################



#F1) 10 points
def fruit_price_dict(input_file):
    """Returns a dictionary containing the fruits and their Retail Price 
        Key: The key is a concatenation of the fruit name at its form separated by hyphen(-)
            The key for the fruit Apples, in form Fresh is: Apples-Fresh
        Value: The value is the Retail Price for the fruit in the form
        The example below shows the dictionary for the fruit apple alone, your returned dictionary 
        should have all the fruits in their different forms
        Example with apples alone:
            {"Apples-Fresh":1.5193, "Apples-Canned":1.066, "Apples-Juice":0.7804,"Apples-Frozen":0.5853}
    """ 
    #Write code here
    file_obj = open(input_file)
    # Initialize empty dictionary to store fruit-form: price
    fruit_dict = {}
    # Skip the first line which is the header
    file_obj.readline()
    # Iterate through each line in the file after the header
    for row in file_obj:
        # print(row)
        # Split into parts between any commas
        fruit_arr = row.rstrip().split(',')
        fruit_dict[f"{fruit_arr[0]}-{fruit_arr[1]}"] = float(fruit_arr[2])
    
    # Close the files when done working with them
    file_obj.close()
    return fruit_dict

fruit_prices = fruit_price_dict('./Fruit Prices 2020 P3.csv')
print(fruit_prices)
    
#F2) 3 points
def list_of_fruits(fruit_dict):
    """Returns the list of all the fruits in the dictionary
        The dictionary has the same key/value pairs defined in the function fruit_price_dict
    """
    #Write code here
    # Initialize empty set to store unique/distinct fruits
    fruit_set = set()
    # Iterate through the dictionary keys
    for fruits in fruit_dict.keys():
        # Split the hyphen in the key and get what is before it which is the fruit name
        fruit = fruits.split('-')[0]
        # Add the fruit name to the set
        fruit_set.add(fruit)
    # Convert the set to a list and return it
    return list(fruit_set)
    
print(list_of_fruits(fruit_prices))

#F3) 4 points
def list_of_juice_fruits(fruit_dict):
    """Returns the list of all the fruits that can purchased as a juice in the dictionary
        The dictionary has the same key/value pairs defined in the function fruit_price_dict
    """
    #Write code here
    fruit_set = set()
    for fruits in fruit_dict.keys():
        # Split the hyphen in the key and get what is before it which is the fruit name 
        # and after it which is the form
        fruit, fruit_form = fruits.split('-')
        # Check if the form is 'Juice'
        if fruit_form == "Juice":
            # Add the fruit to the set
            fruit_set.add(fruit)
    # Convert the set to a list and return it
    return list(fruit_set)
    
print(list_of_juice_fruits(fruit_prices))

#F4 6 points
def average_fruit_price(fruit_dict,fruit_list,form="Fresh"):
    """Returns average fruit price of the provided fruits in the list fruit_list
        The prices will be obtained from the dictionary fruit_dict
        The dictionary has the same key/value pairs defined in the function fruit_price_dict
    """
    #Write code here
    total_amount = 0
    fruit_count = 0
    
    # If the fruit is empty, we want to return 0
    if len(fruit_list) < 1:
        return 0
    
    # Loop through the fruit_list
    for fruit in fruit_list:
        # We want to concatenate the fruit name and its form with a hyphen. 
        # This key format matches how data is stored in fruit_dict.
        fruit = f'{fruit}-{form}'
        # Check if the fruit is in the dictionary
        if fruit in fruit_dict:
            # If it is, calculate the price
            total_amount += fruit_dict[fruit]
            fruit_count += 1
    # Compute the average
    average_fruit_price = total_amount / fruit_count
    return average_fruit_price
        
    
fruit_list = ['Apples', 'Grapes']
print(average_fruit_price(fruit_prices, fruit_list)) 

#F4 4 points
def high_priced_berry(fruit_dict,form="Fresh"):
    """Returns the most expensive berry in the form provided in the dictionary fruit_dict
        The dictionary has the same key/value pairs defined in the function fruit_price_dict
    """
    #Write code here
    max_price = 0
    # Iterate through the dictionary
    for key, value in fruit_dict.items():
        # Split the key into fruit name and form
        fruit, current_form = key.split('-')
        # Check if the form we get from dictionary equals to the form passed.
        # And check if 'berries' or 'berry' is in the fruit part of the key
        if current_form == form and ('berries' in fruit or 'berry' in fruit):
            # If is, check if the current price we getting is greater than what we have for the max price
            if value > max_price:
                # Whenever the value is greater, update mac_price to the current value(value)
                max_price = value
                # Update most_expensive_berry to the fruit with most price
                most_expensive_berry = fruit
    return most_expensive_berry

print(high_priced_berry(fruit_prices))     

#F4 3 points
def which_is_expensive(fruit_dict,fruit1,fruit2,form="Fresh"):
    """Compares two fruits retail prices and returns the fruit with higher price based on the prices in the dictionary fruit_dict
        The dictionary has the same key/value pairs defined in the function fruit_price_dict
    """  
    #Write code here
    fruit1_key = f'{fruit1}-{form}'
    fruit2_key = f'{fruit2}-{form}'
    
    # Check if both fruit keys are in the dictionary
    if fruit1_key in fruit_dict and fruit2_key in fruit_dict:
        # Get the prices for each fruit from the dictionaryy
        fruit1_price = fruit_dict[fruit1_key]
        fruit2_price = fruit_dict[fruit2_key]
        # Compare the prices and return the fruit with higher price
        if fruit1_price > fruit2_price:
            return fruit1
        elif fruit2_price > fruit1_price:
            return fruit2
        else:
            return 'The prices are equal'
    else:
        return 'One of the fruits is not in dictionary'
print(which_is_expensive(fruit_prices, 'Apples', 'Grapes')) 

#F4 5 points - Extra credit
def total_amount_to_be_paid(fruit_dict,fruit_list,form_list,pound_list):
    """Given a list of fruits, their form, and the quantity purchased, returns total amount to be paid for this purchase 
            based on the prices in the dictionary fruit_dict
        The dictionary has the same key/value pairs defined in the function fruit_price_dict
    """
    #Write code here
    total_amount = 0
    # Iterate through the lists
    if len(fruit_list) == len(form_list) == len(pound_list):
        # Expecting all have the same size of length, so just loop on one of the length
        for i in range(len(fruit_list)):
            # Initialize the key for the dictionary
            fruit_key = f'{fruit_list[i]}-{form_list[i]}'
            if fruit_key in fruit_dict:
                # Calculate cost for this fruit and add to total
                total_amount += fruit_dict[fruit_key] * pound_list[i]
        
    return total_amount
    
fruit_list = ['Apples', 'Grapes']
form_list = ['Juice', 'Fresh']
pound_list = [2, 3]
print(total_amount_to_be_paid(fruit_prices, fruit_list, form_list, pound_list)) 

