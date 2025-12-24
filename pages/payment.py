import streamlit as st
from utils.gsheets import get_worksheet

def payments_page():
    st.title("💰 Vendor Payment")

    with st.form("payment_form"):
        date = st.date_input("Payment Date")
        vendor = st.selectbox("Vendor Name",['Nirmala Traders','Maintainance_Repair','Pakka Fresh','Aradhya Gas','Ram Dev','Kwality Icecream','Baba Milk house','Junnu','DSY Water','coconut water','MD Jahangeer Lemons','Konaseema coconuts','Farm Agro','Sarvana Milk','30 KL swathi water','Kanchi PVT LTD','Mehabood Pan','Arife','Dmart','Nirmala Pickle','Kaveri Rice Mills','AV Enterprice','Hyperpure','Venkateshwara Coconuts Ramu','Manikanta Traders Gajaraj rice','Coconut Water','AV Enterprises Tea Time','Giridhar Enterprices valet cards','Online order','Venkateshwara charcoal','Market Fruits_vegetables'])
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
