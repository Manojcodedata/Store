def db():
    departments = ["Main Kitchen","Juice","Grinding","Dosa","Parotta","Poori_Snacks","First_Floor","Coffee","House Keeping","Parcel"]
    import pandas as pd

    df = pd.read_excel("Material Master.xlsx")

    items = list(df['Item'].values)

    return departments, items