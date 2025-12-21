import gspread
from google.oauth2.service_account import Credentials
from config.settings import SPREADSHEETS

def get_worksheet(spreadsheet_name, worksheet_name):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=scopes
    )

    client = gspread.authorize(creds)
    spreadsheet = client.open(spreadsheet_name)

    return spreadsheet.worksheet(worksheet_name)