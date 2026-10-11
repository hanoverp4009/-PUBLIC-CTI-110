# Paul Hanover
 # Date: 11 October 2026
 # P2HW2
 # You are provided with a partial Python program that contains bugs. Your job is to fix and complete the program so it runs correctly.

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
#get the grade for module 1
mod_1 = float(input('Enter grade for Module 1: '))

#get the grade for moduele 2
mod_2 = float(input('Enter grade for Module 2: '))

#get the grade for module 3
mod_3 = float(input('Enter grade for Module 3: '))

#get the grade for module 4
mod_4 = float(input('Enter grade for Module 4: '))

#get the grade for module 5
mod_5 = float(input('Enter grade for Module 5: '))

#get the grade for module 6
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')

# display grade summary
print(f'Lowest grade: {low}')
print(f'Highest grade: {high}')
print(f'Sum of grades: {total}')
print(f'Average grade: {avg:.2f}')






