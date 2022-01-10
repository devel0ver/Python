for i in range(0, 151):
    print(i)            # Prints all integers from 0 to 150.

for v  in range(5, 1001, 5):
    print(v)          # Prints all the multiples of 5 from 5 to 1,000 in a for loop

"""v = 5
while v <= 1000:
    print(v)            
    v += 5"""                # Prints all the multiples of 5 from 5 to 1,000 in a while loop

for count in range(1, 101):
    print(count)        # Print integers 1 to 100
    if count % 5 == 0:  
        print("Coding") # If count is divisible by 5, print "Coding"
    if count % 10 == 0:
        print("Coding Dojo") # If count is divisible by 10, print "Coding Dojo".


sum = 0
for odd in range(0,500001, 2):
    sum += odd         # Add odd integers from 0 to 500,000.
print(sum)             # prints the final sum.

for down in range(2018, 0, -4):
    print(down)      # Print positive numbers starting at 2018, counting down by fours.

lowNum = 2
highNum = 9
mult = 3        # Set three variables
for flex in range(lowNum+1, highNum+1, mult):       # Starting at lowNum and going through highNum
    print(flex)         # print only the integers that are a multiple of mult