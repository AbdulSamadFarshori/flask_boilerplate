from application.core.db.models.User import User

def check_credential(username, hash_password):
    obj = User.query.filter(username=username).first()
    if obj.password == hash_password:
        return True
    else:
        return False