from module import validate_user, register_user

name = input('Digite seu nome: ')
email = input('Digite seu email: ')
senha = input('Escolha uma senha de 4 caracteres: ')



valido = validate_user(name, email, senha)
if valido == True:
    register_user(name, email, senha)
    print('Cadastrando usuario...')
else:
    print('Nome de usuario, email ou senha invalidos, tente novamente...')