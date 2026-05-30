from funções import limpar_terminal, ler_dados, salvar_dados
from usuarios import login_empresa

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
            
class carga:
    def __init__(self, id_carga, nome, empresa_cnpj, origem, destino, peso, valor):
        self.id_carga = id_carga
        self.nome = nome
        self.empresa_cnpj = empresa_cnpj
        self.origem = origem
        self.destino = destino
        self.peso = peso
        self.valor = valor
        self.status = "DISPONIVEL"
        self.motorista_cpf = None

    def reservar(self, cpf_motorista): 
        if self.status == "DISPONIVEL":
            self.status = "RESERVADO"
            self.motorista_cpf = cpf_motorista

            print('carga reservado com sucesso!')
            return True
        else:
            print("Desculpe, esta carga não está mais disponível.")
            return False


def main():
    postar_carga(cnpj)
if __name__ == '__main__':
    main()