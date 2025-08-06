import streamlit as st
from auth import login, signup
from catalog import show_catalog
from cart import view_cart

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None
if "cart" not in st.session_state:
    st.session_state.cart = []

# App Navigation
st.sidebar.title("🧭 Navigation")

if not st.session_state.logged_in:
    auth_page = st.sidebar.radio("Select", ["Login", "Sign Up"])
    if auth_page == "Login":
        login()
    else:
        signup()
else:
    page = st.sidebar.radio("Go to", ["Product Catalog", "View Cart", "Logout"])

    if page == "Product Catalog":
        show_catalog()
    elif page == "View Cart":
        view_cart()
    elif page == "Logout":
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.cart.clear()
        st.success("Logged out!")
