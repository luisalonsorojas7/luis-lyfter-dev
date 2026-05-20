import csv

students_headers = (
    'name',
    'section',
    'spanish',
    'english',
    'social',
    'science'
)

def export_students_to_csv(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter="\t")
        writer.writeheader()
        writer.writerows(data)

def import_students_data(file_path, students_list):
    students_list.clear()
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter="\t")
        for row in reader:
            student = {
                "name": row['name'],
                "section": row['section'],
                "spanish": int(row['spanish']),
                "english": int(row['english']),
                "social": int(row['social']),
                "science": int(row['science']),
            }
            students_list.append(student)