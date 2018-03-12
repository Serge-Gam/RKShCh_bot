from datetime import date

def get_key(link):
    output = link.split('/')[5]
    return output

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