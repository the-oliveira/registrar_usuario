#Lista de dominios para teste
top_level_domains = [
    ".org",
    ".net",
    ".edu",
    ".ac",
    ".gov",
    ".com",
    ".io"
]

#Variavel para validar o nome de usuario, onde deve conter mais de 2 caracteres
#Precisa conter o tipo de dado string
def validate_name(name_data):
    if type(name_data) == str and len(name_data) > 2:
        return True
    else:
        return False

#Verifica se o email é valido, se possui @ e se está na lista de dominios.    
def validate_email(email_data):
    if '@' in email_data:
        verify_email = email_data.split('.')
        if '.'+ verify_email[-1] in top_level_domains:
            return True
        else:
            return False
    else:
        return False


def validate_password(password_data):
    if len(password_data) != 4 and type(password_data) != int:
        return False
    else:
        return True

def validate_user(name, email, password):
    if validate_name(name) == False:
        raise ValueError

    if validate_email(email) == False:
        raise ValueError

    if validate_password(password) == False:
        raise ValueError
    else:
        return True
    
def register_user(name, email, password):
    if validate_user(name, email, password) == True:
        new_user = {'name':name, 'email':email, 'password':password}
        return new_user