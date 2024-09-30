from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hola', methods=['GET'])
def hola():
    """Endpoint que devuelve un saludo en formato JSON."""
    return jsonify({"mensaje": "¡Hola, mundo!"})

if __name__ == '__main__':
    app.run(port=5000)