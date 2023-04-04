import csv

def read_tasks(file):

    """
    Reads the tasks from the CSV file and returns a list of tasks.
    
    :param file: path to the file where tasks are stored
    :return: list of tasks (list)
    
    """
    # Create an empty list to store tasks
    tasks = []
    # Open the CSV file in read mode
    with open(file, 'r') as csvfile:
        # Create a CSV reader object
        reader = csv.reader(csvfile)
        # Iterate over each row in the CSV file
        for row in reader:
            # Add the row to the tasks list
            tasks.append(row)
    # Return the list of tasks
    return tasks

def write_tasks(file, tasks):

    """
    Writes the tasks to the CSV file.

    :param file: path to the file where tasks are stored
    :param tasks: list of tasks (list)
    :return: None

    """
    # Open the CSV file in write mode
    with open(file, 'w', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)
        # Write the tasks to the file
        writer.writerows(tasks)
        
