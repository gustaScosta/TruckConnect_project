print("Bem-vindo ao sistema de cadastro de fretes!")
print(f"\nEscolha uma opção: ")

fretes = []

while True:

    print("1 - Cadastrar novo frete")
    print("2 - Listar fretes cadastrados")
    print("3 - Alterar status de um frete")
    print("4 - Sair")

    esc = str(input("Digite o número da opção desejada: "))

    if esc == "4":

        print("Saindo do sistema. Até mais!")
        break

    if esc == "1":

        def cadastrar_frete(origem, destino, peso, valor, status):

            origem = input("Digite a origem do frete: ")
            destino = input("Digite o destino do frete: ")
            peso = float(input("Digite o peso do frete (em kg): "))
            valor = float(input("Digite o valor do frete: "))
            status = input("Digite o status do frete (pendente, em trânsito, entregue): ")
            
            cadastrar_frete(origem, destino, peso, valor, status)

            global fretes 

            novo_frete = { 

                "origem": origem,
                "destino": destino,
                "peso": peso,
                "valor": valor,
                "status": status

        }

            fretes.append(novo_frete)
            
            print("Frete cadastrado com sucesso!")


    elif esc == "2":

        if len(fretes) == 0:
            print("Nenhum frete cadastrado.")

        else:
            print("Fretes cadastrados:")

            for i, frete in enumerate(fretes):
                print(f"Frete {i + 1}")
            
            esc2 = str(input("Digite o número do frete para ver detalhes ou '0' para voltar ao menu: "))

            if esc2 == "0":
                continue

            else:
                
                if esc2 > 0 and esc2 <= len(fretes):
                    frete = fretes[esc2 - 1]

                    print(f"\nDetalhes do frete: ")
                    print(f"Origem: {frete['origem']}")
                    print(f"Destino: {frete['destino']}")
                    print(f"Peso: {frete['peso']} kg")
                    print(f"Valor: R$ {frete['valor']}")
                    print(f"Status: {frete['status']}")

                else:
                    print("Número de frete inválido. Voltando ao menu.")
                continue

    elif esc == "3":

        if len(fretes) == 0:
            print("Nenhum frete cadastrado.")

        else:
            print("Fretes cadastrados:")

            for i, frete in enumerate(fretes):
                print(f"Frete {i + 1}")
            
            esc3 = str(input("Digite o número do frete para alterar o status ou '0' para voltar ao menu: "))

            if esc3 == "0":
                continue

            else:
                
                if esc3 > 0 and esc3 <= len(fretes):
                    frete = fretes[esc3 - 1]

                    novo_status = input("Digite o novo status do frete (pendente, em trânsito, entregue): ")
                    frete['status'] = novo_status

                    print("Status do frete atualizado com sucesso!")

                else:
                    print("Número de frete inválido. Voltando ao menu.")
        
        