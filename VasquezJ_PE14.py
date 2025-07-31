# script that manages a **task list** using a dictionary.


def main():
    task_list = {}
    while True:
        print('\nType 1: To Add a Task')
        print('Type 2: To Mark A Task Complete')
        print('Type 3: To Display All Tasks')
        print('Type 4: To Quit')
        selection = input('\nEnter number to continue: ')

        if selection == '1':
            print('\nADDING TASK')
            task = input('Enter task name: ')
            status = 'Pending'
            print(new_task(task_list, task, status))

        elif selection == '2':
            print('\nMARK A TASK AS COMPLETE')
            task = input('Enter task name to complete: ')
            print(complete_task(task_list, task))

        elif selection == '3':
            print('\nDISPLAYING ALL TASKS:\nTask List')
            if task_list == {}:
                print('*List empty, try again*\n')
            else:
                display_tasks(task_list, task, status)
        elif selection == '4':
            break
    else:
            print('Your choices are: 1, 2, 3, Exit.\n')


def new_task(task_list, task, status):
    if task not in task_list:
        task_list[task] = status
        return 'Task added!'
    else:
        return 'Task already in system'

def complete_task(task_list, task):
    if task in task_list:
        task_list[task] = 'Complete'
        return 'Task marked as Completed!'
    else:
        return '*Task not in list, try again*\n'

def display_tasks(task_list, task, status):
    for key, value in task_list.items():
        print(f'- {key}: {value}')


if __name__ == '__main__':
    main()
