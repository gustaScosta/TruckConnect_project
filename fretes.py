import os


def limpar_tela():
    os.system("cls")


def cadastro():

    nome = input("Digite o nome do frete: ")
    origem = input("Digite a origem do frete: ")
    destino = input("Digite o destino do frete: ")
    peso = float(input("Digite o peso do frete (em kg): "))
    valor = float(input("Digite o valor do frete: "))
    status = input("Digite o status do frete (pendente, em trânsito, entregue): ")           

    return nome, origem, destino, peso, valor, status

def alterar_frete(frete):

    print(f"\nInformações atuais do frete: ")    
    print(f"\nOrigem: {frete['origem']}")
    print(f"Destino: {frete['destino']}")
    print(f"Peso: {frete['peso']} kg")
    print(f"Valor: R$ {frete['valor']}")
    print(f"Status: {frete['status']}")

fretes = []


print("Bem-vindo ao sistema de cadastro de fretes!")
print(f"\nEscolha uma opção: ")

while True:

    print(f"\n1 - Cadastrar novo frete")

    limpar_tela()

    print("1 - Cadastrar novo frete")
    print("2 - Listar fretes cadastrados")
    print("3 - Alterar informação de um frete")
    print("4 - Sair")

    esc = (input("Digite o número da opção desejada: "))

    if esc == "4":

        print("Saindo do sistema. Até mais!")
        break

    try:

        if esc == "1":

            limpar_tela()

            nome, origem, destino, peso, valor, status = cadastro()

            limpar_tela()

            print(f"\nConfirme os dados do frete")
            print(f"\nNome do frete: {nome}")
            print(f"Origem: {origem}")
            print(f"Destino: {destino}")
            print(f"Peso: {peso} kg")
            print(f"Valor: R$ {valor}")
            print(f"Status: {status}")

            conf = input(f"\nDigite 'S' para confirmar ou 'N' para cancelar: ").upper()
            
            if conf == "S":
                
                novo_frete = { 

                    "nome": nome,
                    "origem": origem,
                    "destino": destino,
                    "peso": peso,
                    "valor": valor,
                    "status": status

                }

                nome = novo_frete

                fretes.append(novo_frete)

                print("Frete cadastrado com sucesso!")

            if conf == "N":

                limpar_tela()

                print("Cadastro cancelado. Voltando ao menu.")
                continue

        elif esc == "2":

            limpar_tela()

            if len(fretes) == 0:
                print("Nenhum frete cadastrado.")

            else:
                print("Fretes cadastrados:")

                for i, frete in enumerate(fretes):
                    print(f"\n {i + 1} - {frete['nome']} \n")
                
                esc2 = int(input(f"\nDigite o número do frete para ver detalhes ou '0' para voltar ao menu: "))

                if esc2 == 0:
                    continue

                else:
                    
                    if esc2 > 0 and esc2 <= len(fretes):
                        frete = fretes[esc2 - 1]

                        print(f"\nDetalhes do frete: ")
                        print(f"\nNome do frete: {frete['nome']}")
                        print(f"Origem: {frete['origem']}")
                        print(f"Destino: {frete['destino']}")
                        print(f"Peso: {frete['peso']} kg")
                        print(f"Valor: R$ {frete['valor']}")
                        print(f"Status: {frete['status']}")

                    else:
                        print("Número de frete inválido. Voltando ao menu.")
                    continue

        elif esc == "3":

            limpar_tela()

            if len(fretes) == 0:
                print("Nenhum frete cadastrado.")

            else:
                print("Fretes cadastrados:")

                for i, frete in enumerate(fretes):
                    print(f"Frete {i + 1}")
                
                esc3 = int(input("Digite o número do frete para alterar a informação ou '0' para voltar ao menu: "))

                if esc3 == 0:
                    continue
                    
                else:
                    
                    if esc3 > 0 and esc3 <= len(fretes):
                        frete = fretes[esc3 - 1]
                        
                        alterar_frete()

                        alt = input(f"\n Qual informação deseja alterar? (origem, destino, peso, valor, status): ").lower()

                        if alt == "origem":

                            novo_origem = input("Digite a nova origem do frete: ")
                            frete['origem'] = novo_origem
                            
                        elif alt == "destino":

                            novo_destino = input("Digite o novo destino do frete: ")
                            frete['destino'] = novo_destino

                        elif alt == "peso":
                            
                            novo_peso = float(input("Digite o novo peso do frete (em kg): "))
                            frete['peso'] = novo_peso

                        elif alt == "valor":

                            novo_valor = float(input("Digite o novo valor do frete: "))
                            frete['valor'] = novo_valor

                        elif alt == "status":

                            novo_status = input("Digite o novo status do frete (pendente, em trânsito, entregue): ")
                            frete['status'] = novo_status

                        

                        print("Informações do frete atualizadas com sucesso!")

                    else:
                        print("Número de frete inválido. Voltando ao menu.")  

    finally:
        print("Obrigado por usar o sistema de cadastro de fretes!") 