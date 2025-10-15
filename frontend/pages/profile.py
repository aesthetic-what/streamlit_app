import streamlit as st

data = st.session_state
print(data)

label = st.title(f"Hello {data["username"]}", anchor=False)