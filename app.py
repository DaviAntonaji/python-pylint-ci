from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_app_name():
    app_name = "Minha Aplicação Flask"
    return jsonify({'name': app_name})

if __name__ == '__main__':
    app.run(debug=True)
