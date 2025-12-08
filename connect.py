def connection():
    import gspread
    from google.oauth2.service_account import Credentials

    credential = "credentials.json"

    scopes = [
    'https://www.googleapis.com/auth/spreadsheets', # Access Sheets data
    'https://www.googleapis.com/auth/drive']

# Create credentials object from the JSON file
    creds = Credentials.from_service_account_file(
        credential, scopes=scopes)
    
    client = gspread.authorize(creds)
    return client