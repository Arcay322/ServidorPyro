import os
import Pyro4
import threading

@Pyro4.expose
class FactorialServer:
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

def start_nameserver():
    # Inicia el nameserver
    Pyro4.naming.startNS(host="0.0.0.0", port=9090)

def start_server():
    # Inicia el Nameserver en un hilo
    ns_thread = threading.Thread(target=start_nameserver)
    ns_thread.start()

    # Usa un puerto estático para pruebas
    port = 5000
    print(f"Iniciando el servidor en el puerto {port}")

    # Inicia el daemon del servidor
    daemon = Pyro4.Daemon(host="0.0.0.0", port=port)

    # Registra el servidor en el Nameserver
    uri = daemon.register(FactorialServer)
    print(f"Servidor factorial disponible en {uri}")

    # Mantiene el servidor corriendo
    daemon.requestLoop()

if __name__ == "__main__":
    start_server()
