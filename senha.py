nome = input('Por favor insira o seu nome: ')
senha = input('Por favor insira uma senha numerica: ')
sexo = input('Se seu sexo for masculino pressione 1, se for feminino pressione 2: ')
qtn = len(senha)

if senha.isdigit():
    senha = int(senha)

    if qtn <= 4:
        sexo = int(sexo)
        if sexo == 1:
            print(f'Sua senha: {senha} e fraca senhor {nome} por favor insisra uma senha adequada!')
        else:
            print(f'Sua senha: {senha} e fraca senhora {nome} por favor insira uma senha adequada!')
    elif qtn <= 6:
        sexo = int(sexo)
        if sexo == 1:
            print(f'Sua senha: {senha} e forte senhor {nome}!')
        else:
            print(f'Sua senha: {senha} e forte senhora {nome}!')
    else:
        sexo = int(sexo)
        if sexo == 1:
            print(f'Sua senha: {senha} e muito forte senhor {nome}!')
        else:
            print(f'Sua senha: {senha} e muito forte senhora {nome}!')
else:
    if sexo.isdigit():
        sexo = int(sexo)

        if sexo == 1:
            print(f'Senhor {nome} por favor insira uma senha numerica!')
        else:
            print(f'Senhora {nome} por favor insira uma senha numerica!')

    else:
        print('Por favor digite 1 se for do sexo masculino e 2 se for do sexo feminino!')