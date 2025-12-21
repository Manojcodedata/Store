import streamlit as st
import base64
from pages.purchase import purchase_page
from pages.indents import indents_page
from pages.payment import payments_page
from pages.bill import bills_entry_page

def add_bg_from_local(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.set_page_config(page_title="Store & Vendor Management", layout="wide")

add_bg_from_local("assets/background.png")

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