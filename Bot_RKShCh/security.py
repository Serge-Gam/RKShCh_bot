import storage

def authentication_passed(user_id):
    if str(user_id) in storage.dict_users:
        return True
    else:
        return False

def user_is_admin(user_id):
    user_id = str(user_id)
    if storage.dict_users[user_id]['admin'] == 'TRUE':
        return True
    else:
        return False