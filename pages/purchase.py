import streamlit as st
from utils.gsheets import get_worksheet
from utils.data import db

def purchase_page():
    st.title("🛒 Store Purchase")
    items = db()

    with st.form("purchase_form"):
        date = st.date_input("Purchase Date")
        item = st.selectbox("Item",items)
        supplier = st.selectbox("Supplier",['Nirmala Traders','Maintainance_Repair','Pakka Fresh','Aradhya Gas','Ram Dev','Kwality Icecream','Baba Milk house','Junnu','DSY Water','coconut water','MD Jahangeer Lemons','Konaseema coconuts','Farm Agro','Sarvana Milk','30 KL swathi water','Kanchi PVT LTD','Mehabood Pan','Arife','Dmart','Nirmala Pickle','Kaveri Rice Mills','AV Enterprice','Hyperpure','Venkateshwara Coconuts Ramu','Manikanta Traders Gajaraj rice','Coconut Water','AV Enterprises Tea Time','Rajamouli (Priting material)','Manasa Dairy','Online order','Venkateshwara charcoal','Market Fruits_vegetables','Local Purchase','SS_fitness(cold pressed Juice)','Bal Reddy(sadguru veg)'])
        qty = st.number_input("Quantity")
        price = st.number_input("Unit Price", min_value=0.0)

        submit = st.form_submit_button("Save Purchase")

    if submit:
        sheet = get_worksheet("Store Sheet", "Purchases")

        sheet.append_row([
            str(date),
            item,
            supplier,
            qty,
            price
        ])

        st.success("✅ Purchase saved in Store → Purchases")
