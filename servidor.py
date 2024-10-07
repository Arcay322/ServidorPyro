import Pyro4
from flask import Flask
import threading

# Crear una aplicación Flask para servir HTTP
app = Flask(__name__)

# Ruta simple que responde a Render para "mantener feliz" el servicio web
@app.route('/')
def home():
    return "Servidor Pyro4 corriendo."

# Iniciar el servidor Pyro4 en un hilo separado
def iniciar_servidor_pyro():
    Pyro4.config.HOST = "0.0.0.0"
    daemon = Pyro4.Daemon(host=Pyro4.config.HOST)
    uri = daemon.register(CalculadoraFactorial)
    print(f"Servidor Pyro4 listo en la URI: {uri}")
    daemon.requestLoop()

# Clase Pyro4 para el cálculo de factorial
@Pyro4.expose
class CalculadoraFactorial:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

if __name__ == "__main__":
    # Crear un hilo para correr el servidor Pyro4 en paralelo
    hilo_pyro = threading.Thread(target=iniciar_servidor_pyro)
    hilo_pyro.daemon = True
    hilo_pyro.start()

    # Iniciar el servidor HTTP Flask en el puerto que Render espera
    app.run(host='0.0.0.0', port=10000)
