import streamlit as st
from utils.gsheets import get_worksheet

def payments_page():
    st.title("💰 Vendor Payment")

    with st.form("payment_form"):
        date = st.date_input("Payment Date")
<<<<<<< HEAD
        vendor = st.selectbox("Vendor Name",['Nirmala Traders','Maintainance_Repair','Pakka Fresh','Aradhya Gas','Ram Dev','Kwality Icecream','Baba Milk house','Junnu','DSY Water','coconut water','MD Jahangeer Lemons','Konaseema coconuts','Farm Agro','Sarvana Milk','30 KL swathi water','Kanchi PVT LTD','Mehabood Pan','Arife','Dmart','Nirmala Pickle','Kaveri Rice Mills','AV Enterprice','Hyperpure','Venkateshwara Coconuts Ramu','Manikanta Traders Gajaraj rice','Coconut Water','AV Enterprises Tea Time','Giridhar Enterprices valet cards','Manasa Dairy','Online order','Venkateshwara charcoal','Market Fruits_vegetables'])
=======
        vendor = st.selectbox("Vendor Name",['Nirmala Traders','Maintainance_Repair','Pakka Fresh','Aradhya Gas','Ram Dev','Kwality Icecream','Baba Milk house','Junnu','DSY Water','coconut water','MD Jahangeer Lemons','Konaseema coconuts','Farm Agro','Sarvana Milk','30 KL swathi water','Kanchi PVT LTD','Mehabood Pan','Arife','Dmart','Nirmala Pickle','Kaveri Rice Mills','AV Enterprice','Hyperpure','Venkateshwara Coconuts Ramu','Manikanta Traders Gajaraj rice','Coconut Water','AV Enterprises Tea Time','Giridhar Enterprices valet cards','Manasa Dairy','Online order','Venkateshwara charcoal','Market Fruits_vegetables','Local Purchase','SS_fitness(cold pressed Juice)','Bal Reddy(sadguru veg)'])
>>>>>>> a5d6da6776d6e919bb74dbe7be2218a959906121
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
