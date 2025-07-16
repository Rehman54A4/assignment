# task1:
# Step 1: Creating a dictionary with student names and their marks
student_marks = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'Diana': 88,
    'Ethan': 90
}

# Step 2: Asking the user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieving and displaying marks, or showing a message if not found
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the records.")

#task2:
# Step 1: Creating a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Extracting the first five elements
first_five = numbers[:5]

# Step 3: Reversing the extracted elements
reversed_five = first_five[::-1]

# Step 4: Printing  both lists
print("First five elements:", first_five)
print("Reversed list:", reversed_five)    