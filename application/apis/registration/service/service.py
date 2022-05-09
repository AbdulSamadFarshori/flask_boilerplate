from application.core.db_logic.registration import create_user

def user_register(username, password):
    if instance(username, str) and password:
        hash_password = hash(password)
        create_user(username, hash_password)
        return True
    return False

