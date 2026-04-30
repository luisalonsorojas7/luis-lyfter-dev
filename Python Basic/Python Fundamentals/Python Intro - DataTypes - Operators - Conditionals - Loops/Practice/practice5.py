'''5. Dada n cantidad de notas de un estudiante, calcular:
Cuantas notas tiene aprobadas (mayor a 70).
Cuantas notas tiene desaprobadas (menor a 70).
El promedio de todas.
El promedio de las aprobadas.
El promedio de las desaprobadas.'''
total_grades = 0
total_average = 0
pass_average = 0
failed_average = 0
passed_count = 0
failed_count = 0
grade_count = 0
grade = 0
sum_grades = 0
sum_pass = 0
sum_failed = 0

total_grades = int(input("How many students grades would you like to evaluate?\n"))

while grade_count < total_grades:
    grade = int(input("Please enter the student grade: \n"))
    grade_count += 1
    sum_grades += grade

    if grade < 70:
        failed_count +=1
        sum_failed += grade
    else:
        passed_count += 1 
        sum_pass += grade

total_average = sum_grades / total_grades

if passed_count > 0:
    pass_average = sum_pass / passed_count
else:
    pass_average = 0
    
if failed_count > 0:
    failed_average = sum_failed / failed_count
else:
    failed_average = 0
    
print(f"Grades average: {total_average}")
print(f"Passed average: {pass_average}")
print(f"Failed average: {failed_average}")
print(f"Passed students: {passed_count}")
print(f"Failed students: {failed_count}")
