# Paul Hanover
 # Date: 26 October 2026
 # P4LAB2
 # Creat a neew Python code file


'''
Ask user to input a number of scores they would like to enter
create a loop to collect the number of scoores the user wants to enter
every time a score is entered, the following should be done:
Evaluate if the score is valid (between 0 and 100)
if it is not, notrify the user and ask for a VALID score to be entered
if the score is valid, add it to a list of scores. Make sure the score list is given an informative name.
After collecting all the scores. The program is to display the following information:
Lowest score entered
Score List after dropping lowest score
The average of the scores in modified list
Determine the letter grade for the average score and display it to the user'''


#Ask user to input a number of scores they would like to enter
num_scores = int(input("How many scores would you like to enter? "))
#Create a loop to collect the number of scores the user wants to enter
scores = []  # List to store valid scores
for _ in range(num_scores):
    while True:
        try:
            score = float(input("Enter a score (0-100): "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Display the required information
if scores:
    lowest_score = min(scores)
    modified_scores = [score for score in scores if score != lowest_score]
    average = sum(modified_scores) / len(modified_scores) if modified_scores else 0

    # Determine letter grade for the average score
    if average >= 90:
        letter_grade = 'A'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 70:
        letter_grade = 'C'
    elif average >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    # Display results
    print(f"Lowest score entered: {lowest_score}")
    print(f"Score List after dropping lowest score: {modified_scores}")
    print(f"The average of the scores in the modified list: {average:.2f}")
    print(f"Letter grade for the average score: {letter_grade}")
else:
    print("No valid scores entered.")