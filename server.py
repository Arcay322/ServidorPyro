import Pyro4
import os
from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)


@Pyro4.expose
class FactorialServer(object):
    def factorial(self, n):
        if n < 0:
            raise ValueError("El número debe ser no negativo.")
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)


@app.route('/')
def index():
    # Obtener el puerto y la URI
    port = int(os.getenv("PORT", 9090))  # Usar el puerto asignado por Render o 9090 como valor por defecto
    # La URI se mostrará con 'localhost' si se ejecuta localmente
    uri = f"PYRO:obj_{id(FactorialServer)}@localhost:{port}"
    return render_template_string('''
        <html>
            <head><title>URI del Servidor Pyro4</title></head>
            <body>
                <h1>URI del Servidor Pyro4</h1>
                <p>{{ uri }}</p>
            </body>
        </html>
    ''', uri=uri)


def start_flask():
    # Iniciar la aplicación Flask
    port = int(os.getenv("PORT", 9090))
    app.run(host='0.0.0.0', port=port)


def start_server():
    # Obtener el puerto desde las variables de entorno
    port = int(os.getenv("PORT", 9090))  # Usamos 9090 como puerto por defecto si no está definido
    daemon = Pyro4.Daemon(port=port)  # Crear un daemon Pyro4 en el puerto especificado
    daemon.register(FactorialServer)  # Registrar el servidor

    # Iniciar el servidor Pyro en un hilo separado
    Thread(target=daemon.requestLoop).start()


if __name__ == "__main__":
    start_server()  # Iniciar el servidor Pyro4
    start_flask()  # Iniciar la aplicación Flask
