from funções import limpar_terminal, ler_dados, saida
from usuarios import cadastro_empresa, cadastro_parceiro, login_empresa, login_parceiro
from fretes import postar_carga

import json
import os
        
def escolha_cadastro():
    while True:
        print("Precisamos de algumas informacoes para realizar o seu cadastro")
        print("1. Empresa")
        print("2. Parceiro")
        print("3. Voltar ao menu principal")

        try:
            escolha_cadastro = int(input("Escolha qual seu tipo de cadastro: "))
        except ValueError:
            if saida():
                continue
            return

        if escolha_cadastro == 1:
            limpar_terminal()
            cadastro_empresa()
            return

        if escolha_cadastro == 2:
            limpar_terminal()
            cadastro_parceiro()
            return

        if escolha_cadastro == 3:
            limpar_terminal()
            return

        limpar_terminal()
        print("Opcao invalida.")
        input("Pressione Enter para continuar...")


def menu_principal():
    while True:
        limpar_terminal()
        print(
            """
    ████████╗██████╗ ██╗   ██╗ ██████╗██╗  ██╗ ██████╗ ██████╗ ███╗   ██╗███╗   ██╗███████╗ ██████╗████████╗
    ╚══██╔══╝██╔══██╗██║   ██║██╔════╝██║ ██╔╝██╔════╝██╔═══██╗████╗  ██║████╗  ██║██╔════╝██╔════╝╚══██╔══╝
       ██║   ██████╔╝██║   ██║██║     █████╔╝ ██║     ██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██║        ██║
       ██║   ██╔══██╗██║   ██║██║     ██╔═██╗ ██║     ██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║        ██║
       ██║   ██║  ██║╚██████╔╝╚██████╗██║  ██╗╚██████╗╚██████╔╝██║ ╚████║██║ ╚████║███████╗╚██████╗   ██║
       ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═╝
        """
        )

        print("Bem-vindo ao TrunckConnect")
        print("1. Login Empresa")
        print("2. Login Parceiro")
        print("3. Cadastro")
        print("4. Sair")

        try:
            ini_servico = int(input("Escolha uma das opcoes citadas: "))
        except ValueError:
            if saida():
                return
            continue
                
        if ini_servico == 1:
            limpar_terminal()
            cnpj = login_empresa()
            if cnpj:
                menu_empresa(cnpj)
            continue

        if ini_servico == 2:
            limpar_terminal()
            cpf = login_parceiro()
            if cpf:
                menu_parceiro(cpf)
            continue

        if ini_servico == 3:
            limpar_terminal()
            escolha_cadastro()
            continue

        if ini_servico == 4:
            limpar_terminal()
            return

def menu_empresa(cnpj):
    while True:
        dados = ler_dados()
        dados_em = dados['empresas'][cnpj]
        nome_em = dados_em['nome']

        limpar_terminal()
        print('Bem vindo aom menu de sua empresa')
        print(f'dados da empresa:{nome_em}')
        print('1. cadastrar nova carga')
        print('2. ver minhas cargas')
        print('3. sair')

        try:
            opcao = int(input('escolha a opção: '))
        except ValueError:
            if saida():
                return
            continue
        
        if opcao == 1:
            limpar_terminal()
            postar_carga(cnpj)
            continue
        elif opcao == 2:
            limpar_terminal()
            print('em construção')
            input('pressione qualquer tecla para continuar... ')
            continue
        elif opcao == 3:
            limpar_terminal()
            print('saindo... ')
            return


def menu_parceiro(cpf):
    while True:

        dados = ler_dados()
        dados_par = dados['parceiros'][cpf]
        nome_par = dados_par['nome']
    
        limpar_terminal()
        print(f'Bem vindo ao seu menu de parceiro {nome_par}')
        print('1. ver cargas disponiveis')
        print('2. ver minhas propostas')
        print('3. sair')

        try:
            opcao = int(input('escolha a opção: '))
        except ValueError:
            if saida():
                return
            continue
            
        if opcao == 1:
            limpar_terminal()
            print('em construção')
            input('pressione qualquer tecla para continuar... ')
            continue
        elif opcao == 2:
            limpar_terminal()
            print('em construção')
            input('pressione qualquer tecla para continuar... ')
            continue
        elif opcao == 3:
            limpar_terminal()
            print('saindo... ')
            return


def main():
    menu_principal()

if __name__ == "__main__":
    main()