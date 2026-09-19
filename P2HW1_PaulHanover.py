# Paul Hanover
 # Date: 19 September 2026
 # P2HW1 
 # Ceate a program that does some basic math on numbers that are entered for a budget on a potential trip. the output will be nicely formatted.

# Ask the user for a budget to start for the trip.

budget = float(input("Enter your budget for the trip: $"))

# Ask the user to enter the travel destination.

destination = input("Enter your travel destination: ")

# Ask the user to enter the amount of money they will spend on gas for the trip.

gas = float(input("Enter the amount of money you will spend on gas for the trip: $"))

# Ask the user the amount of money they will spend on accomadations for the trip.

accommodation = float(input("Enter the amount of money you will spend on accommodation for the trip: $"))

# Ask the user for the ammount they plan on spending on food for the trip.

food = float(input("Enter the amount of money you will spend on food for the trip: $"))

# Add espenses for the trip.
total_expenses = gas + accommodation + food

# Subtract the total expenses from the budget to find out how much money is left over for the trip.
remaining_budget = budget - total_expenses

# display results to the user.
print("-----------------Travel Expenses-------------------------")
print(f'\n{"Location":<15}: {destination:>16}')
print(f"{"Initial Budget":<15}: ${budget:>15.2f}")
print(f"{"Total Expenses":<15}: ${total_expenses:>15.2f}")
print(f"{"Remaining Budget":<15}: ${remaining_budget:>14.2f}\n")
print("---------------------------------------------------------")