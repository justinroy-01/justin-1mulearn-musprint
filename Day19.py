#Write a code to find grade of students from given dictionary

students = {
    "Alice": {"Math": 90, "Science": 88, "English": 92},
    "Bob": {"Math": 70, "Science": 65, "English": 72},
    "Charlie": {"Math": 40, "Science": 45, "English": 38},
    "David": {"Math": 85, "Science": 78, "English": 80}
}

failed_students = []

for name, marks in students.items():
    total = sum(marks.values())
    average = total / len(marks)

    if average >= 85:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"
        failed_students.append(name)

    print("Student:", name)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)
    print("-" * 30)

print("Failed Students:", failed_students)
