from connect import *
import streamlit as st
from data import *

departments, items= db()
client = connection()

# select the sheet

sheet_name = st.text_input("Select the sheet name")

#Date sheet
target_date = st.text_input("Enter the sheet date")

vocherid = st.text_input("Enter the vocher number")
department = st.selectbox("Select the department",departments)
item = st.selectbox("Select the item",items)
indent_qty = st.text_input("Enter the Quantity")

if st.button("Save"):
    sheet = client.open(sheet_name)
    target_sheet = sheet.worksheet(target_date)
    new = [vocherid,department,item,indent_qty]
    # Update a cell
    target_sheet.append_row(new)
    st.write("Updated")

# Append a new row
#sheet.append_row(["Sai", "Manoj", "Data Scientist", "India"])

#print("Data updated successfully ✅")