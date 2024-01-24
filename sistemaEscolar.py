import random
print("---Cadastro dos alunos---")

listaNomes = []
listaIdades = []
listaEmail = []
listaRenda = []
listaBolsa100 = []
listaBolsa50 = []
listaBolsa30 = []
listaFiliacaoMae = []
listaFiliacaoPai = []
listaCpf = []
listaEscolaridade = []
listaMaternal = []
listaFundamental = []
listaMedio = []

def maternal():
    idade = int(input("Digite a idade do aluno:"))
    listaIdades.append(idade)
    if idade < 5:
        print("Adiantado")
    elif idade > 5 and idade <= 6:
        print("Certo")
    else:
        print("Atrasado")
    return (idade)

def fundamental():
    idade = int(input("Digite a idade do aluno:"))
    listaIdades.append(idade)
    fundamental = float(input("\n1- 1° Ano\n2- 2° Ano\n3- 3° Ano\n4- 4° Ano\n5- 5° Ano\n6- 6° Ano\n7- 7° Ano\n8- 8° Ano\n9- 9° Ano\n"))
    match fundamental:
        case 1:
            if idade < 6:
                print("Adiantado")
            elif idade >= 6 and idade <= 7:
                print("Certo")
            else:
                print("Atrasado")
        case 2:
            if idade < 7:
                print("Adiantado")
            elif idade >= 7 and idade <= 8:
                print("Certo")
            else:
                print("Atrasado")
        case 3:
            if idade < 8:
                print("Adiantado")
            elif idade >= 8 and idade <= 9:
                print("Certo")
            else:
                print("Atrasado")
        case 4:
            if idade < 9:
                print("Adiantado")
            elif idade >= 9 and idade <= 10:
                print("Certo")
            else:
                print("Atrasado")
        case 5:
            if idade < 10:
                print("Adiantado")
            elif idade >= 10 and idade <= 11:
                print("Certo")
            else:
                print("Atrasado")
        case 6:
            if idade < 11:
                print("Adiantado")
            elif idade >= 11 and idade <= 12:
                print("Certo")
            else:
                print("Atrasado")
        case 7:
            if idade < 12:
                print("Adiantado")
            elif idade >= 12 and idade <= 13:
                print("Certo")
            else:
                print("Atrasado")
        case 8:
            if idade < 13:
                print("Adiantado")
            elif idade >= 13 and idade <= 14:
                print("Certo")
            else:
                print("Atrasado")
        case 9:
            if idade < 14:
                print("Adiantado")
            elif idade >= 14 and idade <= 15:
                print("Certo")
            else:
                print("Atrasado")
    return (idade)

def medio():
    idade = int(input("Digite a idade do aluno:"))
    listaIdades.append(idade)
    if idade > 16:
        notaEnem = int(input("Informe a nota do Enem:"))
        if notaEnem >= 450:
            print("Passou na média")
        elif notaEnem < 450:
            print("Média baixa")
    ano = int(input("\n1- 1° Ano\n2- 2° Ano\n3- 3° Ano\n"))
    match ano:
        case 1:
            if idade < 15:
                print("Adiantado")
            elif idade >=15 and idade <= 16:
                print("Certo")
            else:
                print("Atrasado")
        case 2:
            if idade < 16:
                print("Adiantado")
            elif idade >= 16 and idade <= 17:
                    print("Certo")
            else:
                print("Atrasado")
        case 3:
            if idade < 17:
                print("Adiantado")
            elif idade >= 17 and idade <= 18:
                print("Certo")
            else:
                print("Atrasado")
    return(idade)

cadastro = input("Deseja realizar um novo cadastro? s ou n")
while cadastro != "n":
    matricula = print("matricula", random.randint(1,100))
    nome = (input("Digite o nome do aluno:"))
    sobrenome = (input("Digite o sobrenome do aluno:"))
    listaNomes.append(nome + sobrenome)
    email = input("Digite o e-mail do aluno:")
    listaEmail.append(email)
    rendaFamiliar = float(input("Informe a renda familiar:"))
    listaRenda.append(rendaFamiliar)
    if rendaFamiliar < 1.412:
        bolsa100 = ("100%")
        print("Receber uma bolsa de 100%")
        listaBolsa100.append(bolsa100)
    elif rendaFamiliar >= 1.412 and rendaFamiliar < 2.824:
        bolsa50 = ("50%")
        print("Receber uma bolsa de 50%")
        listaBolsa50.append(bolsa50)
    elif rendaFamiliar >= 2.824 and rendaFamiliar < 4.236:
        Bolsa30 = ("30%")
        print("Receber uma bolsa de 30%")
        listaBolsa30.append(Bolsa30)
    else:
        print("Aluno não se enquadra nos requisitos para receber uma bolsa.")
    filiacaoMae = (input("Digite o nome da mãe do aluno:"))
    listaFiliacaoMae.append(filiacaoMae)
    filiacaopai = (input("Digite o nome do pai do aluno:"))
    listaFiliacaoPai.append(filiacaopai)
    cpf = int(input("Digite o cpf do aluno:"))
    listaCpf.append(cpf)
    escolaridade = int(input("Informe a escolaridade do aluno: \n1- Pré-escolar / Maternal\n2- Fundamental\n3- Ensino médio\n"))
    listaEscolaridade.append(escolaridade)

    match escolaridade:
        case 1:
            maternal()
            listaMaternal.append("1")
        case 2:
            fundamental()
            listaFundamental.append("1")
        case 3:
            medio()
            listaMedio.append("1")

    cadastro = input("Deseja realizar um novo cadastro? s ou n")

acessoLista = input("Deseja acessar alguma lista? s ou n")
while acessoLista != "n":
    escolha = int(input("\n1- Nomes\n2- Idades\n3- CPF\n4- Filiação\n5- Rendas\n6- Bolsas\n7- Escolaridades\n"))
    match escolha:
        case 1:
            print(listaNomes)
        case 2:
            print(listaIdades)
        case 3:
            print(listaCpf)
        case 4:
            print(str("Lista de mães: "), listaFiliacaoMae)
            print(str("Lista de pais: "), listaFiliacaoPai)
        case 5:
            print(listaRenda)
        case 6:
            print(str("Lista de bolsas 100%: "), listaBolsa100)
            print(str("Lista de bolsas 50%: "), listaBolsa50)
            print(str("Lista de bolsas 30%: "), listaBolsa30)
        case 7:
            print(str("Lista dos maternais: "), listaMaternal)
            print(str("Lista do Ensino fundamental: "), listaFundamental)
            print(str("Lista do Ensino médio: "), listaMedio)

    acessoLista = input("Deseja acessar alguma lista? s ou n")

print("Acesso encerrado.")