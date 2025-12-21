import streamlit as st
from pages.purchase import purchase_page
from pages.indents import indents_page
from pages.payment import payments_page
from pages.bill import bills_entry_page

st.sidebar.title("🏪 Management Panel")

menu = st.sidebar.radio(
    "Select Module",
    [
        "Vendor Bills",
        "Vendor Payments",
        "Store Purchases",
        "Store Indents"
    ]
)


if menu == "Vendor Bills":
    bills_entry_page()

elif menu == "Vendor Payments":
    payments_page()

elif menu == "Store Purchases":
    purchase_page()

elif menu == "Store Indents":
    indents_page()