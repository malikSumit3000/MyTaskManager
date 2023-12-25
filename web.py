import streamlit as st

import functions

todos = functions.get_todos()


def add_todos():
    new_todo = st.session_state["new_todo"]
    for todo in todos:
        if new_todo == todo:
            st.experimental_rerun()
    todos.append(new_todo + '\n')
    functions.write_todos(todos)


st.title('Task Manager')
st.subheader('Add or Complete your tasks')
st.text('Increase your productivity with my task manager')

for index, todo in enumerate(todos):
    checked = st.checkbox(todo, key=todo)
    if checked:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder='Add todo here...', on_change=add_todos, key='new_todo')
