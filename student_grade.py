# Get student name
student_name = input("Enter student name: ")

# Get marks for three subjects
marks = []

for i in range(1, 4):
    while True:
        try:
            mark = float(input(f"Enter marks for subject {i} (0-100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

# Calculate total and average
total = sum(marks)
average = total / 3

# Calculate grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

# Display student result
print("\n--- Student Result ---")
print("Name:", student_name)
print("Total:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
