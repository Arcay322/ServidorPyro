import os
import Pyro4

@Pyro4.expose
class FactorialServer:
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

def start_name_server():
    # Inicia el servidor de nombres en el puerto 9090
    Pyro4.naming.startNS(host='0.0.0.0', port=9090)

def start_server():
    # Captura el puerto proporcionado por Render
    port = os.getenv("PORT", "5000")  # Usa 5000 como valor predeterminado
    try:
        port = int(port)  # Intenta convertir a entero
    except ValueError:
        print(f"Valor no válido para el puerto: {port}. Usando 5000 como valor predeterminado.")
        port = 5000

    # Inicia el servidor de nombres
    start_name_server()

    # Inicia el daemon del servidor
    daemon = Pyro4.Daemon(host="0.0.0.0", port=port)

    # Registra el servidor de nombres
    ns = Pyro4.locateNS()  # Cambia esto a locateNS() solo si el servidor de nombres ya está en funcionamiento
    uri = daemon.register(FactorialServer)
    ns.register("factorial.server", uri)

    print(f"Servidor factorial disponible en {uri}")  # Esta línea imprime la URI

    # Mantiene el servidor corriendo
    daemon.requestLoop()

if __name__ == "__main__":
    start_server()
