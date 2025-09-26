import streamlit as st
import random

# ---------- Page Config ----------
st.set_page_config(page_title="College Canteen", page_icon="🍴", layout="wide")

# ---------- Custom CSS ----------
page_bg = """
<style>
/* Background Gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f9f9f9, #e3f2fd);
    background-attachment: fixed;
}

/* Welcome Card Animation */
.welcome-box {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    padding: 25px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 4px 6px 15px rgba(0,0,0,0.2);
    animation: fadeIn 2s ease-in-out;
}
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(-20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Food Card Style */
.food-card {
    padding: 20px;
    margin: 10px;
    border-radius: 20px;
    box-shadow: 2px 4px 12px rgba(0,0,0,0.25);
    background-color: white;
    text-align: center;
    transition: transform 0.25s;
    position: relative;
}
.food-card:hover {
    transform: scale(1.05);
    box-shadow: 4px 8px 20px rgba(0,0,0,0.3);
}

/* Special Dish Card */
.special-card {
    background:#fff8e1; 
    border-left:6px solid #ff9800; 
    text-align:center;
    padding: 15px;
    border-radius:15px;
    margin-bottom:10px;
}

/* Bill Container */
.bill-container {
    background: linear-gradient(135deg, #fdf6e3, #e0f7fa);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---------- Welcome Section ----------
st.markdown("""
<div class="welcome-box">
    <h1>🍽 Welcome to Our College Canteen</h1>
    <p style="font-size:20px; color:#2e3b4e;">
        🌟 Good Food = Good Mood! Stay Happy 😋  
        <br>Explore today’s menu and place your order instantly 🚀
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- Weekly Menu ----------
weekly_menu = {
    "Monday": [
        {"name": "Poha", "price": 25},
        {"name": "Tea", "price": 10},
        {"name": "Vada Pav", "price": 20}
    ],
    "Tuesday": [
        {"name": "Idli", "price": 30},
        {"name": "Coffee", "price": 15},
        {"name": "Sandwich", "price": 40}
    ],
    "Wednesday": [
        {"name": "Pav Bhaji", "price": 50},
        {"name": "Cold Drink", "price": 25},
        {"name": "Samosa", "price": 15}
    ],
    "Thursday": [
        {"name": "Chole Bhature", "price": 60},
        {"name": "Lassi", "price": 30},
        {"name": "Pakora", "price": 20}
    ],
    "Friday": [
        {"name": "Masala Dosa", "price": 50},
        {"name": "Maggi", "price": 20},
        {"name": "Cake", "price": 70}
    ],
    "Saturday": [
        {"name": "Aloo Paratha", "price": 40},
        {"name": "Curd", "price": 20},
        {"name": "Spring Rolls", "price": 50}
    ]
}

special_dishes = {
    "Monday": "Poha with a twist of peanuts",
    "Tuesday": "Steamy Idli served with spicy chutney",
    "Wednesday": "Chole Bhature – the king of taste",
    "Thursday": "Maggi magic for your hunger",
    "Friday": "Crispy Dosa – south Indian delight",
    "Saturday": "Full Thali – feast like a king"
}

# ---------- Day Selection ----------
day = st.selectbox("📅 Select day of the week", list(weekly_menu.keys()))

# ---------- Special Dish ----------
st.markdown(f"""
<div class="special-card">
    <h3>🌟 Special Dish of the Day</h3>
    <p style="font-size:18px; color:#d84315;">{special_dishes[day]}</p>
</div>
""", unsafe_allow_html=True)

# ---------- Pop Button Toggle ----------
show_pop = st.checkbox("🍴 Show Dish Name Pop on Cards", value=True)

# ---------- Display Menu ----------
cols = st.columns(len(weekly_menu[day]))
quantities = {}

for i, item in enumerate(weekly_menu[day]):
    with cols[i]:
        st.markdown("<div class='food-card'>", unsafe_allow_html=True)
        
        # White Pop
        if show_pop:
            st.markdown(f"""
                <div style="
                    position:absolute;
                    top:10px;
                    left:50%;
                    transform:translateX(-50%);
                    background:white;
                    padding:5px 10px;
                    border-radius:12px;
                    box-shadow:1px 2px 5px rgba(0,0,0,0.2);
                    font-weight:bold;
                    z-index:10;
                    font-size:14px;
                ">
                    {item['name']}
                </div>
            """, unsafe_allow_html=True)
        
        # Placeholder Box (instead of image URL)
        st.markdown(f"<div style='background:#c8e6c9; height:150px; display:flex; align-items:center; justify-content:center; font-weight:bold;'>{item['name']}</div>", unsafe_allow_html=True)
        qty = st.number_input(f"Qty {item['name']}", 0, 10, 0, key=item["name"])
        quantities[item["name"]] = qty
        st.markdown("</div>", unsafe_allow_html=True)

# ---------- Bill & Payment ----------
st.markdown("---")
st.markdown("## 🛒 Place Your Order")

total = sum(item["price"] * quantities[item["name"]] for item in weekly_menu[day])

with st.container():
    st.markdown("<div class='bill-container'>", unsafe_allow_html=True)
    
    # Order Summary
    for item in weekly_menu[day]:
        if quantities[item["name"]] > 0:
            st.markdown(f"<p style='font-size:16px; color:#00695c;'>➡ {item['name']} x {quantities[item['name']]} = ₹{item['price']*quantities[item['name']]}</p>", unsafe_allow_html=True)

    st.markdown(f"<h3 style='color:#d84315;'>💰 Total Bill: ₹{total}</h3>", unsafe_allow_html=True)

    # Payment Options
    payment_mode = st.radio("💳 Select Payment Method", ["Online Payment", "Cash on Delivery", "Advance Payment"])

    # OTP Function
    def generate_otp():
        return random.randint(100000, 999999)

    if st.button("✅ Confirm Order"):
        if total > 0:
            if payment_mode == "Online Payment":
                st.success("🔗 Redirecting to Online Payment Gateway (Demo)...")
                if st.button("📲 Generate OTP"):
                    otp = generate_otp()
                    st.info(f"🔑 Your OTP is: {otp} (Demo)")

            elif payment_mode == "Cash on Delivery":
                st.success(f"💵 Pay ₹{total} when you receive your food.")

            elif payment_mode == "Advance Payment":
                st.success(f"✅ Please pay ₹{total} at counter first to confirm your advance booking.")
                if st.button("📲 Generate OTP for Advance Payment"):
                    otp = generate_otp()
                    st.info(f"🔑 Your OTP is: {otp} (Demo)")

            st.markdown("""
            <hr>
            <div style="text-align:center; font-size:18px; color:#1565c0;">
                🙏 Thank you for visiting our Canteen 🍴  
                <br>Come hungry, leave happy 😋  
            </div>
            <hr>
            """, unsafe_allow_html=True)
        else:
            st.warning("⚠ Please select at least one item to order.")

    st.markdown("</div>", unsafe_allow_html=True)
