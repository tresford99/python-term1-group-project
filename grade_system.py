def calculate_grade(marks):
    # Input validation: ensure we have exactly 5 marks
    if len(marks) != 5:
        print("Error: Please enter exactly 5 marks.")
        return

    # Validate marks are numbers between 0 and 100
    for m in marks:
        if not (0 <= m <= 100):
            print("Error: Marks must be between 0 and 100.")
            return

    # Calculate average
    average = sum(marks) / len(marks)

    # Determine grade
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Print results
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


# Main program
marks = []
for i in range(5):
    while True:
        try:
            mark = int(input(f"Enter mark {i+1}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

calculate_grade(marks)
