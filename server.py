import Pyro4
import os

@Pyro4.expose
class FactorialServer(object):
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

def start_server():
    # Obtener el puerto desde las variables de entorno proporcionadas por Render
    port = int(os.getenv("PORT", 9090))  # Render asigna un puerto a través de la variable PORT
    host = "0.0.0.0"  # Asegurarse de que Pyro4 escuche en todas las interfaces
    daemon = Pyro4.Daemon(host=host, port=port)  # Crear un daemon Pyro4 en el puerto especificado y enlazarlo a 0.0.0.0
    uri = daemon.register(FactorialServer)  # Registrar el servidor
    print(f"Servidor disponible en URI: {uri}")
    daemon.requestLoop()  # Mantener el servidor corriendo

if __name__ == "__main__":
    start_server()
