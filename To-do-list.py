# This program immplements a simple to-do list application using a list to store tasks. Users can add, view, and remove tasks from the list.
print("\n‖ Welcome to the To-Do List Application!")
# Initialize an empty list to store tasks
to_do_list = []

# Function to add a task to the to-do list
def add_task(task):
    '''Adds a task to the to-do list'''
    to_do_list.append(task)
    print(f'☞)Task [{task}] is added to the list.')

# Function to view all tasks in the to-do list
def view_tasks():
       "''Displays all tasks in the to-do list'''"
       if not to_do_list:
           print("The to-do list is empty.")
       else:
           print("To-Do List:")
           for index,tasks in enumerate(to_do_list, start=1):
               print(f"{index}. {tasks}")

# function to remove task from the to-do list by its number                           
def remove_task(task_number):
    "''Removes a task from the to-do list by its number'''"
    x=task_number -1
    to_do_list.pop(x)
    print(f"\n☞)Task [{task_number}] is removed from the list.")

while True:
    print("\n📋 TO-DO LIST MENU")
    print("1. ➕ Add Task")
    print("2. 👀 View Tasks")
    print("3. ❌ Delete Task")
    print("4. 🚪 Exit")
    user_choice = input("\n🤔_Enter your choice [1-4]: ")
    if user_choice in ('1', '2', '3', '4'):
       
       if user_choice == '1':
             task = input("\nEnter the task that you want to add to-do list: ")
             add_task(task)
       elif user_choice == '2':
             view_tasks()
       elif user_choice == '3':
             task_remove = int(input("\nEnter the task number that you want to remove from to-do list: "))
             remove_task(task_remove)
       else:
            break  
    else:
         print("Please enter the correct input!") 
    print("\n" + "="*30)
    print("✅ Task Completed Successfully 🎉")
    print("="*30)

print("\nThank you for using the To-Do List Application! Goodbye! 👋")
print("This program is created by [Abdul-Rehman Azam]\n")