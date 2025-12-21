def db():
    import pandas as pd

    df = pd.read_excel("Material Master.xlsx")

    items = list(df['Item'].values)

    return items