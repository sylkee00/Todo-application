
def display_tasks(tasks):
    """
    Displays the tasks in a numbered list.
    
    :param tasks: list of tasks 
    :return: None
    
    """
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task[0]}")

def view_task(tasks, index):
    """
    Displays the details of a task.
    
    :param tasks: list of tasks (list)
    :param index: index of the task to be displayed (int)
    :return: None
    
    """
    task = tasks[index]
    print(f"\nTitle: {task[0]}\nDescription: {task[1]}\nDeadline: {task[2]} \n")

def add_task(tasks, title, description, deadline):
    """
    Adds a new task to the list of tasks.

    :param tasks: list of tasks (list)
    :param title: title of the task (str)
    :param description: description of the task (str)
    :param deadline: deadline of the task (str)
    :return: None

    """
    tasks.append([title, description, deadline])