# canteen-weekly-menu-by-vishakha-
“Week-wise College Canteen Menu Project”)
# canteen_streamlit.py
import streamlit as st

# Weekly menu
weekly_menu = {
    "Monday": {1: ("Poha", 20), 2: ("Tea", 10), 3: ("Samosa", 15)},
    "Tuesday": {1: ("Idli", 30), 2: ("Coffee", 15), 3: ("Sandwich", 40)},
    "Wednesday": {1: ("Paratha", 25), 2: ("Lassi", 30), 3: ("Chole Bhature", 50)},
    "Thursday": {1: ("Maggi", 25), 2: ("Tea", 10), 3: ("Pakora", 20)},
    "Friday": {1: ("Dosa", 40), 2: ("Cold Drink", 20), 3: ("Vada Pav", 15)},
    "Saturday": {1: ("Thali", 80), 2: ("Roti Sabzi", 50), 3: ("Jalebi", 30)},
    "Sunday": {1: ("Chole Kulche", 60), 2: ("Ice Cream", 40), 3: ("Pasta", 50)}
}

# Special dish
special_dish = {
    "Monday": "Poha with a twist of peanuts",
    "Tuesday": "Steamy Idli served with spicy chutney",
    "Wednesday": "Chole Bhature – the king of taste",
    "Thursday": "Maggi magic for your hunger",
    "Friday": "Crispy Dosa – south Indian delight",
    "Saturday": "Full Thali – feast like a king",
    "Sunday": "Chole Kulche – perfect Sunday vibes"
}

st.title("🍽 Welcome to the College Canteen")
st.subheader("Good food = Good mood! Stay Happy 😄")

# Day selection
day = st.selectbox("Select day of the week", list(weekly_menu.keys()))

menu = weekly_menu[day]
st.write(f"### Menu for {day}")
for key, value in menu.items():
    st.write(f"{key}. {value[0]} - Rs.{value[1]}")

st.write(f"*Special Dish:* {special_dish[day]}")

st.write("---")
st.write("### Place your order")

# Order input
order = {}
for key, value in menu.items():
    qty = st.number_input(f"{value[0]} (Rs.{value[1]})", min_value=0, step=1, key=key)
    if qty > 0:
        order[key] = qty

# Calculate bill
if st.button("Generate Bill"):
    if order:
        st.write("### 🧾 Bill Receipt")
        total = 0
        for item_no, qty in order.items():
            item, price = menu[item_no]
            cost = price * qty
            total += cost
            st.write(f"{item} x {qty} = Rs.{cost}")
        st.write(f"*Total Bill = Rs.{total}*")
        st.success("Thank you for visiting our Canteen! Come hungry, leave happy 😋")
    else:
        st.warning("No items selected. Visit again when hungry!")
