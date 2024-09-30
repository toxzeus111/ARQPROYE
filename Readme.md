# Proyecto Cliente/Servidor en Python

## Descripción
Este proyecto es un ejemplo básico de una arquitectura cliente/servidor utilizando Flask para el servidor y requests para el cliente. El servidor ofrece un endpoint que responde con un saludo en formato JSON.

## Requisitos
- **Python**: Asegúrate de tener instalada la versión 3.x de Python.
- **Flask**: Para ejecutar el servidor.
- **Requests**: Para hacer solicitudes HTTP desde el cliente.


```bash
pip install Flask requests
## Funcionamiento del Proyecto

Este proyecto implementa una arquitectura cliente/servidor utilizando Flask como framework para el servidor y la biblioteca `requests` para el cliente. 

### Servidor
- El archivo `servidor.py` configura un servidor Flask que escucha en el puerto 5000.
- Proporciona un único endpoint (`/hola`) que, al ser accedido mediante una solicitud GET, devuelve un mensaje en formato JSON: `{"mensaje": "¡Hola, mundo!"}`.

### Cliente
- El archivo `cliente.py` se encarga de realizar una solicitud GET al endpoint del servidor.
- Cuando el cliente recibe la respuesta del servidor, imprime el mensaje en la consola.

### Proceso de Ejecución
1. Primero, se debe iniciar el servidor ejecutando `servidor.py`, lo que permite que el servidor comience a escuchar solicitudes.
2. Luego, en otra terminal, se ejecuta `cliente.py`, que realiza la solicitud al servidor y muestra la respuesta.

Este modelo demuestra la interacción básica entre un cliente y un servidor, ilustrando cómo se pueden comunicar y compartir información a través de solicitudes HTTP.
