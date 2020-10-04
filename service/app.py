"""
Servidor para rodar o docker com o flask
"""

from flask import Flask, request
from main import services

app = Flask(__name__)

@app.route("/<path:path>", methods=['GET'])
def service(path):
    """
    Name: Service

    Descrição:
        Retorna o enpoint requisitado

    Args: path (endpoint)

    Return: request /path
    """
    return services(request)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
