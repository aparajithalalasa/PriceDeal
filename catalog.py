import streamlit as st

# Sample product data
products = [
    {"id": 1, "name": "iPhone 15", "price": 85000, "desc": "Apple smartphone with A16 chip"},
    {"id": 2, "name": "Pixel 7", "price": 70000, "desc": "Google's flagship with AI camera"},
    {"id": 3, "name": "OnePlus 11", "price": 59999, "desc": "Performance phone with clean UI"},
    {"id": 4, "name": "Samsung S23", "price": 80000, "desc": "Premium Samsung Galaxy device"},
]

# Initialize cart if not in session state
if "cart" not in st.session_state:
    st.session_state.cart = []

st.title("🛒 Product Catalog")

# Display all products
for product in products:
    with st.container(border=True):
        st.subheader(product["name"])
        st.write(product["desc"])
        st.write(f"💰 Price: ₹{product['price']}")

        if st.button(f"Add to Cart - {product['name']}", key=product["id"]):
            st.session_state.cart.append(product)
            st.success(f"Added {product['name']} to cart!")
