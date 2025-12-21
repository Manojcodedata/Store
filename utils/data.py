def db():
    import pandas as pd

    df = pd.read_excel("materials.xlsx")

    items = list(df['Item'].values)

    return items