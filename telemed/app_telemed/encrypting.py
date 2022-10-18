from django.contrib.auth.hashers import make_password

def encriptar_senha(senha):
    senhastr = str(senha)
    return make_password(password=senhastr, salt=None, hasher="argon2")