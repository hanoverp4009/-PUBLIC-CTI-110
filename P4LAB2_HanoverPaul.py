# Paul Hanover
 # Date: 26 October 2026
 # P4LAB2
 # write a program that asks the user to enter an integer. If the integer is zero or higher, the program should print the multiplication table for that number. If the user enters a negative number, the program should print a message that it cannot accept negative values.

'''
Get an integer from the user
Determine if the integer is positive or negative
if number ispositive, print the multiplication table for that number
if number is negative, print a message that it cannot accept negative values
Ask user to run aggain?
if yes, run program again
if no, end the program
'''

run_again = 'yes'

while run_again != 'no':
    user_numb = int(input("Please enter an integer: "))

    if user_numb >= 0:
        #display the multiplication table for the number and range (1-12)
        print(f"Multiplication table for {user_numb}:")
        for item in range(1, 13):
            print(f"{user_numb} x {item} = {user_numb * item}")
    else:
        print("Cannot accept negative values.")
    
    run_again = input("Would you like to run the program again? ")

#Loop has broken. User entered 'no'
print("program has ended. Thank you for playing!")

user_numb = int(input("Please enter an integer: "))

if user_numb >= 0:
    #display the multiplication table for the number and range (1-12)
    print(f"Multiplication table for {user_numb}:")
    for item in range(1, 13):
        print(f"{user_numb} x {item} = {user_numb * item}")
else:
    print("Cannot accept negative values.")