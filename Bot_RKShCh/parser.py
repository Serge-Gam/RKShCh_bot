import pandas as pd
import parser_utility
from storage import dict_months_links, dict_users, video_set, sound_set
from constants import rus_days, rus_months

def make_rasp_for_user(user_id):
    name = dict_users[user_id]['user_name']
    df = parser_utility.get_dataframe(user_id)
    Pd_series=df.loc[str(name)]  #это уже series

    output = ''
    # вытащим месяц из даты указанной в датафрэйме
    rus_month = rus_months[int(Pd_series.index[0][3:5])-1]
    output += (str(name)+" вот твое расписание на " +'*'+ rus_month +'*' )
    output += ('\n============')

    # в этой переменной храним индекс который указывает на день недели, для того чтобы отчертить линией конец недели
    pred = 0

    #смотрим на дни недели
    Days = range(Pd_series.shape[0])
    for day in Days:
        Weekday_pd_index = parser_utility.get_weekday_number(Pd_series.index[day])
        Day_pd = Pd_series.index[day][:2]
        Weekday_rus = rus_days[Weekday_pd_index]
        if pred == 6: # 6 - это Вск - проверяем не Вск ли сейчас случайно
            output += ('\n----------------')

        if type(Pd_series[day]) == str:
            output += ('\n' + '*' + Weekday_rus + '*' + '\t' + '/'+Day_pd + '\t' + Pd_series[day])
        else:
            output += ('\n' + '*' + Weekday_rus + '*' + '\t' + '/'+Day_pd + '\t' + '   -')
        pred = Weekday_pd_index
        #добавляем эмоджи если функция if_today возврящает True
        if parser_utility.event_is_today(Pd_series.index[day]):
            output += dict_users[user_id]['emoji']

    return output
#print(get_rasp_for_user('3261372')

def make_rasp_for_date(user_id, day='/01'):
    df = parser_utility.get_dataframe (user_id)
    d = str(day.split('/')[1])
    m = dict_users[user_id]['month'].split('/')[0]  #получаем дату в формате 01/18
    y = dict_users[user_id]['month'].split('/')[1]
    Pd_date = '.'.join([d,m,y])
    df_new = df[[Pd_date]]
    df_new = df_new.sort_values([Pd_date])
    PD_series = df_new[Pd_date]
    week_day = rus_days[parser_utility.get_weekday_number(Pd_date)]
    month_name_rus = rus_months[int(m)]
    #проспрягаем наш месяц в родительный падеж
    if month_name_rus == ('Март' or 'Август'):
        month_name_rus = ''.join([month_name_rus[:-1],'а'])
    else: month_name_rus = ''.join([month_name_rus[:-1],'я'])


    output = ' '.join(['*\n=======================\n',d,month_name_rus,week_day,Pd_date,'\n=======================\n*'])

    for i in range(PD_series.shape[0] - 1):
        name = PD_series.index[i]
        if dict_users[user_id]['team'] == 'video':
            some_set, emoji = video_set, '📹'
        else:
            some_set, emoji = sound_set, '🎙'

        if name in some_set:
            name = emoji + name

        if type(PD_series[i]) == str:
            event = PD_series[i]
        else:
            event = '🏡'

        if i%2 == 0:
            row = '\n*'+ (str(event)).title() + ':   ' + str(name ) + '*\n'
        else:
            row = '\n'+ (str(event)).title()+ ':   ' + str(name)  + '\n'
        output += row
    last_row_index = PD_series.shape[0]-1
    kontramarki_title = PD_series.index[last_row_index]
    if PD_series[last_row_index] == str():
        kontramarki_info = PD_series[last_row_index]
    else:
        kontramarki_info = '-'
    output += ' '.join(['\n📝',str(kontramarki_title),':   ',str(kontramarki_info)])
    output += ' '.join(['*\n=======================\n',d,month_name_rus,week_day,Pd_date,'\n=======================\n*'])
    return output
#print(get_rasp_for_date(3261372, '/02'))
