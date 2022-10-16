class Student:
    def __init__(self, id, name, age, school_name, completed_classes, ongoing_classes):
        self.id = id
        self.name = name
        self.age = age
        self.school_name = school_name
        self.completed_classes = completed_classes
        self.ongoing_classes = ongoing_classes


s1 = Student('N01472214', 'Julian Wu', 23, "Waterloo University", {'CPAN211': 88, 'CPAN212': 90},
             {'CPAN231': 88, 'CPAN213': 89})
s2 = Student('N01542214', 'Eric Chou', 22, "Humber College", {'CPAN211': 97, 'CPAN212': 86},
             {'CPAN231': 87, 'CPAN213': 92})
s3 = Student('N02453587', 'Kay Lee', 25, "Western University", {'CPAN231': 87, 'CPAN212': 71},
             {'CPAN212': 90, 'CPAN213': 91})

student_dic = {
    s1.id: {
        'Name': s1.name,
        'ID': s1.id,
        'Age': s1.age,
        "School's Name": s1.school_name,
        "Completed Courses": {
            list(s1.completed_classes)[0]: s1.completed_classes.get(list(s1.completed_classes)[0]),
            list(s1.completed_classes)[1]: s1.completed_classes.get(list(s1.completed_classes)[1])
        },
        "Ongoing Courses": {
            list(s1.ongoing_classes)[0]: s1.ongoing_classes.get(list(s1.ongoing_classes)[0]),
            list(s1.ongoing_classes)[1]: s1.ongoing_classes.get(list(s1.ongoing_classes)[1])
        },
    },
    s2.id: {
        'Name': s2.name,
        'ID': s2.id,
        'Age': s2.age,
        "School's Name": s2.school_name,
        "Completed Courses": {
            list(s2.completed_classes)[0]: s2.completed_classes.get(list(s2.completed_classes)[0]),
            list(s2.completed_classes)[1]: s2.completed_classes.get(list(s2.completed_classes)[1])
        },
        "Ongoing Courses": {
            list(s2.ongoing_classes)[0]: s2.ongoing_classes.get(list(s2.ongoing_classes)[0]),
            list(s2.ongoing_classes)[1]: s2.ongoing_classes.get(list(s2.ongoing_classes)[1])
        },
    },
    s3.id: {
        'Name': s3.name,
        'ID': s3.id,
        'Age': s3.age,
        "School's Name": s3.school_name,
        "Completed Courses": {
            list(s3.completed_classes)[0]: s3.completed_classes.get(list(s3.completed_classes)[0]),
            list(s3.completed_classes)[1]: s3.completed_classes.get(list(s3.completed_classes)[1])
        },
        "Ongoing Courses": {
            list(s3.ongoing_classes)[0]: s3.ongoing_classes.get(list(s3.ongoing_classes)[0]),
            list(s3.ongoing_classes)[1]: s3.ongoing_classes.get(list(s3.ongoing_classes)[1])
        },
    }
}


def all_info_display():
    print("----------------------------------------------")
    for s_index, s_info in student_dic.items():
        print(f"\nStudent {s_index} ")
        for keyy, value in s_info.items():
            if keyy == "Completed Courses":
                for k, v in value.items():
                    print(f'{k}' + ":", value.get(k), "(Completed)")
            elif keyy == "Ongoing Courses":
                for k, v in value.items():
                    print(f'{k}' + ":", value.get(k), "(Ongoing)")
            else:
                print(f'{keyy}' + ":", s_info.get(keyy))


def unique_info(id):
    print("----------------------------------------------")
    for s_index, s_info in student_dic.items():
        if s_index == id:
            print(f"\nStudent {id} ")
            for keyy, value in s_info.items():
                if keyy == "Completed Courses":
                    for k, v in value.items():
                        print(f'{k}' + ":", value.get(k), "(Completed)")
                elif keyy == "Ongoing Courses":
                    for k, v in value.items():
                        print(f'{k}' + ":", value.get(k), "(Ongoing)")
                else:
                    print(f'{keyy}' + ":", s_info.get(keyy))


def unique_on_grades(id):
    print("----------------------------------------------")
    for s_index, s_info in student_dic.items():
        if s_index == id:
            print(f"\nStudent {s_index}'s Grades for Ongoing Courses:")
            for keyy, value in s_info.items():
                if keyy == "Ongoing Courses":
                    for k, v in value.items():
                        print(f'{k}' + ":", value.get(k))


def unique_com_grades(id):
    for s_index, s_info in student_dic.items():
        if s_index == id:
            print(f"\nStudent {s_index}'s Grades for Completed Courses:")
            print("----------------------------------------------")
            for keyy, value in s_info.items():
                if keyy == "Completed Courses":
                    for k, v in value.items():
                        print(f'{k}' + ":", value.get(k))


def ave_for_com_courses(id):
    ave = []
    for s_index, s_info in student_dic.items():
        if s_index == id:
            for keyy, value in s_info.items():
                if keyy == "Completed Courses":
                    for k, v in value.items():
                        ave.append(value.get(k))
                    print(f"\nStudent {id}'s Average Grades for courses completed is: {sum(ave) / len(ave)}")


def grade_for_a_course(id, courseName):
    print("----------------------------------------------")
    for s_index, s_info in student_dic.items():
        if s_index == id:
            print(f"\nStudent {id}'s Grade for {courseName}:")
            for keyy, value in s_info.items():
                if keyy == "Completed Courses" or keyy == "Ongoing Course":
                    for k, v in value.items():
                        if courseName == k:
                            print(value.get(k))


def continue_or_not():
    decision = input('Do you want to perform another query? (y/n): ')
    return decision.lower()


def choose_what_to_view():
    number = input(f'Choose a task to perform from below:\n'
                   f"1, view all students' information\n"
                   f'2, view information on a specific student\n'
                   f'3, view all grades of ongoing courses for a specific student\n'
                   f'4, view all grades of completed courses for a specific student\n'
                   f'5, view the average grade of courses completed for a specific student\n'
                   f'6, view a specific grade of specific student\n'
                   f'----------------------------------------------\n'
                   f'Enter a number: ')
    return number


i = 1
while i:
    match (choose_what_to_view()):
        case ('1'):
            all_info_display()
            if continue_or_not() == 'y':
                continue
            else:
                print("Goodbye~~~")
                break
        case ('2'):
            id = input("Please enter student ID: ")
            unique_info(id)
            if continue_or_not() == 'y':
                continue
            else:
                print("Goodbye~~~")
                break
        case ('3'):
            id = input("Please enter student ID: ")
            unique_on_grades(id)
            if continue_or_not() == 'y':
                continue
            else:
                print("Goodbye~~~")
                break
        case ('4'):
            id = input("Please enter student ID: ")
            unique_com_grades(id)
            if continue_or_not() == 'y':
                continue
            else:
                break
        case ('5'):
            id = input("Please enter student ID: ")
            ave_for_com_courses(id)
            if continue_or_not() == 'y':
                continue
            else:
                print("Goodbye~~~")
                break
        case ('6'):
            id = input("Please enter student ID: ")
            cn = input("Please enter course name: ")
            grade_for_a_course(id, cn)
            if continue_or_not() == 'y':
                continue
            else:
                print("Goodbye~~~")
                break
        case _:
            print("Input invalid...")
            print("Goodbye~~~")
            break

