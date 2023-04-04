import sys
from datetime import datetime
from task_manager import read_tasks, write_tasks
from task_operation import display_tasks, view_task, add_task

def handle_view_all_tasks(tasks,file):
    """

    Handles the "View all tasks" option from the main menu.

    :param tasks: list of tasks (list)
    :param file: path to the file where tasks are stored
    :return: None


    """
    # Sort tasks by deadline
    sorted_tasks = sorted(tasks, key=lambda x: x[2])
    display_tasks(sorted_tasks)
    while True:
        # Get task number to view
        selected_task = input("Enter task number to view or 0 to go back: ")

        # check if the task number is valid
        try:
            selected_task = int(selected_task)
        # If the input is not a number, ask the user to enter a valid input
        except ValueError:
            print("Invalid input. Enter task number to view or 0 to go back!")
            continue

        # If the input is 0, go back to the main menu
        if selected_task == 0:
            break


        # check if the task number is valid
        if 1 <= selected_task <= len(sorted_tasks):
            # -1 because the task numbers start from 1
            view_task(sorted_tasks, selected_task - 1)
            delete_choice = input("Enter 'd' to delete task or any other key to go back: ")
            # Delete the selected task from the tasks list and write the updated list to file
            if delete_choice == 'd':
                tasks.remove(sorted_tasks[selected_task - 1])
                write_tasks(file, tasks)
        else:
            print("Invalid task number! Try again!")
            continue

        break

def handle_view_pending_tasks(tasks,file):
    """

    Handles the "View pending tasks" option from the main menu.

    :param tasks: list of tasks (list)
    :param file: path to the file where tasks are stored
    :return: None


    """
    # Filter pending tasks (deadline > today)
    pending_tasks = [task for task in tasks if datetime.strptime(task[2], "%Y-%m-%d") > datetime.now()]
    display_tasks(pending_tasks)
    while True:
        # Get task number to view
        selected_task = input("Enter task number to view or 0 to go back: ")
        # check if the task number is valid
        try:
            selected_task = int(selected_task)

        # If the input is not a number, ask the user to enter a valid input
        except ValueError:
            print("Invalid input. Enter task number to view or 0 to go back!")
            continue
        
        # If the input is 0, go back to the main menu
        if selected_task == 0:
            break
        
        # If the input is a valid task number, display the task details
        if 1 <= selected_task <= len(pending_tasks):
            view_task(pending_tasks, selected_task - 1)
            # Delete the selected task from the tasks list and write the updated list to file
            delete_choice = input("Enter 'd' to delete task or any other key to go back: ")
            if delete_choice == 'd':
                tasks.remove(pending_tasks[selected_task - 1])
                write_tasks(file, tasks)
        else:
            print("Invalid task number! Try again!")
            continue

        break

def handle_create_task(tasks,file):
    """

    Handles the "Create a new task" option from the main menu.

    :param tasks: list of tasks (list)
    :param file: path to the file where tasks are stored
    :return: None


    """
    while True:
        # Get task title
        title = input("Enter task title: ")

        # Check if the title is empty, ask the user to enter a valid input
        if not title:
            print("Title cannot be empty! Try again!")
            continue

        # Check if the title already exists, ask the user to enter a valid input
        if title in [task[0] for task in tasks]:
            print("Task with title '{}' already exists! Try again!".format(title))
            continue
        
        break
    
    while True:
        # Get task deadline
        deadline = input("Enter task deadline (YYYY-MM-DD): ")

        # Check if the deadline is empty
        if not deadline:
            print("Deadline cannot be empty!")
            continue
        
        # Check if the deadline is in the correct format
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
        
        # If the deadline is not in the correct format, ask the user to enter a valid input
        except ValueError:
            print("Invalid date format! Try again!")
            continue
        
        # Get task description
        print("Enter task description (Press Ctrl+D on Mac/Linux or Ctrl+Z on Windows to end input): ")
        # Description can be empty (optional)
        description = sys.stdin.read().strip()
        # Add the new task to the tasks list and write the updated list to file
        add_task(tasks, title, description, deadline)
        write_tasks(file, tasks)
        break


def main():
    """

    Main function to run the task manager application.
    :return: None
    
    """
    # Read tasks from file
    file = 'tasks.csv'
    tasks = read_tasks(file)
    # Display the main menu
    while True:
        print("\nMenu:")
        print("1. View all tasks")
        print("2. View pending tasks")
        print("3. Create a new task")
        print("4. Exit")
        # Get user choice
        choice = input("Enter your choice: ")
        # Handle user choice
        if choice == "1":
            print("\nAll tasks:")
            print("----------")
            handle_view_all_tasks(tasks,file)
            print("\n")

        elif choice == "2":
            print("\nPending tasks:")
            print("--------------")
            handle_view_pending_tasks(tasks,file)
            print("\n")
           
        elif choice == "3":
            print("\n***** Create a new task ***** \n")
            handle_create_task(tasks,file)
            print("\n")

        elif choice == "4":
            break
        # If the user enters an invalid choice, ask the user to enter a valid input
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()
