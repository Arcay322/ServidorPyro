import os
import Pyro4

@Pyro4.expose
class FactorialServer:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

def start_server():
    # Obtener el puerto de la variable de entorno que Render proporciona
    port = int(os.getenv("PORT", "8080"))
    # Iniciar el demonio Pyro en el puerto y host especificados
    daemon = Pyro4.Daemon(host="0.0.0.0", port=port)
    uri = daemon.register(FactorialServer)  # Registrar la clase
    print("Servidor listo. URI:", uri)
    daemon.requestLoop()  # Mantener el servidor corriendo

if __name__ == "__main__":
    start_server()
