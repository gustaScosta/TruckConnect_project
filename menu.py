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
