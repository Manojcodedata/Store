import pandas as pd
import os

def db():
    base_dir = os.path.dirname(os.path.dirname(__file__))

    file_path = os.path.join(base_dir, "materials.xlsx")

    df = pd.read_excel(file_path)

    items = list(df['Item'].values)
    return items