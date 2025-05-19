import flask
from flask import Flask, jsonify

#teste do pipeline 3

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint para verificação de saúde da aplicação."""
    return jsonify({"status": "healthy", "version": "1.0.0"})

@app.route('/', methods=['GET'])
def home():
    """Página inicial da aplicação."""
    return jsonify({
        "message": "Bem-vindo à API de demonstração do Projeto DevOps",
        "endpoints": [
            "/health - Verificação de saúde",
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
