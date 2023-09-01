import sys, os, math
from random import randint
import datetime
import urllib.request, requests

def funcao_muito_util(numero):
    resultado = math.factorial(numero)
    return resultado

class MinhaClasse:
    def __init__(self, nome):
        self.nome = nome
        self.idade = 0

    def configurar_idade(self, nova_idade):
        self.idade = nova_idade

def main():
    print("Bem-vindo ao programa sujo!")

    numero = int(input("Digite um número: "))
    resultado = funcao_muito_util(numero)
    print("O fatorial do número é:", resultado)

    nome = input("Digite seu nome: ")
    instancia = MinhaClasse(nome)
    idade = int(input("Digite sua idade: "))
    instancia.configurar_idade(idade)

    print("Informações:")
    print("Nome:", instancia.nome)
    print("Idade:", instancia.idade)

    url = input("Digite uma URL para buscar: ")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Conteúdo da página:", response.content)
        else:
            print("Erro ao acessar a URL")
    except:
        print("Erro ao realizar a requisição")

if __name__ == "__main__":
    main()
