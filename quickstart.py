from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from gspread import *

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
# Google sheet budget link: https://docs.google.com/spreadsheets/d/1WvDjq4OBjNx5sAm6QVSl2NntG0pA_jrOMKFVCXKKiJc/edit?usp=sharing
SAMPLE_SPREADSHEET_ID = '1WvDjq4OBjNx5sAm6QVSl2NntG0pA_jrOMKFVCXKKiJc'
SAMPLE_RANGE_NAME = 'Feb!A1:M32'

# Helpful tutorial: https://www.makeuseof.com/tag/read-write-google-sheets-python/


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            for i in range(4):
                print(f"{row[i]}", end="\t")
            print()

        # Updating Cells test:
        sheet.update_acell("E1", 45)
        sheet.update_cell(2,4, "hello")
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()