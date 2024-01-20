def Average(Marks, MaxMarks):
    total_marks = sum(Marks)
    total_max_marks = MaxMarks

    average = (total_marks / total_max_marks) * 100 
    return average


def Questions():
    No_of_SUB = int(input("Enter The Number Of Subject : ",))
    print()
    Max_Marks_obtain = int(input("Enter The Maximum Marks : "))
    print()
    Max_marks = (Max_Marks_obtain*No_of_SUB)
    print()

    All_Sub_marks = []

    for i in range(No_of_SUB):
        subject_marks = int(input(f"Enter Marks of Subject {i+1} : "))
        if subject_marks > Max_Marks_obtain:
            print('''                                  There is Some Error
              
                            Fill The Information one More Time ''')
            Questions()
            exit()
        
        
        else:
            All_Sub_marks.append(subject_marks)


        print()


    Average_of_all_sub=Average(Marks=All_Sub_marks, MaxMarks=Max_marks)

    print(f"The Average of {No_of_SUB} is  : {Average_of_all_sub:.2f}%")

    
Questions()
