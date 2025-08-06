import streamlit as st

def show_catalog():
    st.title("🛍️ Product Catalog")

    products = [
        {"id": 1, "name": "iPhone 15", "price": 85000, "desc": "Apple smartphone with A16 chip"},
        {"id": 2, "name": "Pixel 7", "price": 70000, "desc": "Google flagship AI phone"},
        {"id": 3, "name": "OnePlus 11", "price": 59999, "desc": "Flagship killer with smooth UI"},
        {"id": 4, "name": "Samsung S23", "price": 80000, "desc": "High-end Samsung Galaxy"},
    ]

    for product in products:
        with st.container(border=True):
            st.subheader(product["name"])
            st.write(product["desc"])
            st.write(f"💰 ₹{product['price']}")
            if st.button(f"Add to Cart - {product['name']}", key=product["id"]):
                st.session_state.cart.append(product)
                st.success(f"Added {product['name']} to cart!")
