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
        if department == 'Grinding':
            item = st.selectbox('Grinding_Item',['Masala Dosa','Chitti Pesarattu','Idly','Rice Flour','Kal Dosa','Paper Dosa','Rava Mixing','Green Chutney','Red Chutney','Temple Pulihora','Dosa Garlic Paste','Sambar Masala','Elaneer Payasam','Peanut chutney','Idly Podi'])
            quantity = st.number_input("Quantity of item")
              
        else:
            item = st.selectbox("Item Name",items)
            quantity = st.number_input("Quantity")
        

        submit = st.form_submit_button("Save Indent")

    if submit:
        sheet = get_worksheet("Store Sheet", "Indents")

        if department == 'Grinding':
            if item == 'Masala Dosa':
                if quantity == 8:
                    rows = [[str(date),indent_no,'Dosa Rice',department,8],
                            [str(date),indent_no,'Round Urad Dal',department,0.8],
                            [str(date),indent_no,'Boiled Rice',department,0.420],
                            [str(date),indent_no,'Chana Dal',department,0.080],
                            [str(date),indent_no,'Poha',department,0.270],
                            [str(date),indent_no,'Methi',department,0.100]]
                elif quantity == 10:
                    [[str(date),indent_no,'Dosa Rice',department,10],
                            [str(date),indent_no,'Round Urad Dal',department,1],
                            [str(date),indent_no,'Boiled Rice',department,0.530],
                            [str(date),indent_no,'Chana Dal',department,0.100],
                            [str(date),indent_no,'Poha',department,0.330],
                            [str(date),indent_no,'Methi',department,0.110]]
                elif quantity == 12:
                    rows = [[str(date),indent_no,'Dosa Rice',department,12],
                            [str(date),indent_no,'Round Urad Dal',department,1.2],
                            [str(date),indent_no,'Boiled Rice',department,0.630],
                            [str(date),indent_no,'Chana Dal',department,0.120],
                            [str(date),indent_no,'Poha',department,0.400],
                            [str(date),indent_no,'Methi',department,0.130]]
                elif quantity == 13:
                    rows = [[str(date),indent_no,'Dosa Rice',department,13],
                            [str(date),indent_no,'Round Urad Dal',department,1.3],
                            [str(date),indent_no,'Boiled Rice',department,0.690],
                            [str(date),indent_no,'Chana Dal',department,0.130],
                            [str(date),indent_no,'Poha',department,0.430],
                            [str(date),indent_no,'Methi',department,0.150]]
                elif quantity == 15:
                    rows = [[str(date),indent_no,'Dosa Rice',department,15],
                            [str(date),indent_no,'Round Urad Dal',department,1.5],
                            [str(date),indent_no,'Boiled Rice',department,0.800],
                            [str(date),indent_no,'Chana Dal',department,0.150],
                            [str(date),indent_no,'Poha',department,0.500],
                            [str(date),indent_no,'Methi',department,0.270]]
                elif quantity == 5:
                    rows = [[str(date),indent_no,'Dosa Rice',department,5],
                            [str(date),indent_no,'Round Urad Dal',department,0.500],
                            [str(date),indent_no,'Boiled Rice',department,0.270],
                            [str(date),indent_no,'Chana Dal',department,0.050],
                            [str(date),indent_no,'Poha',department,0.170],
                            [str(date),indent_no,'Methi',department,0.060]]
                else:
                    st.write("Please enter correct quantity")
                sheet.append_rows(
                rows)
        else:
            sheet.append_row([
                str(date),
                indent_no,
                item,
                department,
                quantity
            ])
        st.success(f"✅Item of Qty in saved in Store sheet → Indent")