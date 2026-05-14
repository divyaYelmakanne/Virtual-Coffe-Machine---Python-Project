import streamlit as st
import time

# PAGE SETTINGS
st.set_page_config(
    page_title="Virtual Coffee Machine",
    page_icon="☕",
    layout="centered"
)

# TITLE
st.title("☕ Virtual Coffee Machine")
st.write("Welcome to the Python Coffee Cafe ☕")


# MENU
MENU = {
    "Espresso": 85,
    "Latte": 125,
    "Cappuccino": 150,
    "Americano": 110,
    "Mocha": 170,
    "Black Coffee": 90,
    "Hot Chocolate": 140,
    "Cold Coffee": 160,
    "Green Tea": 60,
    "Masala Tea": 70
}


# CUSTOMER NAME
name = st.text_input("👤 Enter Your Name")


# DRINK SELECTION
drink = st.selectbox(
    "☕ Choose Your Drink",
    list(MENU.keys())
)


# SHOW PRICE
price = MENU[drink]

st.info(f"💰 Price of {drink}: Rs{price}")


# PAYMENT
money = st.number_input(
    "💵 Enter Amount",
    min_value=0,
    step=5
)


# SUGAR LEVEL
sugar = st.slider(
    "🍬 Sugar Level",
    0,
    5,
    2
)


# SIZE
size = st.radio(
    "🥤 Select Size",
    ["Small", "Medium", "Large"]
)


# BUY BUTTON
if st.button("☕ Make Coffee"):

    if name == "":
        st.warning("Please enter your name")

    else:

        if money >= price:

            change = money - price

            st.success(f"✅ Payment Successful")

            # PROGRESS BAR
            progress = st.progress(0)

            for i in range(100):
                time.sleep(0.02)
                progress.progress(i + 1)

            st.balloons()

            st.success(
                f"☕ Here is your {size} {drink}, {name}!"
            )

            st.info(f"🍬 Sugar Level: {sugar}")

            st.info(f"💵 Change Returned: Rs{change}")

            # BILL
            st.subheader("🧾 BILL")

            st.write(f"👤 Customer : {name}")
            st.write(f"☕ Drink : {drink}")
            st.write(f"🥤 Size : {size}")
            st.write(f"🍬 Sugar : {sugar}")
            st.write(f"💰 Cost : Rs{price}")
            st.write(f"💵 Paid : Rs{money}")
            st.write(f"🪙 Change : Rs{change}")

            # RATING
            rating = st.slider(
                "⭐ Rate Our Coffee",
                1,
                5,
                5
            )

            st.success(
                f"🙏 Thank You For Giving {rating} Stars!"
            )

        else:

            st.error(
                "❌ Not enough money. Please insert more money."
            )


# SIDEBAR
st.sidebar.title("📋 Coffee Menu")

for item, cost in MENU.items():
    st.sidebar.write(f"☕ {item} - Rs{cost}")


# FOOTER
st.markdown("---")
st.caption("Made with ❤️ using Python & Streamlit")
