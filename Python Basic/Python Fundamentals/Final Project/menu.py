def get_valid_grade(subject_name):
    while True:
        try:
            grade = int(input(f"Please enter {subject_name} grade: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Invalid range! Must be between 0 and 100.")
        except ValueError:
            print("Please only use numbers, do not use letters")

def is_valid_name():
    while True:
        name = input("Please enter student name: ").strip()
        if len(name) == 0:
            print("Name cannot be empty!")
            continue
        
        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Invalid name! Please use only letters (no numbers or symbols).")         
            
def is_valid_section():
    while True:
        section = input("Please enter student section: ").strip()
        
        if len(section) == 0 or len(section) > 3:
            print("Use only 2 digits and one letter. Correct format -> Exp: 11B | Section cant be empty!!!")
            continue
        
        if section[0].isdigit() and section[1].isdigit():
            if not section[2].isdigit():
                return section.upper()
        else:
            print("Wrong format, please try again -> Exp: 11B")

import actions
import data

def get_valid_grade(subject_name):
    while True:
        try:
            grade = int(input(f"Please enter {subject_name} grade: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Invalid range! Must be between 0 and 100.")
        except ValueError:
            print("Please only use numbers, do not use letters")

def is_valid_name():
    while True:
        name = input("Please enter student name: ").strip()
        if len(name) == 0:
            print("Name cannot be empty!")
            continue
        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Invalid name! Please use only letters (no numbers or symbols).")         

def is_valid_section():
    while True:
        section = input("Please enter student section: ").strip()
        if len(section) == 0 or len(section) > 3:
            print("Use only 2 digits and one letter. Correct format -> Exp: 11B | Section cant be empty!!!")
            continue
        if section[0].isdigit() and section[1].isdigit():
            if not section[2].isdigit():
                return section.upper()
        else:
            print("Wrong format, please try again -> Exp: 11B")

def run_menu(students_list):
    menu_option = 9
    while True:
        print("Student Tracking System App!")
        print("Menu Options")
        print("1. Add students")
        print("2. All students")
        print("3. Top 3 students")
        print("4. Average grades")
        print("5. Export students data to CSV")
        print("6. Import data from CVS")
        print("7. Remove students")
        print("8. Failed students")
        print("9. Exit")

        try:
            option_selected = int(input("Please enter an option (1-9) \n"))
            if option_selected == menu_option:
                print("Closing app, see you later!")
                break

            match option_selected:
                case 1:
                    try:
                        numer_of_students = int(input("How many students would you like to add?\n"))
                        for _ in range(numer_of_students):
                            name = is_valid_name()
                            section = is_valid_section()
                            spanish = get_valid_grade("Spanish")
                            english = get_valid_grade("English")
                            social = get_valid_grade("Social Studies")
                            science = get_valid_grade("Science")
                            actions.add_student(name, section, spanish, english, social, science)
                    except ValueError:
                        print("\nPlease only use numbers\n")
                case 2:
                    if not students_list: print("No students found!")
                    else: actions.view_students_list(students_list)
                case 3:
                    actions.print_top_3_students(actions.get_grades_average(students_list))
                case 4:
                    actions.get_general_average(actions.get_grades_average(students_list))
                case 5:
                    if not students_list: print("No students to export!")
                    else: 
                        data.export_students_to_csv('students.csv', students_list, data.students_headers)
                        print("Data exported!")
                case 6:
                    file_to_read = input("Enter CSV name: ")
                    try: 
                        data.import_students_data(file_to_read)
                        print("Imported successfully!")
                    except FileNotFoundError: print("File not found!")
                case 7:
                    actions.remove_student(students_list)
                case 8:
                    actions.get_failing_students(students_list)
                case _:
                    print("Invalid option!")
        except ValueError:
            print("\nPlease only use numbers\n")