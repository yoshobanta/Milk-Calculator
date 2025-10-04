import streamlit as st
from datetime import datetime
import calendar

def milk_calculator():
    st.title("🥛 Milk Rate Calculator")

    # --- Custom Price Input ---
    price_per_litre = st.number_input("Milk Price per Litre (₹)", min_value=1, value=52, step=1)

    # --- Unit Selector ---
    unit = st.radio("Select unit:", ("Milliliters", "Liters"))

    # --- Default values ---
    default_ml = 750
    default_liters = 0.75  # equivalent to 750 ml

    if unit == "Liters":
        amount_str = st.text_input("Enter amount (Liters per day)", value=str(default_liters))
    else:
        amount_str = st.text_input("Enter amount (Milliliters per day)", value=str(default_ml))

    # convert safely
    try:
        amount = float(amount_str) if amount_str else 0
    except ValueError:
        st.error("⚠️ Please enter a valid number")
        return

    liters_per_day = amount if unit == "Liters" else amount / 1000

    # --- Month Selector ---
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    today = datetime.now()
    previous_month_index = (today.month - 2) % 12  # previous month index (0-based)
    default_month_name = months[previous_month_index]

    # Calculate number of days in selected month
    year_for_month = today.year
    # if previous month is December, year decreases by 1
    if previous_month_index == 11 and today.month == 1:
        year_for_month -= 1

    days_in_month = calendar.monthrange(year_for_month, previous_month_index + 1)[1]

    selected_month = st.selectbox("Select Month", months, index=previous_month_index)
    # update days based on selected month
    selected_month_index = months.index(selected_month)
    if selected_month_index == 1:  # February
        days = calendar.monthrange(year_for_month, 2)[1]
    else:
        days = calendar.monthrange(year_for_month, selected_month_index + 1)[1]

    # --- Calculate ---
    if st.button("Calculate Bill"):
        total_cost = liters_per_day * price_per_litre * days

        st.markdown(
            f"""
            <div style="text-align:center; padding:20px; border-radius:15px; background-color:#f0f8ff;">
                <h2>📅 Month: {selected_month} ({days} days)</h2>
                <h1 style="color:#2E86C1; font-size: 40px;">💰 Final Bill: ₹{total_cost:,.2f}</h1>
                <p style="font-size:18px;">({amount} {unit}/day × ₹{price_per_litre} × {days} days)</p>
            </div>
            """,
            unsafe_allow_html=True
        )

milk_calculator()
