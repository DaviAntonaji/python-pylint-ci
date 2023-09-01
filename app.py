import math
import requests

class MinhaClasse:
    """
    Classe para representar uma pessoa.
    """
    def __init__(self, nome):
        """
        Inicializa uma instância da classe MinhaClasse.
        
        Args:
            nome (str): O nome da pessoa.
        """
        self.nome = nome
        self.idade = 0

    def configurar_idade(self, nova_idade):
        """
        Configura a idade da pessoa.

        Args:
            nova_idade (int): A nova idade da pessoa.
        """
        self.idade = nova_idade

    def obter_nome(self):
        """
        Retorna o nome da pessoa.

        Returns:
            str: O nome da pessoa.
        """
        return self.nome

    def obter_idade(self):
        """
        Retorna a idade da pessoa.

        Returns:
            int: A idade da pessoa.
        """
        return self.idade

def funcao_muito_util(numero):
    """
    Calcula o fatorial de um número.

    Args:
        numero (int): O número para calcular o fatorial.

    Returns:
        int: O fatorial do número.
    """
    resultado = math.factorial(numero)
    return resultado

def main():
    """
    Função principal do programa.
    """
    print("Bem-vindo ao programa!")

    numero = int(input("Digite um número: "))
    resultado = funcao_muito_util(numero)
    print("O fatorial do número é:", resultado)

    nome = input("Digite seu nome: ")
    instancia = MinhaClasse(nome)
    idade = int(input("Digite sua idade: "))
    instancia.configurar_idade(idade)

    print("Informações:")
    print("Nome:", instancia.obter_nome())
    print("Idade:", instancia.obter_idade())

    url = input("Digite uma URL para buscar: ")
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            print("Conteúdo da página:", response.content)
        else:
            print("Erro ao acessar a URL")
    except requests.RequestException:
        print("Erro ao realizar a requisição")

if __name__ == "__main__":
    main()
