
def menu_principal():
    print("""
    ████████╗██████╗ ██╗   ██╗ ██████╗██╗  ██╗ ██████╗ ██████╗ ███╗   ██╗███╗   ██╗███████╗ ██████╗████████╗
    ╚══██╔══╝██╔══██╗██║   ██║██╔════╝██║ ██╔╝██╔════╝██╔═══██╗████╗  ██║████╗  ██║██╔════╝██╔════╝╚══██╔══╝
       ██║   ██████╔╝██║   ██║██║     █████╔╝ ██║     ██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██║        ██║   
       ██║   ██╔══██╗██║   ██║██║     ██╔═██╗ ██║     ██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║        ██║   
       ██║   ██║  ██║╚██████╔╝╚██████╗██║  ██╗╚██████╗╚██████╔╝██║ ╚████║██║ ╚████║███████╗╚██████╗   ██║   
       ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═╝   """)

    print('bem vindo ao TrunckConnect')
    print('1 - login Empresa')
    print('2 - login Parceiro')
    print('3 - cadstro')
    ini_servico = int(input('escolha uma das opções citadas'))

    def login_empresa():
        print('insira sua informações: ')
        nome_login = input('login: ')
        senha_login = input('senha: ')
        



    try:
        if ini_servico == 1:
            login_empresa()
        
    except:
        print('Opção inválida')
        input('precione qualquer tecla para voltar')
        menu_principal()