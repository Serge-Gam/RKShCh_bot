import storage

def authentication_passed(user_id):
    if user_id in storage.dict_users:
        return True
    else:
        return False