from funções import limpar_terminal, ler_dados, salvar_dados

import json
import os


def login_empresa():
    while True:
        print('Login da empresa... ')
        cnpj_digitado = input('insira o CNPJ: ').replace('-','').replace("/", "").replace("-", "").replace(" ", "")

        dados = ler_dados()
        empresas = dados['empresas']
        if cnpj_digitado not in empresas:
            limpar_terminal()
            print('empresa não encontrada.')
            print('''
Caso deseje sair pressione X, 
caso queira continuar pressione qualquer tecla.
''')
            resposta = input('O que deseja: ').lower()
            limpar_terminal()
            if resposta == 'x':
                return
            continue     
        
        senha_digitado = input('insira o senha: ')

        empresa = empresas[cnpj_digitado]
        senha_confirm = senha_digitado == empresa['senha']

        if senha_confirm:
            print('senha confirmada.')
            input("Pressione Enter para voltar ao menu...")
            return cnpj_digitado
        else:
            print('senha incorreta.')
            input('precione qualquer tecla para tentar novamente... ')
            continue
    return cnpj_digitado

def login_parceiro():
    print("Precisamos de algumas informacoes para continuar com seu login:")

    while True:
        cpf_digitado = input("CPF: ")

        dados = ler_dados()
        parceiros = dados["parceiros"]

        # Primeiro validamos se o CPF existe para evitar erro de chave.
        if cpf_digitado not in parceiros:
            limpar_terminal()
            print("CPF nao encontrado.")
            print('''
Caso deseje sair pressione X, 
caso queira continuar pressione qualquer tecla.
    ''')
            resposta = input('O que deseja: ').lower()
            if resposta == 'x':
                return
            continue

        senha_digitada = input("Senha: ")

        parceiro = parceiros[cpf_digitado]
        senha_confere = senha_digitada == parceiro["senha"]

        if senha_confere:
            print("Login correto.")
            input("Pressione Enter para voltar ao menu...")
            return cpf_digitado

        print("Senha incorreta.")
        input("Pressione Enter para tentar novamente...")
        limpar_terminal()
    return cpf_digitado

def cadastro_parceiro():
    while True:
        print("Preencha os campos a seguir corretamente:")
        cpf = input("CPF (somente numeros): ")
        cnh = input("Numero da CNH: ")
        nome = input("Nome: ").title()
        data = input("Data de nascimento: ").replace("/", "").replace("-", "").replace(" ", "")
        senha = input("Senha: ")

        dados = ler_dados()
        parceiros = dados["parceiros"]

        if cpf == '':
            print("impossivel cadastrar esse cpf")
            print("Refaça o cadastro ou faça o login.")
            input("Pressione Enter para continuar...")
            limpar_terminal()
            continue

        if cnh == '':
            print("impossivel cadastrar esse cnh")
            print("Refaça o cadastro ou faça o login.")
            input("Pressione Enter para continuar...")
            limpar_terminal()
            continue

        if nome == '':
            print("impossivel cadastrar esse nome")
            print("Refaça o cadastro ou faça o login.")
            input("Pressione Enter para continuar...")
            limpar_terminal()
            continue

        if data == '':
            print("impossivel cadastrar esse data")
            print("Refaça o cadastro ou faça o login.")
            input("Pressione Enter para continuar...")
            limpar_terminal()
            continue

        if senha == '':
            print("impossivel cadastrar esse senha")
            print("Refaça o cadastro ou faça o login.")
            input("Pressione Enter para continuar...")
            limpar_terminal()
            continue

        # CPF e chave unica; se existir, nao podemos cadastrar novamente.
        if cpf in parceiros:
            print("CPF ja cadastrado.")
            print("Refaça o cadastro ou faça o login.")
            input("Pressione Enter para continuar...")
            limpar_terminal()
            continue

        # CNH fica dentro de cada parceiro, entao percorremos os valores.
        cnh_existe = any(parceiro["cnh"] == cnh for parceiro in parceiros.values())

        if cnh_existe:
            print("CNH ja cadastrada.")
            print("Reinicie o processo de cadastro.")
            input("Pressione Enter para continuar...")
            limpar_terminal()
            continue

        print("Confirme seus dados...\n")
        print(f"CPF: {cpf}")
        print(f"CNH: {cnh}")
        print(f"Nome: {nome}")
        print(f"Data: {data}")
        print(f"Senha: {senha}")

        redef = input(
            'Caso seu cadastro esteja correto pressione "S". '
            'Caso deseje reiniciar o processo pressione "N": '
        ).upper()

        if redef == "S":
            dados["parceiros"][cpf] = {
                "nome": nome,
                "data": data,
                "senha": senha,
                "cnh": cnh,
            }
            salvar_dados(dados)
            print("Parceiro cadastrado com sucesso.")
            input("Pressione Enter para voltar ao menu...")
            return

        if redef == "N":
            limpar_terminal()
            continue

        print("Opcao invalida.")
        input("Pressione Enter para continuar...")
        limpar_terminal()


def cadastro_empresa():
    while True:
        print("Preencha os campos a seguir corretamente:")
        cnpj = input("CNPJ (somente numeros): ")
        nome = input("Nome: ")
        senha = input("Senha: ")

        dados = ler_dados()
        empresas = dados["empresas"]

        if cnpj in empresas:
            print("CNPJ ja cadastrado.")
            input("Pressione Enter para continuar...")
            limpar_terminal()
            continue

        dados["empresas"][cnpj] = {
            "nome": nome,
            "senha": senha,
            "cnpj": cnpj,
        }
        salvar_dados(dados)

        print("Empresa cadastrada com sucesso.")
        input("Pressione Enter para voltar ao menu...")
        return