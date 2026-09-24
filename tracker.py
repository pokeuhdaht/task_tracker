import json

#create a task
def addTask():
    print("add task")

#update a specific task as defined by the user
def updateTask():
    print("update task")

#delete the task as created by the user
def deleteTask():
    print("delete task")



def main():
    print("Task Tracker")
    print("Enter 'help' for assistance.")
    looping = True
    while looping == True:
        userInput = input("> ")
        userInput = userInput.lower()
        if userInput.lower()=='exit':
            looping = False
        elif userInput.lower()=='add':
            addTask()
        elif userInput=='help':
            print(f"add\nUsed to add a new task to the tracker.")
        else:
            print("not an available command")

if __name__=="__main__":
    main()
    exit()

