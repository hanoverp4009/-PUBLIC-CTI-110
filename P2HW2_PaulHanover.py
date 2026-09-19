#Paul Hanover
#Date: 19 September 2026
#Assignment Name: P2HW2
#Build a program that prompts for test grades for modules, store grades in a list and the calulate results and format the output exactly as shown in the instructions.

#get the grade for module 1
module1 = float(input("Enter the grade for module 1: "))

#get grade for module 2
module2 = float(input("Enter the grade for module 2: "))

#get grade for module 3
module3 = float(input("Enter the grade for module 3: "))

#get grade for module 4
module4 = float(input("Enter the grade for module 4: "))

#get grade for module 5
module5 = float(input("Enter the grade for module 5: "))

#get grade for module 6
module6 = float(input("Enter the grade for module 6: "))

#store grades for modules in a list
grades_modules = [module1, module2, module3, module4, module5, module6]

#Using the list of grades, calculate and display the Lowest grade, the highest grade, the average grade, and the total of all grades. Format the output exactly as shown in the instructions.
lowest_grade = min(grades_modules)
highest_grade = max(grades_modules)
total_grade = sum(grades_modules)
average_grade = total_grade / len(grades_modules)

print("------------------Results------------------")
print(f'{"Lowest grade":<15}: {lowest_grade :>.2f}')
print(f'{"Highest grade":<15}: {highest_grade :>.2f}')
print(f'{"Total grade":<15}: {total_grade :>.2f}')
print(f'{"Average grade":<15}: {average_grade :>.2f}')
print("-------------------------------------------")
