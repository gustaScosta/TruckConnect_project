print("Bem-vindo ao sistema de cadastro de fretes!")
print(f"\nEscolha uma opção: ")

print("1 - Cadastrar novo frete")
print("2 - Listar fretes cadastrados")
print("3 - Alterar status de um frete")
print("4 - Sair")

esc = str(input("Digite o número da opção desejada: "))

fretes = []

if esc == "1":
    def cadastrar_frete(origem, destino, peso, valor, status):

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
    print("Listando fretes cadastrados...")
    
    for frete in fretes:
        print(f"\nFretes Criados:", fretes)