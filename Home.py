import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("To-Do App")
st.subheader("Developed by Erkan Gulec in Python")
st.write("This app will improve your <b>productivity</b>.",
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=index)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()

st.text_input(label="Enter a to-do item in the list above",
              on_change=add_todo, key="new_todo")
