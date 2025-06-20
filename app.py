import streamlit as st

st.title("AI Talking Video App")
st.write("Welcome to your first Streamlit app!")
st.write("This is just a basic starter template. You can modify it anytime.")

# Example input
user_input = st.text_input("Type something here:")
if user_input:
    st.success(f"You typed: {user_input}")
