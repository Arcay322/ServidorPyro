import Pyro4
import os
from flask import Flask, jsonify
from threading import Thread

app = Flask(__name__)


@Pyro4.expose
class FactorialServer(object):
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)


# Ruta para mostrar la URI del servidor
@app.route('/uri')
def get_uri():
    port = int(os.getenv("PORT", 9090))
    uri = f"PYRO:obj_XXXXXX@0.0.0.0:{port}"  # Cambia 'obj_XXXXXX' por el identificador correcto
    return jsonify({"uri": uri})


def start_server():
    # Obtener el puerto desde las variables de entorno proporcionadas por Render
    port = int(os.getenv("PORT", 9090))
    host = "0.0.0.0"

    # Iniciar el servidor Pyro4
    daemon = Pyro4.Daemon(host=host, port=port)
    uri = daemon.register(FactorialServer)

    # Mantener el servidor Pyro corriendo en un hilo separado
    Thread(target=daemon.requestLoop).start()

    # Iniciar la aplicación Flask
    app.run(host='0.0.0.0', port=port, debug=True)


if __name__ == "__main__":
    start_server()
