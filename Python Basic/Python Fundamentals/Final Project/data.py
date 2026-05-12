import csv
from actions import students_list

students_headers = (
	'name',
	'section',
	'spanish',
	'english',
    'social',
    'science'
)

def export_students_to_csv(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers, delimiter="\t")
        writer.writeheader()
        writer.writerows(data)

def import_students_data(file):
    with open(file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter="\t")
        for row in reader:
            name = row['name']
            section = row['section']
            spanish = int(row['spanish'])
            english = int(row['english'])
            social = int(row['social'])
            science = int(row['science'])
                            
            student = {
                "name": name,
                "section": section,
                "spanish": spanish,
                "english": english,
                "social": social,
                "science": science,
            }
            
            students_list.append(student)