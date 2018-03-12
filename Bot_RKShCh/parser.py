import pandas as pd
import parser_utility
from storage import dict_months_links, dict_users, video_set, sound_set
from constants import rus_days, rus_months

def get_rasp_for_user(user_id):
    name = dict_users[user_id]['user_name']
    month_code = dict_users[user_id]['month']
    link = dict_months_links[month_code]['link']
    key = parser_utility.get_key(link)

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
        Weekday_pd_index = parser_utility.get_weekday_number(Pd_series.index[day])
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
        if parser_utility.event_is_today(Pd_series.index[day]):
            message_rasp += dict_users[user_id]['emoji']

    return message_rasp
#print(get_rasp_for_user('3261372')

def get_rasp_for_date(user_id, day='/01'):
    user_id = str(user_id)
    month_code = dict_users[user_id]['month']
    link = dict_months_links[month_code]['link']
    key = parser_utility.get_key(link)
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/' +
                       key +
                       '/export?gid=0&format=csv',
                       header = 1, index_col=0,
                      )

    d = str(day.split('/')[1])
    m = dict_users[user_id]['month'].split('/')[0]  #получаем дату в формате 01/18
    y = dict_users[user_id]['month'].split('/')[1]
    Pd_date = '.'.join([d,m,y])
    PD_new = df[[Pd_date]]
    PD_new = PD_new.sort_values([Pd_date])
    PD_series = PD_new[Pd_date]

    output ='Расписание на *'+Pd_date+'*\n=======================\n'

    for i in range(PD_series.shape[0] ):
        name = PD_series.index[i]
        if dict_users[user_id]['team'] == 'video':
            some_set, emoji = video_set, '📹'
        else:
            some_set, emoji = sound_set, '🎙'

        if name in some_set:
            name = name + emoji

        if type(PD_series[i]) == str:
            event = PD_series[i]
        else:
            event = '-'

        if i%2 == 0:
            row = '\n*🔸'+ str(name )+ ':   ' + str(event) + '*\n'
        else:
            row = '\n🔹'+str(name) + ':   ' + str(event) + '\n'
        output += row

    return output+'\nРасписание на *'+ Pd_date +'*\n=======================\n'

  #PD_series=df.loc[str(name)]  #это уже series
#print(get_rasp_for_date(3261372, '/02'))
