import requests

def obtener_saludo():
    """Función que hace una solicitud al servidor y obtiene el saludo."""
    response = requests.get('http://127.0.0.1:5000/hola')
    if response.status_code == 200:
        return response.json()['mensaje']
    else:
        return "Error al obtener el saludo."

if __name__ == '__main__':
    saludo = obtener_saludo()
    print(saludo)