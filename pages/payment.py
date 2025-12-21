import streamlit as st
from utils.gsheets import get_worksheet

def payments_page():
    st.title("💰 Vendor Payment")

    with st.form("payment_form"):
        date = st.date_input("Payment Date")
        vendor = st.selectbox("Vendor Name",['NTree','Pakka Fresh','Aradhya Gas','Ram Dev','Kwality Icecream','Baba Milk house','Junnu','Lemons','Farm Agro','Sarvana Milk','30 KL swathi water','Kanchi PVT LTD','Mehabood Pan','Arife','Dmart','Nirmala Pickle','Kaveri Rice','AV Enterprice','Hyperpure','Venkateshwara Coconuts Ramu','Manikanta Traders','Others','Tea Time','Rajamouli valet cards'])
        mode = st.selectbox("Payment Mode", ["Cash", "UPI", "Bank Transfer"])
        amount = st.number_input("Amount Paid", min_value=0.0)

        submit = st.form_submit_button("Save Payment")

    if submit:
        sheet = get_worksheet("Vendor Payments", "Payment")

        sheet.append_row([
            str(date),
            vendor,
            mode,
            amount
        ])

        st.success("✅ Payment saved in Vendors → Payment")
