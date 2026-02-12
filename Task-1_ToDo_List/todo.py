import json
import os
FILE_NAME= "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    return []
def save_tasks(tasks):
    with open(FILE_NAME,"w") as file:
        json.dump(tasks,file,indent=4)
def add_tasks(tasks):
    title=input("Enter task Title: ")
    priority =input("Enter the priority of the Task(High/Medium/Low):").capitalize()
    due_date =input("Due Date (DD-MM-YYYY): ")
    task= {
        "title":title,
        "priority":priority,
        "due_date":due_date,
        "completed":False
    }
    tasks.append(task)
    save_tasks(tasks)
def view_tasks(tasks):
    if not tasks:
        print("No tasks are available")
        return
    for index, task in enumerate(tasks, start=1):
        status="Done" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} | {task['priority']} | {task['due_date']} | {status}")

def update_task(tasks):
    view_tasks(tasks)
    choice=int(input("Enter task number to mark as completed: ")) -1
    if 0<=choice<len(tasks):
        tasks[choice]["Completed"]= True
        save_tasks(tasks)
        print("Task Updated Successfully.")
    else:
        print("Invalid Task Number.")
def delete_task(tasks):
    view_tasks(tasks)
    choice = int(input("Enter task number to delete: ")) - 1

    if 0 <= choice < len(tasks):
        removed = tasks.pop(choice)
        save_tasks(tasks)
        print(f"Task '{removed['title']}' deleted.")
    else:
        print("Invalid task number.")
def delete_all_tasks(tasks):
    confirm = input("Are you sure you want to delete ALL tasks? (yes/no): ")

    if confirm.lower() == "yes":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks deleted successfully.")
    else:
        print("Operation cancelled.")

def main():
    tasks =load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Delete all tasks")
        print("5. Exit the to-do list")
        option=input("Choose an option: ")
        if option=="1":
            add_tasks(tasks)
        elif option=="2":
            view_tasks(tasks)
        elif option=="3":
            update_task(tasks)
        elif option=="4":
            delete_task(tasks)
        elif option=="5":
            delete_all_tasks(tasks)
        elif option=="6":
            print("Exiting the to do list application, Thank you!")
            break        
        else:
            print("Invalid Choice, Try again")

if __name__ == "__main__":
    main()
        


