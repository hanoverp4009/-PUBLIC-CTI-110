# Paul Hanover
 # Date: 26 October 2026
 # P3LAB1
 # Use Turtle and loops to draw a square and a triangle.

#import the library
import turtle

# Create the turtle window and drawing object
window = turtle.Screen()
pen = turtle.Turtle()


# Set turtle options
pen.pensize(5)
pen.pencolor('olive')
pen.shape('arrow')

# Code to draw the shapes
for side in range(4):  # Loop to draw a square
    pen.forward(200)  # Draw one side of the square
    pen.left(90)      # Turn left 90 degrees 

#move the turtle to the top left corner of the square
pen.penup()  # Lift the pen to move without drawing
pen.forward(200)  # Move to the top left corner of the square
pen.left(90)  # Turn left to face downwards 
pen.forward(200)  # Move down to the bottom left corner of the square 
pen.right(90)  # Turn right to face right 
pen.pendown()  # Put the pen down to draw

#while loop that executes 3 times to draw a triangle
sides = 3

while sides > 0:
    pen.left(120)     # Turn left 120 degrees
    pen.forward(200)  # Draw one side of the triangle
    sides = sides - 1


# Wait for user to close the window
window.mainloop()
