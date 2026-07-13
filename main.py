def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "Fail"


print("=" * 40)
print("      STUDENT RESULT CALCULATOR")
print("=" * 40)

name = input("Enter Student Name: ")

subjects = ["Maths", "Science", "English", "Python", "AI"]

marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter {subject} Marks (0-100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")

total = sum(marks)
average = total / len(marks)
grade = calculate_grade(average)

print("\n" + "=" * 40)
print("RESULT")
print("=" * 40)
print(f"Student Name : {name}")
print(f"Total Marks  : {total}/500")
print(f"Average      : {average:.2f}%")
print(f"Grade        : {grade}")
print("=" * 40)