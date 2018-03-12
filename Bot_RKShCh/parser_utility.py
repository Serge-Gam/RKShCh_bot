from datetime import date
from storage import dict_months_links, dict_users, video_set, sound_set
import pandas as pd

def get_weekday_number(s_smth): #принимаем на вход пандовский series
    dmy = s_smth.split('.')
    d,m,y = int(dmy[0]), int(dmy[1]), int(dmy[2])
    return date(y,m,d).weekday()

#по дате проверяем не сегодня ли это событие
def event_is_today(s_smth):
    dmy = s_smth.split('.')
    d, m, y = int(dmy[0]), int(dmy[1]), int(dmy[2])
    if date(y, m, d) == date.today():
        return True
    else:
        return False

#загружаем файл таблицу как csv и возвращаем  dataframe
def get_dataframe(user_id):
    month_code = dict_users[user_id]['month']
    link = dict_months_links[month_code]['link']
    key = link.split('/')[5]
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/' +
                       key +
                       '/export?gid=0&format=csv',
                       header = 1, index_col=0,
                      )
    return df