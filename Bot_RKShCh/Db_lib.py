
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('botrkshch-342645f98a77.json', scope)
client = gspread.authorize(creds)

# проверяем со со второй строки чтобы не проверять строку заголовков
# вызываем эти функции после проверки ID

def download_dict_users():

    sheet = client.open("DB_Table_Users").sheet1
    dict_users = {}
    for row_number in range(2, 100):
        current_row = sheet.row_values(row_number)
        if current_row[0].isdigit():
            if len(current_row[1]) > 2:# проверяем есть ли чтото в поле имя
                telegram_id = current_row[1]
                user_name = current_row[2]
                month = current_row[3]
                emoji = current_row[4]
                admin = current_row[5]
                team = current_row[6]
                dict_users[telegram_id] = {'user_name': user_name, 'month': month, 'emoji': emoji, 'admin': admin,
                                          'team': team}
        else:
            break
    return dict_users
print(download_dict_users())

def download_video_set():
    sheet = client.open("DB_Table_Users").sheet1
    cells = sheet.findall('video')
    video_set = set()
    for cell in cells:
        video_set.add(str(sheet.row_values(cell.row)[2]))
    return video_set

def download_sound_set():
    sheet = client.open("DB_Table_Users").sheet1
    cells = sheet.findall('sound')
    sound_set = set()
    for cell in cells:
        sound_set.add(str(sheet.row_values(cell.row)[2]))
    return sound_set

def download_dict_months_links():
    sheet = client.open("DB_Table_Months").sheet1
    dict_months_links = {}
    for row_number in range(2, 100):
        current_row = sheet.row_values(row_number)
        if current_row[0].isdigit():
            month_code = current_row[1]
            name = current_row[2]
            link = current_row[3]
            dict_months_links[month_code] = {'name':name,'link':link}
        else:
            break
    return dict_months_links
#print(download_dict_months_links())

def upload_month_code(user_id, month_code):
    sheet = client.open("DB_Table_Users").sheet1
    cell = sheet.find(str(user_id))
    sheet.update_cell(cell.row, 4, str(month_code))
#upload_month_code(146250723, '05/2018')

def upload_emoji(user_id, emoji):
    sheet = client.open("DB_Table_Users").sheet1
    cell = sheet.find(str(user_id))
    sheet.update_cell(cell.row, 5, emoji)






