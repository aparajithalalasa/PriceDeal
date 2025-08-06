import streamlit as st

# Mock user database
users = {
    "testuser": "password123"
}

def login():
    st.subheader("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if users.get(username) == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid credentials")

def signup():
    st.subheader("📝 Sign Up")
    new_user = st.text_input("Create Username")
    new_pass = st.text_input("Create Password", type="password")

    if st.button("Create Account"):
        if new_user in users:
            st.warning("User already exists")
        else:
            users[new_user] = new_pass
            st.success("Account created. Please log in.")
