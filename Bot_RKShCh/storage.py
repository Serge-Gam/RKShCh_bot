import Db_lib

#загружаем данные из гугл таблицы

# print('#stage1# dict_users downloading...')
# dict_users = Db_lib.download_dict_users()
# print('dict_users:',dict_users,sep='\n')
# print('#stage1# complete')
# print('#stage2# video_set & sound_set downloading...')
# video_set = Db_lib.download_video_set()
# sound_set = Db_lib.download_sound_set()
# print('video_set:',video_set,'sound_set:',sound_set,sep='\n')
# print('#stage2# complete')
# print('#stage3# dict_months_links updating...')
# dict_months_links = Db_lib.download_dict_months_links()
# print('dict_months_links:', dict_months_links, sep='\n')
# print('#stage3# complete')
# print('Bot is ready to play')

dict_users = {'544311202': {'emoji': '👈', 'admin': 'FALSE', 'month': '04/2018', 'user_name': 'Алексей Косилов', 'team': 'sound'},'146250723': {'emoji': '😎', 'admin': 'FALSE', 'month': '04/2018', 'user_name': 'Алексей Титов', 'team': 'sound'}, '150497180': {'emoji': '👈', 'admin': 'FALSE', 'month': '04/2018', 'user_name': 'Игорь', 'team': 'video'}, '172974394': {'emoji': '👈', 'admin': 'FALSE', 'month': '04/2018', 'user_name': 'Николай', 'team': 'video'}, '3261372': {'emoji': '👈', 'admin': 'TRUE', 'month': '04/2018', 'user_name': 'Сергей Гамалий', 'team': 'video'}, '387208353': {'emoji': '👈', 'admin': 'FALSE', 'month': '04/2018', 'user_name': 'Петр Тенетко', 'team': 'video'}, '85305365': {'emoji': '👈', 'admin': 'FALSE', 'month': '04/2018', 'user_name': 'Сергей Тимошенко', 'team': 'video'}}
video_set = {'Петр Тенетко', 'Николай', 'Сергей Гамалий', 'Валентин', 'Игорь', 'Дима Вологдин', 'Сергей Тимошенко'}
sound_set = {'Антон', 'Тамара', 'Ясин', 'Денис', 'Владимир', 'Алексей Косилов', 'Светлана', 'Эдик', 'Эрик', 'Дмитрий Климкин', 'Алексей Титов', 'Даня Лутцев', 'Егор'}
dict_months_links = {'11/2018': {'name': 'Ноябрь', 'link': 'https://docs.google.com/spreadsheets/d/1PJGRPOO5mcwESGwglhXdetcgIwthiBnRtI6VpdDu8r8/edit?usp=sharing'}, '06/2018': {'name': 'Июнь', 'link': 'https://docs.google.com/spreadsheets/d/14NyUjtj2dzLuCCTrf8fpHaiqS4EV7etysTdOu3wt7As/edit#gid=0'}, '03/2018': {'name': 'Март', 'link': 'https://docs.google.com/spreadsheets/d/1GwxoMmKZSULq_-w8KtEEsbVdefHCxpFzZHD0trux0aU/edit#gid=0'}, '08/2018': {'name': 'Август', 'link': 'https://docs.google.com/spreadsheets/d/1Bg5KVOHnrlNHuTQ1v-PduP-NuSUgcHkBGyZbZTyvDIM/edit?usp=sharing'}, '04/2018': {'name': 'Апрель', 'link': 'https://docs.google.com/spreadsheets/d/1nGrQcbBjAezNbflZHf2Pcp1suIvNtiwWUDQ6KlbBsJI/edit#gid=0'}, '10/2018': {'name': 'Октябрь', 'link': 'https://docs.google.com/spreadsheets/d/1PeFVKxqsuRNo2OT-D6cHZBQmFoZvbp7WCL-bqwi1KIM/edit#gid=0'}, '12/2018': {'name': 'Декабрь', 'link': 'https://docs.google.com/spreadsheets/d/1sAQ5b6RuPM5bauM8zfE68fTAeKzxvVtqpP7nKfwv7c0/edit#gid=0'}, '09/2018': {'name': 'Сентябрь', 'link': 'https://docs.google.com/spreadsheets/d/1jzWTmfOr2t8XY0VfWQQ3krFIttigXED_etgIvhR57dg/edit?usp=sharing'}, '01/2018': {'name': 'Январь', 'link': 'https://docs.google.com/spreadsheets/d/1fdO6Hj_9ekrUAyz5r7PJ-S3qn3yCUa3EkQ1Xle9e4AA/edit#gid=0'}, '05/2018': {'name': 'Май', 'link': 'https://docs.google.com/spreadsheets/d/1QRkHR3a6aqZRFLKUdFN0HkXBHNPoXEZXhFZUz3lc870/edit?usp=sharing'}, '07/2018': {'name': 'Июль', 'link': 'https://docs.google.com/spreadsheets/d/1X7Hho2M29Aet19kR3n7WAM1BMBllp3e0hhpHW_d2RC0/edit?usp=sharing'}, '02/2018': {'name': 'Февраль', 'link': 'https://docs.google.com/spreadsheets/d/1TEDtNX9IPo03toq8W2EGAuOTxu1FzbWfC6lrvz38s2M/edit#gid=0'}}


