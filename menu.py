import json
import os


ARQUIVO_DADOS = "dados.json"


def limpar_terminal():
    os.system("cls")


def ler_dados():
    # Centraliza a leitura do JSON para evitar repeticao.
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_dados(dados):
    # Salva os dados formatados de volta no arquivo.
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def login_empresa():
    print("Insira suas informacoes:")
    num_login = input("Login: ")
    senha_login = input("Senha: ")

    print("\nDados recebidos com sucesso.")
    print(f"Login digitado: {num_login}")
    print(f"Senha digitada: {senha_login}")

    return num_login, senha_login


def login_parceiro():
    print("Precisamos de algumas informacoes para continuar com seu login:")

    while True:
        cpf_digitado = input("CPF: ")
        senha_digitada = input("Senha: ")

        dados = ler_dados()
        parceiros = dados["parceiros"]

        # Primeiro validamos se o CPF existe para evitar erro de chave.
        if cpf_digitado not in parceiros:
            print("CPF nao encontrado.")
            input("Pressione Enter para tentar novamente...")
            limpar_terminal()
            continue

        parceiro = parceiros[cpf_digitado]
        senha_confere = senha_digitada == parceiro["senha"]

        if senha_confere:
            print("Login correto.")
            input("Pressione Enter para voltar ao menu...")
            return True

        print("Senha incorreta.")
        input("Pressione Enter para tentar novamente...")
        limpar_terminal()


def cadastro_parceiro():
    while True:
        print("Preencha os campos a seguir corretamente:")
        cpf = input("CPF (somente numeros): ")
        cnh = input("Numero da CNH: ")
        nome = input("Nome: ").upper().replace(" ", "_")
        data = input("Data de nascimento: ").replace("/", "").replace("-", "").replace(" ", "")
        senha = input("Senha: ")

        dados = ler_dados()
        parceiros = dados["parceiros"]

        # CPF e chave unica; se existir, nao podemos cadastrar novamente.
        if cpf in parceiros:
            print("CPF ja cadastrado.")
            print("Refaca o cadastro ou faca o login.")
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


def escolha_cadastro():
    while True:
        print("Precisamos de algumas informacoes para realizar o seu cadastro")
        print("1. Empresa")
        print("2. Parceiro")
        print("3. Voltar ao menu principal")

        try:
            escolha_cadastro = int(input("Escolha qual seu tipo de cadastro: "))
        except ValueError:
            limpar_terminal()
            print("Opcao invalida.")
            input("Pressione Enter para continuar...")
            continue

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
            print("Opcao invalida.")
            input("Pressione Enter para continuar...")
            continue

        if ini_servico == 1:
            limpar_terminal()
            login_empresa()
            input("Pressione Enter para voltar ao menu...")
            continue

        if ini_servico == 2:
            limpar_terminal()
            login_parceiro()
            continue

        if ini_servico == 3:
            limpar_terminal()
            escolha_cadastro()
            continue

        if ini_servico == 4:
            limpar_terminal()
            print("Saindo do sistema...")
            return

        print("Opcao invalida.")
        input("Pressione Enter para continuar...")


def main():
    menu_principal()


if __name__ == "__main__":
    main()
