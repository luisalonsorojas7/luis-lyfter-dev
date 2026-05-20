import actions
import data

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
        print("6. Import data from CSV")
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
                        number_of_students = int(input("How many students would you like to add?\n"))
                        for _ in range(number_of_students):
                            name = actions.is_valid_name()
                            section = actions.is_valid_section()
                            spanish = actions.get_valid_grade("Spanish")
                            english = actions.get_valid_grade("English")
                            social = actions.get_valid_grade("Social Studies")
                            science = actions.get_valid_grade("Science")
                            actions.add_student(students_list,name, section, spanish, english, social, science)
                    except ValueError:
                        print("\nPlease only use numbers\n")
                case 2:
                    if not students_list: print("No students found!")
                    else: actions.view_students_list(students_list)
                case 3:
                    if not students_list: print("No students found!")
                    else: actions.print_top_3_students(actions.get_grades_average(students_list))
                case 4:
                    if not students_list: print("No students found!")
                    else: actions.get_general_average(actions.get_grades_average(students_list))
                case 5:
                    if not students_list: print("No students to export!")
                    else: 
                        data.export_students_to_csv('students.csv', students_list, data.students_headers)
                        print("Data exported!")
                case 6:
                    file_to_read = input("Enter CSV name: ")
                    try: 
                        data.import_students_data(file_to_read, students_list)
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