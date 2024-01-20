def Calculator(marks):
    return sum(marks) / len(marks)

def Seprater(average_marks):
    if average_marks >= 80:
        return "A"
    elif average_marks >= 70:
        return "B"
    elif average_marks >= 60:
        return "C"
    else:
        return "D"

def Main():
    print("\n-->   Write a Number of Students   <---\n")
    num_students = int(input("Enter the Number of Students: "))

    subjects = ["Math", "Science", "English", "I.P", "Social Science"]

    students_data = []
    print("\n-->   Now First Write a Name Of Student And Then Write a Marks Of Student Out Of /100   <---\n")

    for n in range(num_students):
        student_name = input(f"\nEnter the name of student {n + 1}: ")

        marks = []
        for subject in subjects:
            marks.append(float(input(f"Enter marks for {subject}: ")))

        average_marks = Calculator(marks)
        division = Seprater(average_marks)

        student_info = {
            "Name": student_name,
            "Marks": dict(zip(subjects, marks)),        
            "Average Marks": average_marks,
            "Division": division
        }

        students_data.append(student_info)
        print(students_data)


    print("\nStudent-wise Result:")
    for student in students_data:
        print(f"\nName: {student['Name']}")
        print("Marks:")
        for subject, mark in student['Marks'].items():
            print(f"  {subject}: {mark}")
        print(f"Average Marks: {student['Average Marks']}")
        print(f"Division: {student['Division']}")


Main()
