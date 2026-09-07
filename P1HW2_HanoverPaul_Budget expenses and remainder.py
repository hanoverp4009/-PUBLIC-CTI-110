# Paul Hanover
 # Date: 7 September 2026
 # P1HW2 
 # Ceate a program that does some basic math on numbers that are entered for a budget on a potential trip.

# Ask the user for a budget to start for the trip.

budget = float(input("Enter your budget for the trip: "))

# Ask the user to enter the travel destination.

destination = input("Enter your travel destination: ")

# Ask the user to enter the amount of money they will spend on gas for the trip.

gas = float(input("Enter the amount of money you will spend on gas for the trip: "))

# Ask the user the amount of money they will spend on accomadations for the trip.

accommodation = float(input("Enter the amount of money you will spend on accommodation for the trip: "))

# Ask the user for the ammount they plan on spending on food for the trip.

food = float(input("Enter the amount of money you will spend on food for the trip: "))

# Add espenses for the trip.
total_expenses = gas + accommodation + food
# Subtract the totall expenses from the budget to find out how much money is left over for the trip.
remaining_budget = budget - total_expenses
# display results to the user.
print(f"\nYour total expenses for the trip to {destination} are: ${total_expenses:.2f}")
print(f"Your remaining budget for the trip is: ${remaining_budget:.2f}")