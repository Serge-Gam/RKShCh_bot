import pandas as pd
import utility
from storage import dict_links, dict_users

rus_months = ["Январь", "Февраль", "Март", "Апрель","Май","Июнь", "Июль", "Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
rus_days = ["Пн.","Вт.", "Ср.","Чт.","Пт.","Сб.","Вс."]

def get_rasp_for_user(user_id):
    name = dict_users[user_id]['name']

    print('Отправлено для ' + str(name)) #контроль
    month = dict_users[user_id]['month']
    link = dict_links[month]
    key = utility.get_key(link)
    print(key, name, month, link, sep=' ')


    df = pd.read_csv('https://docs.google.com/spreadsheets/d/' +
                       key +
                       '/export?gid=0&format=csv',
                       header = 1, index_col=0,
                      )
    Pd_series=df.loc[str(name)]  #это уже series

    #преобразуем данные для бота в читаемый вид
    message_rasp = ''
    # вытащим месяц из даты указанной в датафрэйме
    rus_month = rus_months[int(Pd_series.index[0][3:5])-1]
    message_rasp += (str(name)+" вот твое расписание на " +'*'+ rus_month +'*' )
    message_rasp += ('\n============')

    # в этой переменной храним индекс который указывает на день недели, для того чтобы отчертить линией конец недели
    pred = 0

    #смотрим на дни недели
    Days = range(Pd_series.shape[0])
    for day in Days:
        Weekday_pd_index = utility.get_weekday_number(Pd_series.index[day])
        Day_pd = Pd_series.index[day][:2]
        Weekday_rus = rus_days[Weekday_pd_index]
        if pred == 6: # 6 - это Вск - проверяем не Вск ли сейчас случайно
            message_rasp += ('\n----------------')

        if type(Pd_series[day]) == str:
            message_rasp += ('\n' + '*' + Weekday_rus + '*' + '\t' + '/'+Day_pd + '\t' + Pd_series[day])
        else:
            message_rasp += ('\n' + '*' + Weekday_rus + '*' + '\t' + '/'+Day_pd + '\t' + '   -')
        pred = Weekday_pd_index
        #добавляем эмоджи если функция if_today возврящает True
        if utility.event_is_today(Pd_series.index[day]):
            message_rasp += dict_users[user_id]['emoji']

    return message_rasp
#print(get_rasp_for_user('3261372')


def get_rasp_for_date(user_id, day='/01'):
    month = dict_users[user_id]['month']
    link = dict_links[month]
    key = utility.get_key(link)
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/' +
                       key +
                       '/export?gid=0&format=csv',
                       header = 1, index_col=0,
                      )

    d = str(day.split('/')[1])

    m = dict_users[user_id]['month'].split('/')[0] #получаем дату в формате 01/18
    y = dict_users[user_id]['month'].split('/')[1]
    Pd_date = d +'.0'+ m +'.20'+ y
    Pd_series = df[Pd_date]
    output =''
    for i in range(Pd_series.shape[0]):
        name = Pd_series.index[i]
        if Pd_series[i] == None:
            event = '  -'
        else:
            event = Pd_series[i]

        row = '*' + str(i) +' '+ str(name )+ ':*   '+str(event)+'\n--------------------\n'
        output += row
    return output

  #Pd_series=df.loc[str(name)]  #это уже series




print(get_rasp_for_date('3261372', '/02'))