import json
import os

def limpar_terminal():
    os.system("cls")

ARQUIVO_DADOS = "dados.json"

def ler_dados():
    # Centraliza a leitura do JSON para evitar repeticao.
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
    
def salvar_dados(dados):
    # Salva os dados formatados de volta no arquivo.
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def saida():
    limpar_terminal()
    print('''
Resposta inválida. Caso deseje sair pressione X, 
caso queira continuar pressione qualquer tecla.
    ''')
    resposta = input('O que deseja: ').lower()
    limpar_terminal()
    return resposta == 'x' 