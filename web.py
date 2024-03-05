import streamlit as st
import functions

todos = functions.get_ToDos()
def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    todos.append(todo)
    functions.write_ToDos(todos)
    clear_text()  #call function below

# function to clear the text box once the code has run
def clear_text():
    st.session_state["new_todo"] = ""

st.title("My ToDo App")
st.subheader("This is my ToDo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)  #removes the selected To Do from todos.txt
        functions.write_ToDos(todos)
        del st.session_state[todo] #refreshes the screen
        st.experimental_rerun()

st.text_input(label="blank",label_visibility="hidden", placeholder="Add new To Do....",key="new_todo",
              help="Hit enter to add", on_change=add_todo)  # Label is required, even if left ""