def connection():
    import gspread
    import streamlit as st
    from google.oauth2.service_account import Credentials

    #credential = st.secrets["service_account"]
    credential = credentials.json

    scopes = [
    'https://www.googleapis.com/auth/spreadsheets', # Access Sheets data
    'https://www.googleapis.com/auth/drive']

# Create credentials object from the JSON file
    creds = Credentials.from_service_account_info(
        credential, scopes=scopes)
    
    client = gspread.authorize(creds)

    return client

