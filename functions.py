FILEPATH = "ToDos.txt"
def get_ToDos(): #Function Definition code
    """ Read a text file and return the list of To-do items."""
    with open(FILEPATH, 'r') as file_local:  # Simplifies the rows of code below, now comented out
        ToDos_Local = file_local.readlines()
    return ToDos_Local


def write_ToDos(ToDosList): #Function Definition code with parameters
    """ Write the To-do items list into the text file."""
    with open(FILEPATH, 'w') as file:
        file.writelines(ToDosList)


#To prevent further code from running (printing) in the calling module,
#add the conditional If statement below to only print the messages
#where the name of the calling file is the 'main' one they actually sit in

if __name__ =="__main__":  #the code is run in the 'main' file where the functions sit
    print("hello from functions")
    print(get_ToDos())
