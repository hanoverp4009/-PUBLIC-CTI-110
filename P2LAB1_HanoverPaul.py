#Paul Hanover
#Date: 19 September 2026
#Assignment Name: P2LAB1 
#A brief description of the project: Build a program that will calculate the diameter, circumference and area of a circle.

#Import math module to use the constant, math.pi
import math

# Get radius from user
radius = float(input("What is the radius of the curcle? "))
print()

#calculate diameter
diameter = 2 * radius

#Display the diameter with 1 decimal point
print(f"The diameter of the circle is: {diameter:.1f}\n")

#calculate the circumference
circumference = 2 * math.pi * radius 

#display the circumference with 2 decimal points
print(f"The circumference of the circle is: {circumference:.2f}\n")

#calculate the area
area = math.pi * radius ** 2

#display the area with 23 decimal points
print(f"The area of the circle is: {area:.3f}")
