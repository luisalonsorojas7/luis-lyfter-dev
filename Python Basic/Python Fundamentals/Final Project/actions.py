def add_student(students_list, name, section, spanish_grade, english_grade, social_studies_grade, science_grade):
    student = {
        "name": name,
        "section": section,
        "spanish": spanish_grade,
        "english": english_grade,
        "social": social_studies_grade,
        "science": science_grade,
    }
    
    exists = False
    for person in students_list:
        if name == person['name'] and section == person['section']:
            print("\nThere is already one student with that information, unable to add duplicate information.")
            exists = True
            break
    
    if not exists:
        students_list.append(student)
        print("\nStudent added successfully!")

def view_students_list(students_list):
    if not students_list:
        print("\nThe list is empty.")
        return
    
    for student in students_list:
        print(
            f"Student: {student['name']} | Section: {student['section']} | "
            f"Spanish: {student['spanish']} | English: {student['english']} | "
            f"Social: {student['social']} | Science: {student['science']}"
        )

def get_grades_average(students_list):
    grades_list = []
    for student in students_list:
        name = student['name']
        avg = (student['spanish'] + student['english'] + student['social'] + student['science']) / 4
        grades_list.append((name, avg))
    
    grades_list.sort(key=lambda x: x[1], reverse=True)
    return grades_list

def print_top_3_students(grades_list):
    top_3 = grades_list[:3]
    print("\n--- TOP 3 STUDENTS ---")
    for index, student in enumerate(top_3, start=1):
        print(f"{index}. {student[0]} - Grade average: {student[1]:.2f}")

def get_general_average(grades_list):
    if not grades_list:
        return
    
    total = sum(item[1] for item in grades_list)
    general_avg = total / len(grades_list)
    print(f"\nClass average is: {general_avg:.2f}")

def remove_student(students):
    name = input("Please enter student name:\n")
    section = input("Please enter student section:\n")
    student_found = False
    
    for student in students:
        if name == student['name'] and section == student['section']:
            student_found = True
            option = input(f"Student {name} found! Are you sure you want to remove it? (Y/N): ")
            if option.lower() == 'y':
                students.remove(student)
                print(f"Student {name} was successfully removed!")
                break
    
    if not student_found:
        print("No student found!")

def get_failing_students(students):
    any_failing = False
    for student in students:
        this_student_fails = []
        if student['spanish'] < 60: this_student_fails.append(f"Spanish ({student['spanish']})")
        if student['english'] < 60: this_student_fails.append(f"English ({student['english']})")
        if student['social'] < 60: this_student_fails.append(f"Social Studies ({student['social']})")
        if student['science'] < 60: this_student_fails.append(f"Science ({student['science']})")
        
        if this_student_fails:
            any_failing = True
            subjects = ", ".join(this_student_fails)
            print(f"Student: {student['name']} [{student['section']}] - Failed: {subjects}")
            
    if not any_failing:
        print("Great news! No students are failing so far.")
        

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
            print("Invalid name! Please use only letters (no numbers or symbols)")         

def is_valid_section():
    while True:
        section = input("Please enter student section: ").strip()
        if len(section) == 0 or len(section) > 3:
            print("Wrong format, please try again -> Exp: 11B or 9B | Section cant be empty!!!")
            continue
        
        if len(section) == 2:
            if section[0].isdigit() and section[1].isalpha():
                return section.upper()
            
        if len(section) == 3:
            if section[0].isdigit() and section[1].isdigit() and section[2].isalpha():
                return section.upper()
        else:
            print("Wrong format, please try again -> Exp: 11B or 9B")