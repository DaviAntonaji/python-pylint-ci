""""
Este arquivo é o arquivo principal da aplicação, onde a aplicação inicia.
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_app_name():
    """
    Esta rota responde a uma solicitação GET na raiz '/' da aplicação Flask.
    
    Retorna:
        Um JSON contendo o nome da aplicação.
    """
    app_name = "Minha Aplicação Flask"
    return jsonify({'name': app_name})

if __name__ == '__main__':
    app.run(debug=False)
    
