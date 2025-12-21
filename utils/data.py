import pandas as pd
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "materials.xlsx")
def db():

    df = pd.read_excel(DATA_PATH)

    items = list(df['Item'].values)
    return items