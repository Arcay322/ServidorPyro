import os
import Pyro4

# Clase expuesta para calcular el factorial
@Pyro4.expose
class FactorialServer:
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

# Función para iniciar el servidor Pyro4
def start_server():
    # Captura el puerto proporcionado por Render desde la variable de entorno 'PORT'
    port = int(os.getenv("PORT", "9090"))  # Si no se encuentra la variable, usa el 9090 como valor predeterminado

    # Inicia el servidor Pyro4 en todas las interfaces (host="0.0.0.0") y en el puerto capturado
    daemon = Pyro4.Daemon(host="0.0.0.0", port=port)

    # Registra el objeto remoto (FactorialServer) y obtén su URI
    uri = daemon.register(FactorialServer)
    print(f"Servidor factorial disponible en {uri}")

    # Mantiene el servidor Pyro4 corriendo
    daemon.requestLoop()

if __name__ == "__main__":
    start_server()
