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
    # Captura el puerto proporcionado por Render
    port = os.getenv("PORT", "5000")  # Usa 5000 como valor predeterminado
    try:
        port = int(port)  # Intenta convertir a entero
    except ValueError:
        print(f"Valor no válido para el puerto: {port}. Usando 5000 como valor predeterminado.")
        port = 5000

    daemon = Pyro4.Daemon(host="0.0.0.0", port=port)

    # Registra el servidor de nombres
    ns = Pyro4.locateNS()
    uri = daemon.register(FactorialServer)
    ns.register("factorial.server", uri)

    print(f"Servidor factorial disponible en {uri}")  # Esta línea imprime la URI

    # Mantiene el servidor corriendo
    daemon.requestLoop()

if __name__ == "__main__":
    start_server()
