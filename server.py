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
    port = int(os.getenv("PORT", "9090"))
    daemon = Pyro4.Daemon(host="0.0.0.0", port=port)

    # Registra el servidor de nombres
    ns = Pyro4.locateNS()
    uri = daemon.register(FactorialServer)
    ns.register("factorial.server", uri)

    print(f"Servidor factorial disponible en {uri}")

    # Mantiene el servidor corriendo
    daemon.requestLoop()

if __name__ == "__main__":
    start_server()
