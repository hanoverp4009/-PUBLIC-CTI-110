# Paul Hanover
 # 19 SEP 2026
 # P2LAB2 
 # A brief description of the project: Write a program that creates a dictionary where the key and value pairs with data provided in instructions

cars = {'Camaro' :18.21, 'Prius' :52.36, 'Model S' :110, 'Silverado' :26}

#Get keys form dictionery
cars_keys = cars.keys()

print (cars_keys)

print (*cars_keys, sep = ", ")

#Get a car from the user
car_name = input("Enter a car: ")

#Get MPG for the given car
car_MPG = cars [car_name]

print (f"The {car_name} gets {car_MPG} miles per gallon.")

#get miles from the user
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))

#calculate
gallons_needed = miles_driven/car_MPG

#$Display results
print (f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles.")