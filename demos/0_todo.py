import streamlit as st

st.title("Simple Todo App")

if "todos" not in st.session_state:
    st.session_state.todos = []

with st.form("Add Todo"):
    todo = st.text_input("Task", placeholder="Enter a task")
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    submitted = st.form_submit_button("Add Task")
    
    if submitted and todo:
        st.session_state.todos.append({"task": todo, "priority": priority})
        st.success("Task added!")

st.subheader("Todo List")
if st.session_state.todos:
    for index, todo in enumerate(st.session_state.todos):
        with st.container(border=1):
            col1, col2 = st.columns([6, 1])
            with col1:
                st.write(f"{todo['task']} ({todo['priority']} priority)")
            with col2:
                delete_button = st.button(f"Remove", key=f"del_{index}")
                if delete_button:
                    del st.session_state.todos[index]
                    st.rerun()
else:
    st.info("No tasks")