import streamlit as st

def view_cart():
    st.title("🛒 Your Shopping Cart")

    if not st.session_state.cart:
        st.info("Your cart is empty.")
        return

    total = 0
    for idx, item in enumerate(st.session_state.cart):
        st.write(f"{idx+1}. {item['name']} - ₹{item['price']}")
        total += item["price"]

    st.markdown(f"### 🧾 Total: ₹{total}")

    if st.button("Clear Cart"):
        st.session_state.cart.clear()
        st.success("Cart cleared!")
