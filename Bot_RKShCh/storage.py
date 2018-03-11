# import Db_lib
# dict_users, dict_months_links = {}, {}
# sound_set, video_set = set(), set()
#
# def download_data():
#     global dict_users, video_set, sound_set, dict_months_links
#     print('#stage1# dict_users downloading...')
#     dict_users = Db_lib.download_dict_users()
#     print('dict_users:',dict_users,sep='\n')
#     print('#stage1# complete')
#     print('#stage2# video_set & sound_set downloading...')
#     video_set = Db_lib.download_video_set()
#     sound_set = Db_lib.download_sound_set()
#     print('video_set:',video_set,'sound_set:',sound_set,sep='\n')
#     print('#stage2# complete')
#     print('#stage3# dict_months_links updating...')
#     dict_months_links = Db_lib.download_dict_months_links()
#     print('dict_months_links:', dict_months_links, sep='\n')
#     print('#stage3# complete')
#     return print('download_data: success')

dict_users = {'150497180': {'month': '3/2018', 'admin': 'FALSE', 'emoji': '👈', 'team': 'video', 'user_name': 'Игорь'}, '146250723': {'month': '3/2018', 'admin': 'FALSE', 'emoji': '😎', 'team': 'sound', 'user_name': 'Алексей Титов'}, '3261372': {'month': '03/2018', 'admin': 'TRUE', 'emoji': '👈', 'team': 'video', 'user_name': 'Сергей Гамалий'}, '172974394': {'month': '3/2018', 'admin': 'FALSE', 'emoji': '👈', 'team': 'video', 'user_name': 'Николай'}}
video_set = {'Сергей Тимошенко', 'Валентин', 'Николай', 'Дима Вологдин', 'Сергей Гамалий', 'Игорь', 'Петр Тенетко'}
sound_set = {'Даня Лутцев', 'Эдик', 'Алексей Косилов', 'Ясин', 'Антон', 'Дмитрий Климкин', 'Тамара', 'Эрик', 'Денис', 'Владимир', 'Светлана', 'Егор', 'Алексей Титов'}
dict_months_links = {'10/2018': 'https://docs.google.com/spreadsheets/d/1PeFVKxqsuRNo2OT-D6cHZBQmFoZvbp7WCL-bqwi1KIM/edit#gid=0', '08/2018': 'https://docs.google.com/spreadsheets/d/1Bg5KVOHnrlNHuTQ1v-PduP-NuSUgcHkBGyZbZTyvDIM/edit?usp=sharing', '09/2018': 'https://docs.google.com/spreadsheets/d/1jzWTmfOr2t8XY0VfWQQ3krFIttigXED_etgIvhR57dg/edit?usp=sharing', '06/2018': 'https://docs.google.com/spreadsheets/d/14NyUjtj2dzLuCCTrf8fpHaiqS4EV7etysTdOu3wt7As/edit#gid=0', '11/2018': 'https://docs.google.com/spreadsheets/d/1PJGRPOO5mcwESGwglhXdetcgIwthiBnRtI6VpdDu8r8/edit?usp=sharing', '01/2018': '', '12/2018': 'https://docs.google.com/spreadsheets/d/1sAQ5b6RuPM5bauM8zfE68fTAeKzxvVtqpP7nKfwv7c0/edit#gid=0', '04/2018': 'https://docs.google.com/spreadsheets/d/1nGrQcbBjAezNbflZHf2Pcp1suIvNtiwWUDQ6KlbBsJI/edit#gid=0', '05/2018': 'https://docs.google.com/spreadsheets/d/1QRkHR3a6aqZRFLKUdFN0HkXBHNPoXEZXhFZUz3lc870/edit?usp=sharing', '02/2018': 'https://docs.google.com/spreadsheets/d/1TEDtNX9IPo03toq8W2EGAuOTxu1FzbWfC6lrvz38s2M/edit#gid=0', '03/2018': 'https://docs.google.com/spreadsheets/d/1GwxoMmKZSULq_-w8KtEEsbVdefHCxpFzZHD0trux0aU/edit#gid=0', '07/2018': 'https://docs.google.com/spreadsheets/d/1X7Hho2M29Aet19kR3n7WAM1BMBllp3e0hhpHW_d2RC0/edit?usp=sharing'}
