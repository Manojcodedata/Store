import streamlit as st
from utils.gsheets import get_worksheet
from utils.data import db

def indents_page():
    items= db()
    st.title("📦 Store Indent / Dispatch")

    with st.form("indent_form"):
        date = st.date_input("Indent Date")
        indent_no = int(st.number_input("Indent Number"))
        department = st.selectbox("Department", ["Main_Kitchen","Juice","Grinding","Live_Kitchen","First_Floor","Coffee","House_Keeping","Counter_parcel","Cash_Counter","Cutting","Tea_Time","Others"])
        item = st.selectbox("Item Name",items)
        quantity = st.number_input("Quantity")
        

        submit = st.form_submit_button("Save Indent")

    if submit:
        sheet = get_worksheet("Store Sheet", "Indents")

        sheet.append_row([
            str(date),
            indent_no,
            item,
            department,
            quantity
        ])

        st.success(f"✅Item of Qty in saved in Store sheet → Indent")