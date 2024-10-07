import os
import Pyro4


@Pyro4.expose
class FactorialServer:
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)


def start_server():
    # Obtener el puerto dinámico que proporciona Render o usar el 9090 por defecto
    port = int(os.getenv("PORT", "9090"))

    # Iniciar el servidor Pyro4 escuchando en todas las interfaces
    daemon = Pyro4.Daemon(host="0.0.0.0", port=port)

    # Registrar el objeto remoto en el servidor
    uri = daemon.register(FactorialServer)

    print(f"Servidor factorial listo en {uri}")

    # Mantener el servidor corriendo
    daemon.requestLoop()


if __name__ == "__main__":
    start_server()
