class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added successfully.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            print('Tasks:')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task}')

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{completed_task}" marked as completed.')
        else:
            print('Invalid task index.')

def main():
    task_manager = TaskManager()

    while True:
        print('\nTask Manager Menu:')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Complete Task')
        print('4. Exit')

        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            task = input('Enter the task: ')
            task_manager.add_task(task)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            task_manager.view_tasks()
            task_index = int(input('Enter the index of the task to mark as completed: '))
            task_manager.complete_task(task_index)
        elif choice == '4':
            print('Exiting Task Manager. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')

if __name__ == "__main__":
    main()
