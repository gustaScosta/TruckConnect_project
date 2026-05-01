from funções import limpar_terminal, ler_dados, salvar_dados
from usuarios import login_empresa

cnpj = login_empresa()

def postar_carga(cnpj):
    limpar_terminal()
    while True:
        print('''
            Escolha o peso da carga que irá declarar

            1. +5.000 kg
            2. De 2.500 à 5.000 kg
            3. De 1.000 à 2.500 kg
            4. -1.000 kg 

            ''')
        try:
            peso_carga = int(input('Escolha: '))
        except ValueError:
            limpar_terminal()
            print("""
opção inválida
        1. continuar
        2. encerrar                
                      """)            
            invalida = int(input('escolha: '))
            if invalida == 1:
                continue
            else:
                limpar_terminal()
                return    

def main():
    postar_carga(cnpj)
if __name__ == '__main__':
    main()
    