import json

import os

def limpar_terminal():
    os.system('cls')

def login_empresa():
    print('Insira suas informações:')
    num_login = input('Login: ')
    senha_login = input('Senha: ')

    print('\nDados recebidos com sucesso.')
    print(f'Login digitado: {num_login}')
    print(f'Senha digitada: {senha_login}')

    return num_login, senha_login

def login_parceiro():
    pass

def cadastro_parceiro():
    print('preencha os campos a seguir corretamente:')
    cpf = (input('CPF (somente numeros): '))
    cnh = input('numero da CNH: ')
    nome = input('Nome: ')
    data = input('data de nascimento: ')
    senha = input('senha: ')

    with open("dados.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    dados['parceiros'][cpf] = {
        'nome': nome,
        'data': data,
        'senha': senha,
        'cnh': cnh
    }

    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def cadastro_empresa():
    print('preencha os campos a seguir corretamente:')
    cnpj = (input('CNPJ (somente numeros): '))
    nome = input('Nome: ')
    senha = input('senha: ')

    with open("dados.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    dados['empresas'][cnpj] = {
        'nome': nome,
        'senha': senha,
        'cnpj': cnpj
    }

    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def escolha_cadastro():
    while True:

        print('preisamos de algumas informações para realizar o seu cadastro')
        print('1. Empresa')
        print('2. pareiro')
        print('3. voltar ao menu principal')
        try:
            esco_cadatro = int(input('escolha qual seu tipo de cadastro... '))
        except ValueError:
            limpar_terminal()
            print('opção invalida.')
            input('Pressione Enter para continuar...')
            continue   
        if esco_cadatro == 1:
            limpar_terminal()
            cadastro_empresa()
        elif esco_cadatro == 2:
            limpar_terminal()
            cadastro_parceiro()
        elif esco_cadatro == 3:
            return

def menu_principal():
    while True:
        print("""
    ████████╗██████╗ ██╗   ██╗ ██████╗██╗  ██╗ ██████╗ ██████╗ ███╗   ██╗███╗   ██╗███████╗ ██████╗████████╗
    ╚══██╔══╝██╔══██╗██║   ██║██╔════╝██║ ██╔╝██╔════╝██╔═══██╗████╗  ██║████╗  ██║██╔════╝██╔════╝╚══██╔══╝
       ██║   ██████╔╝██║   ██║██║     █████╔╝ ██║     ██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██║        ██║
       ██║   ██╔══██╗██║   ██║██║     ██╔═██╗ ██║     ██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║        ██║
       ██║   ██║  ██║╚██████╔╝╚██████╗██║  ██╗╚██████╗╚██████╔╝██║ ╚████║██║ ╚████║███████╗╚██████╗   ██║
       ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═╝
        """)

        print('Bem-vindo ao TrunckConnect')
        print('1. Login Empresa')
        print('2. Login Parceiro')
        print('3. Cadastro')
        print('4. Sair')

        try:
            ini_servico = int(input('Escolha uma das opções citadas: '))
        except ValueError:
            limpar_terminal()
            print('Opção inválida.')
            input('Pressione Enter para continuar...')
            continue

        if ini_servico == 1:
            limpar_terminal()
            login_empresa()
            input('Pressione Enter para voltar ao menu...')

        elif ini_servico == 2:
            limpar_terminal()
            print('Login de parceiro ainda não foi implementado.')
            input('Pressione Enter para voltar ao menu...')

        elif ini_servico == 3:
            limpar_terminal()
            escolha_cadastro()

        elif ini_servico == 4:
            limpar_terminal()
            print('Saindo do sistema...')
            limpar_terminal()
            break

        else:
            limpar_terminal()
            print('Opção inválida.')
            input('Pressione Enter para continuar...')