import streamlit as st

def milk_calculator():
    price_per_litre = 52  # fixed price

    st.title("🥛 Milk Rate Calculator")

    # choose unit
    unit = st.radio("Select unit:", ("Liters", "Milliliters"))

    if unit == "Liters":
        amount = st.number_input("Enter amount (Liters per day)", min_value=0.0, step=0.1)
        liters_per_day = amount
    else:
        amount = st.number_input("Enter amount (Milliliters per day)", min_value=0.0, step=50.0)
        liters_per_day = amount / 1000  # convert ml → liters

    days = st.number_input("Number of days", min_value=1, step=1)

    if st.button("Calculate"):
        total_cost = liters_per_day * price_per_litre * days
        st.success(f"Milk cost for {amount} {unit}/day over {days} days = ₹{total_cost:.2f}")

milk_calculator()
