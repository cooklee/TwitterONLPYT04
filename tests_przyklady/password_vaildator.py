def _check_length(password):
    return len(password) >= 7

def _check_big_letter(password):
    return any(x for x in password if x.isupper())

def _check_lower_letter(password):
    return any(x for x in password if x.islower())

def _check_special_sign(password):
    sings = """!@#$%^&*()_+=-{}[]|"';:<,>.?/"""
    return any(x for x in password if x in sings)

def check_password(password):
    return check_length(password) and \
           check_big_letter(password) and \
           check_lower_letter(password) and \
           check_special_sign(password)


check_password('alamakota')