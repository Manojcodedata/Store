import gspread
from google.oauth2.service_account import Credentials
from config.settings import SPREADSHEETS
import os

def get_worksheet(spreadsheet_name, worksheet_name):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    creds_path = os.path.join(BASE_DIR, "credentials", "credentials.json")

    creds = Credentials.from_service_account_file(
        creds_path,
        scopes=scopes
    )

    client = gspread.authorize(creds)
    spreadsheet = client.open(spreadsheet_name)

    return spreadsheet.worksheet(worksheet_name)