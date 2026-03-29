import json

import os
def menu_interacao():
    pass
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
    
    print('precisamos de algumas informações para continuar com seu login:')
    while True:
        cpf = int(input('CPF: '))
        senha = input('Senha: ')
        with open('dados.json', 'r', encoding='utf-8') as arquivos:
            dados = json.load(arquivos)

        parceiros = dados['parceiros']
        senha = dados['parceiros']['senha']
        if cpf in parceiros:
            cpf = True
        else:
            cpf = False
        
        if senha in senha:
            senha = True
        else:
            senha = False

        if cpf and senha == True:
            print('login bem sucedido')
            menu_interacao()
        else:
            print('login ou senha invalida')
            input('pressione qualquer tecla para tentar novamente... ')



def cadastro_parceiro():
    while True:
        print('preencha os campos a seguir corretamente:')
        cpf = (input('CPF (somente numeros): '))
        cnh = input('numero da CNH: ')
        nome = input('Nome: ').upper().replace(' ','_')
        data = input('data de nascimento: ').replace('/','').replace('-','').replace(' ','')
        senha = input('senha: ')
#authenticação de cpf duplicado
        with open('dados.json', 'r', encoding='utf-8') as arquivos:
            dados = json.load(arquivos)
        
        parceiros = dados['parceiros']

        if cpf in parceiros:
            print('CPF ja cadastrado')
            print('refaça o cadastro ou faça o login')
            input('pressione enter para continuar... ')
            with open('dados.json', 'r', encoding='utf-8') as arquivos:
                json.load(arquivos)

            limpar_terminal()
            continue 


        cnh_existe = False
        for parceiro in parceiros.values():
            if parceiro['cnh'] == cnh:
                cnh_existe = True
                break
        if cnh_existe == True:
            print('cnh ja cadastrado')
            print('reinicie o processo de cadastro')
            limpar_terminal()
            continue

        print(f'confirme seu dados...\n')
        print(f'CPF: {cpf}')
        print(f'CNH: {cnh}')
        print(f'Nome: {nome}')
        print(f'Data: {data}')
        print(f'Senha: {senha}')
        
        try:
            redef = (input('caso seu cadastro esteja correto pressione "S" caso deseje reiniciar o processo pressione "N" : ')).upper()
     
        except ValueError:
            limpar_terminal()
            print('Opção inválida.')
            input('Pressione Enter para continuar...')
            continue

        if redef == 'S':

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
            return
        elif redef == 'N':
            continue
            

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
        print('2. parceiro')
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
            return
        elif esco_cadatro == 2:
            limpar_terminal()
            cadastro_parceiro()
            return
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
            login_parceiro()

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


def main():
    limpar_terminal()
    menu_principal()

if __name__ == '__main__':
    main()