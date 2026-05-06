students_list = []

def add_student(
    name, section, spanish_grade, english_grade, social_studies_grade, science_grade
):
    student = {
        "name": name,
        "section": section,
        "spanish": spanish_grade,
        "english": english_grade,
        "social": social_studies_grade,
        "science": science_grade,
    }
    students_list.append(student)
    
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

def view_students_list(students_list):
    for student in students_list:
        print(
            f"Student: {student['name']} | Section: {student['section']} | Spanish Grade: {student['spanish']} | English Grade: {student['english']} | Social Studies Grade: {student['social']} | Science Grade: {student['science']}"
        )


def main():
    menu_option = 7
    while True:
        print("Student Tracking System App!")
        print("Menu Options")
        print("1. Add students")
        print("2. All students")
        print("3. Top 3 students")
        print("4. Average grades")
        print("5. Export students data to CSV")
        print("6. Import data from CVS")
        print("7. Exit")

        try:
            option_selected = int(input("Please enter an option (1-7) \n"))

            if option_selected == menu_option:
                print("Closing app, see you later!")
                break

            match option_selected:
                case 1:
                    try:
                        while True:
                            numer_of_students = int(input("How many students would you like to add to the system?\n"))
                            break
                        for _ in range(numer_of_students):
                            name = input("Please enter student name:\n")
                            section = input("Please student section: \n")
                            spanish = get_valid_grade("Spanish")
                            english = get_valid_grade("English")
                            social = get_valid_grade("Social Studies")
                            science = get_valid_grade("Science")
                            add_student(
                                name, section, spanish, english, social, science
                            )
                            print("Student was successfully added!\n")
                    except ValueError:
                        print("\nPlease only use numbers, do not use letters\n")
                case 2:
                    if not students_list:
                        print("No students found in the sytem! Back to menu...\n")
                    else:
                        view_students_list(students_list)
                case 3:
                    print("Hola")
                case 4:
                    print("Hola")
                case 5:
                    print("Hola")
                case 6:
                    print("Hola")
                case _:
                    print("Invalid option!")
        except ValueError:
            print("\nPlease only use numbers, do not use letters\n")


if __name__ == "__main__":
    main()
