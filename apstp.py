#APS
#Grupo: Felipe Lichtenecker, João Pedro Hudson e Lucas Tosti
import re

print('Registre seu Login e Senha: ')
login = str(input('usuario: '))
senha = str(input('senha: '))

passworld = senha
flag = 0
while True:
    if (len(passworld) <8):
        flag =-1
        break
    elif not re.search('[a-z]', passworld):
        flag =-1
        break
    elif not re.search('[A-Z]', passworld):
        flag =-1
        break
    elif not re.search('[0-9]', passworld):
        flag =-1
        break
    elif not re.search('[_@$]', passworld):
        flag =-1
        break
    elif re.search('\s', passworld):
        flag =-1
        break
    else:
        flag = 0
        print('Senha Valida')
        arquivo = open('Login.txt','w')
        arquivo.write(f'user: {login}\n senha: {passworld}')
        arquivo.close()
        break
while flag == -1:
    print('Senha Invalida')
    print('Registre seu Login e Senha: ')
    login = str(input('usuario: '))
    senha = str(input('senha: '))

    passworld = senha
    flag = 0
    while True:
        if (len(passworld) <8):
            flag =-1
            break
        elif not re.search('[a-z]', passworld):
            flag =-1
            break
        elif not re.search('[A-Z]', passworld):
            flag =-1
            break
        elif not re.search('[0-9]', passworld):
            flag =-1
            break
        elif not re.search('[_@$]', passworld):
            flag =-1
            break
        elif re.search('\s', passworld):
            flag =-1
            break
        else:
            flag = 0
            print('Senha Valida')
            arquivo = open('Login.txt','w')
            arquivo.write(f'user: {login}\n senha: {passworld}')
            arquivo.close()
            break
