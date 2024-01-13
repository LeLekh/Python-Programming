class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append({"name": task_name, "completed": False})

    def complete_task(self, task_name):
        for task in self.tasks:
            if task["name"] == task_name:
                task["completed"] = True
                print(f'Awesome! Task "{task_name}" marked as completed.')
                return
        print(f'Sorry, task "{task_name}" not found.')

    def show_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f'{index}. {task["name"]} ({status})')

def main():
    task_manager = TaskManager()

    while True:
        print("\n1. Add Task")
        print("2. Complete Task")
        print("3. Show Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task_name = input("Enter the task you want to add: ")
            task_manager.add_task(task_name)
        elif choice == "2":
            task_name = input("Enter the task you completed: ")
            task_manager.complete_task(task_name)
        elif choice == "3":
            task_manager.show_tasks()
        elif choice == "4":
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


