five_letter_word = ['a', 'p', 'p', 'l', 'e']
five_letter_word_length = len(five_letter_word)
attempts = 5
correct = 0
while attempts > 0:
    if correct == five_letter_word_length:
        print("Success!")
        break
    
    user_input = input("Guess a letter: ")
    
    # Conditional statement checking if the length of the user input is greater than 1
    if len(user_input) > 1:
        print("Please enter only one letter!")
        # Go back and start again from line 4
        continue
    
    # Conditional statement checking if the user_input is in the five_letter_word
    if(user_input in five_letter_word):
        print("Great, Continue!\n")
        correct += 1
        # I am removing the user_input from the list so the user cannot use the same letter over and over again
        five_letter_word.remove(user_input)
        continue
    
    # Decrement the attempts since the user didn't guess correctly. When the if statement above is true, this will not execute because of the 'continue'!
    attempts -= 1
    print("Try Again! Attempts: {}\n".format(attempts))
    
    if attempts == 0:
        print("Sorry, do you want to try again?")