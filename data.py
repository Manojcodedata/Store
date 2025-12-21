def db():
    departments = ["Main_Kitchen","Juice","Grinding","Live_Kitchen","First_Floor","Coffee","House_Keeping","Counter_parcel","Cash_Counter","Cutting","Tea_Time","Others"]
    import pandas as pd

    df = pd.read_excel("Material Master.xlsx")

    items = list(df['Item'].values)

    return departments, items