from application.core.db_logic.login import check_credential 

def authentication(username, password):
    make_hash = hash(password)
    data = check_credential(username, make_hash)
    return data