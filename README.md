# Python Pylint CI

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/DaviAntonaji/python-pylint-ci/Python%20Code%20Quality?label=Code%20Quality&logo=github&style=flat-square)](https://github.com/DaviAntonaji/python-pylint-ci/actions)

Este repositório contém um workflow de CI/CD para verificar a qualidade do código Python usando Pylint, Bandit e outras ferramentas.

## Checks de Qualidade de Código

O workflow `Python Code Quality` é acionado em commits na branch `main` e pull requests para a mesma branch. Ele realiza várias verificações de qualidade de código, incluindo:

| Check                                        | Descrição                                     |
| -------------------------------------------- | -------------------------------------------- |
| **Unused Imports**                           | Verifica se há importações não utilizadas.    |
| **Import Order**                             | Verifica a ordem das importações.             |
| **PEP 8 Compliance**                         | Verifica a conformidade com PEP 8.            |
| **Docstring Conventions**                    | Verifica as convenções de docstrings.         |
| **Naming Conventions**                       | Verifica as convenções de nomenclatura.       |
| **Cyclomatic Complexity**                    | Verifica a complexidade ciclomática.          |
| **Resource Management**                     | Verifica o gerenciamento de recursos.         |
| **Duplicated Code**                         | Verifica código duplicado.                    |
| **Security Vulnerabilities**                 | Verifica vulnerabilidades de segurança com Bandit. |
| **Dependency Security**                     | Verifica a segurança das dependências com Safety. |

O código deve atender ao limite de qualidade definido no arquivo de configuração.

## Como Executar Localmente

Para executar as verificações de qualidade de código localmente, você pode seguir estas etapas:

1. Clone o repositório:

   ```shell
   git clone https://github.com/seu-usuario/python-pylint-ci.git
   cd python-pylint-ci
    ```

2. Instale as dependências:
```
pip install -r requirements.txt
pip install pylint
```
Lembre-se de substituir <limite-de-qualidade> pelo seu limite desejado.

## Implantação
O workflow de implantação será acionado automaticamente em push para a branch main. Você pode personalizar a ação de implantação no arquivo de configuração de fluxo de trabalho validate.yaml.

## Exemplo de Implantação

## Contribuição
Fique à vontade para contribuir com melhorias, correções de bugs ou novos recursos. Siga o fluxo de trabalho padrão de Pull Requests.

## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE). Consulte o arquivo [LICENSE](LICENSE) para obter detalhes sobre os termos da licença.

A Licença MIT é uma licença de código aberto amplamente aceita que permite que você use, modifique e distribua livremente este software em projetos comerciais e pessoais. É altamente recomendado que você inclua esta seção de licença em todos os seus projetos de código aberto.
