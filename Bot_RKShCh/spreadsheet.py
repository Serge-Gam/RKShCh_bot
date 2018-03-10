import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('botrkshch-342645f98a77.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("DB_Table_Months").sheet1
dict_test = {}
print(sheet.row_count)
for row_number in range(1,100):
    current_row = sheet.row_values(row_number)
    month_code = current_row[0]
    link = current_row[2]
    dict_test[month_code] = link

print(dict_test)

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()

print(list_of_hashes)