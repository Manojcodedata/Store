import streamlit as st
from utils.gsheets import get_worksheet
from utils.data import db

def purchase_page():
    st.title("🛒 Store Purchase")
    items = db()

    with st.form("purchase_form"):
        date = st.date_input("Purchase Date")
        item = st.selectbox("Item",items)
        supplier = st.selectbox("Supplier",['NTree','Pakka Fresh','Aradhya Gas','Ram Dev','Kwality Icecream','Baba Milk house','Junnu','Lemons','Farm Agro','Sarvana Milk','30 KL swathi water','Kanchi PVT LTD','Mehabood Pan','Arife','Dmart','Nirmala Pickle','Kaveri Rice','AV Enterprice','Hyperpure','Venkateshwara Coconuts Ramu','Manikanta Traders','Others','Tea Time','Rajamouli valet cards'])
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
