# Function to load tasks from a file
def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

# Initialize tasks by loading from the file
tasks = load_tasks()

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

# Function to view all tasks
def view_tasks():
    if tasks:
        print("Your tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks available.")

# Function to delete a task
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task removed: {removed_task}")
    else:
        print("Invalid task number.")

# Function to save tasks to a file
def save_tasks(filename="tasks.txt"):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved successfully.")

if __name__ == "__main__":
    add_task("Finish Python project")
    add_task("Start a new book")
    add_task("Get a job")
    view_tasks()
    delete_task(0)  # Removes the first task
    view_tasks()  # Shows the updated list of tasks
    save_tasks()  # Save tasks after making changes