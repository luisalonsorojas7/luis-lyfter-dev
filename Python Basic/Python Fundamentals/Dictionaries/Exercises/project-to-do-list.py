"""Gestor de Tareas (To-Do List) con Prioridades 📝
Qué hace: Una lista de diccionarios. Cada tarea tiene un nombre, una prioridad (Alta, Media, Baja) y un estado (Pendiente, Completada).
Lo que demuestra: Manipulación de listas y filtrado.
Funcionalidad: El programa debe ser capaz de imprimir solo las tareas de "Prioridad Alta" que aún están "Pendientes".
"""

my_tasks = []
menu_option = 0
counter_task = 0

while True:
    print("Menu Options.")
    print("1. Add task.")
    print("2. Remove task.")
    print("3. List your tasks.")
    print("4. Close")
    menu_option = int(input("Please enter an option (1-4)\n"))

    if menu_option == 4:
        print("Closing app, see you later!")
        break

    match menu_option:
        case 1:
            name = input("Please enter the task: \n")
            priority = input("Please enter the task priority (High - Medium - Low)\n")
            status = input("Please enter status: (Pending - Completed - In Progress)\n")
            counter_task += 1

            my_task = {
                "TaskID": counter_task,
                "Name": name,
                "Priority": priority,
                "Status": status,
            }

            my_tasks.append(my_task)
            print("Task added successfully!\n")
            print(my_tasks)

        case 2:
            for task in my_tasks:
                ids = task["TaskID"]
                option_to_remove = int(input("Please the task number you want to remove from the Todo list:\n"))
                if ids == option_to_remove:
                    my_tasks.remove(task)
                    print("Task removed successfully!")
                    break
            print(my_tasks)
        case 3:
            if not my_tasks:
                print("Your list is empty \n")
            for task in my_tasks:
                if task["Priority"] == "High" and task["Status"] == "Pending":
                    print(task["Name"])
        case _:
            print("Invalid option")

print(my_tasks)
