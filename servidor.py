import Pyro4
from flask import Flask
import threading
import logging
import time

# Configurar logging
logging.basicConfig(level=logging.INFO)

# Crear una aplicación Flask para servir HTTP
app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor Pyro4 corriendo."

@Pyro4.expose
class CalculadoraFactorial:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

# Iniciar el servidor Pyro4 en un hilo separado
def iniciar_servidor_pyro():
    Pyro4.config.HOST = "0.0.0.0"  # Hacer el servidor accesible externamente
    daemon = Pyro4.Daemon(host=Pyro4.config.HOST)
    uri = daemon.register(CalculadoraFactorial)

    # Imprimir la URI usando el nombre de dominio de Render
    public_uri = f"PYRO:{uri}@servidorpyro.onrender.com:{daemon.port}"
    time.sleep(1)  # Esperar 1 segundo antes de imprimir la URI
    logging.info(f"Servidor Pyro4 listo en la URI: {public_uri}")  # Usar logging para imprimir la URI

    try:
        daemon.requestLoop()
    except Exception as e:
        logging.error(f"Ocurrió un error en el servidor Pyro4: {e}")

if __name__ == "__main__":
    # Crear un hilo para correr el servidor Pyro4 en paralelo
    hilo_pyro = threading.Thread(target=iniciar_servidor_pyro)
    hilo_pyro.daemon = True
    hilo_pyro.start()

    # Iniciar el servidor HTTP Flask en el puerto que Render espera
    app.run(host='0.0.0.0', port=10000)
