# Program to find the highest, lowest, and average marks in a class
marks_list = [78, 92, 85, 64, 99, 53, 88]

# Initialise variables with the first element of the list
highest = marks_list[0]
lowest = marks_list[0]
total_sum = 0

# Loop through the list to calculate values
for mark in marks_list:
    total_sum += mark
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark

average = total_sum / len(marks_list)

print(f"Marks List: {marks_list}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Average Marks of the Class: {average:.2f}")
