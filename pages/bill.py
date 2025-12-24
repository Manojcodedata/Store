import streamlit as st
from utils.gsheets import get_worksheet
from utils.data import db

def bills_entry_page():
    items= db()
    st.title("🧾 Vendor Bill Entry")

    with st.form("bill_form"):
        date = st.date_input("Bill Date")
        vendor = st.selectbox("Vendor Name",['Nirmala Traders','Maintainance_Repair','Pakka Fresh','Aradhya Gas','Ram Dev','Kwality Icecream','Baba Milk house','Junnu','DSY Water','coconut water','MD Jahangeer Lemons','Konaseema coconuts','Farm Agro','Sarvana Milk','30 KL swathi water','Kanchi PVT LTD','Mehabood Pan','Arife','Dmart','Nirmala Pickle','Kaveri Rice Mills','AV Enterprice','Hyperpure','Venkateshwara Coconuts Ramu','Manikanta Traders Gajaraj rice','Coconut Water','AV Enterprises Tea Time','Giridhar Enterprices valet cards','Online order','Venkateshwara charcoal','Market Fruits_vegetables'])
        bill_no = st.text_input("Bill Number")
        item = st.selectbox("Item Purchased",items)
        amount = st.number_input("Bill Amount", min_value=0.0)

        submit = st.form_submit_button("Save Bill")

    if submit:
        sheet = get_worksheet("Vendor Payments", "Vendor_bill")

        sheet.append_row([
            str(date),
            vendor,
            bill_no,
            item,
            amount
        ])

        st.success("✅ Bill saved in Vendors → Bill")