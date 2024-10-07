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
    # Obtener el puerto desde las variables de entorno
    port = int(os.getenv("PORT", 9090))  # Usamos 9090 como puerto por defecto si no está definido
    daemon = Pyro4.Daemon(port=port)  # Crear un daemon Pyro4 en el puerto especificado
    uri = daemon.register(FactorialServer)  # Registrar el servidor
    print(f"Servidor disponible en URI: {uri}")
    daemon.requestLoop()  # Mantener el servidor corriendo

if __name__ == "__main__":
    start_server()
