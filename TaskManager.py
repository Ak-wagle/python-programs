'''
TaskManger.py v1.0

Assignment : Create the Task List: Start with an empty list called tasks.

Add Task:
Ask the user to enter a task (a string), and add it to the tasks list.
Each task should be unique (no duplicates).
If the task already exists, notify the user and do not add it.

Remove Task:
Allow the user to remove a task by specifying its name.
If the task is not found, display an appropriate message.

View All Tasks:
Display all tasks in the list, showing their index and name.
If the list is empty, inform the user.

Task Statistics:
Total Tasks - Display the total number of tasks.
Completed vs. Remaining:
Add a mechanism to mark tasks as "completed."
Display the number of completed and remaining tasks separately.

Search Task:
Allow the user to search for a task by entering a keyword.
If tasks containing the keyword are found, display them with their indexes; otherwise, show a message that no matching tasks were found.

Exit:
Provide an option to exit the program.

'''

tasks = []

def add_task():
    new_item = input("Enter the Task bro! : ")
    if not tasks:
        tasks.append({"Task" : new_item, "Completion_status" : "Pending"})
        print(f"{new_item} added successfully!") 
    else:
        for task in tasks:
            if task["Task"] != new_item:
                tasks.append({"Task" : new_item, "Completion_status" : "Pending"})
                print(f"{new_item} added successfully!")
                return
            else:
                print("What is this bro!!! Duplicates are not allowed\n")
                return

def rmv_task():
    rmv_item = input("Enter the Task, I'll remove it for you : ")
    if not tasks:
        print("The Task List is Empty\n")
    else:
        for task in tasks:
            if rmv_item not in task["Task"]:
                print("{rmv_item} is not in tasks!, there might be typo or you drunk bro\n")
            else:
                tasks.remove(task)
                print(f"{rmv_item} removed successfully from the Tasks list\n")

def view_task():
    if not tasks:
        print("The Tasks list is empty!\n")
    else:
        for i, task in enumerate(tasks):
            print(f"{i} : {task["Task"]} - {task["Completion_status"]}")

def task_stats():
    total_tasks = len(tasks)
    completed_ = []
    pending_ = []
    if not tasks:
        print("Task menu is Empty, fill it to view the statistics")
        return
    for task in tasks:
        if task["Completion_status"] == "completed":
            completed_.append(task["Task"])
        else:
            pending_.append(task["Task"])
    print(f"Completed Task : {len(completed_)}\n")  
    for i, task in enumerate(completed_):
        print(f"{i+1} : {task} ")
    print(f"Pending Task : {len(pending_)}\n")  
    for i, task in enumerate(pending_):
        print(f"{i+1} : {task} ")

def search_task():
    search_key = input("Provide search key here : ")
    matches = []
    for task in tasks:
        if search_key in task["Task"]:
            matches.append(task)
        else:
            print("No match found!")
    for i, task in enumerate(matches):
        print(f"{i} : {task["Task"]}\n")
    
def mark_completion():
    mark_item = input("Enter the task to mark as completed : ")
    for task in tasks:
        if mark_item == task["Task"]:
            task["Completion_status"] = "Completed"
            print(f"{task["Task"]} is marked as completed\n")
            return
    print(f"{mark_item} is not found!\n")

def operations(option):
    match option:
        case 1:
            add_task()
        case 2:
            rmv_task()
        case 3:
            view_task()
        case 4:
            task_stats()
        case 5:
            search_task()
        case 6:
            mark_completion()
        case 7:
            exit()
        case _:
            print("Enter the number in betweeen 0 - 7")

def main():
    print("Welcome to task Manager :)\n")
    while True:
        option = input("Choose an option: \n\t1. Add Task \n\t2. Remove Task \n\t3. View All Tasks \n\t4. Task Statistics \n\t5. Search Task \n\t6. Mark Task as Completed \n\t7. Exit \n\tyour option : ")
        if not option.isdigit():
            print("Only numbers are allowed\n")
            continue
        operations(int(option))

if __name__ == '__main__':
    main()