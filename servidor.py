import Pyro4
import threading

@Pyro4.expose
class FactorialCalculator:
    def factorial(self, n):
        """Calcula el factorial de un número no negativo."""
        if n < 0:
            raise ValueError("El número debe ser no negativo.")
        elif n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

def start_nameserver():
    """Inicia el Nameserver en un hilo separado."""
    Pyro4.naming.startNS()

def start_server():
    """Inicia el servidor."""
    daemon = Pyro4.Daemon(host="0.0.0.0", port=9090)  # Escuchar en todas las interfaces y en el puerto 9090
    uri = daemon.register(FactorialCalculator)

    # Registrar el objeto en el Nameserver
    ns = Pyro4.locateNS()
    ns.register("factorial.calculator", uri)

    print("El servidor está corriendo. Accede a través de 'factorial.calculator'.")

    # Ejecutar el servidor
    daemon.requestLoop()

if __name__ == "__main__":
    # Iniciar el Nameserver en un hilo separado
    threading.Thread(target=start_nameserver, daemon=True).start()

    # Iniciar el servidor
    start_server()
