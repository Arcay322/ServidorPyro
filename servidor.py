import Pyro4
import Pyro4.naming


@Pyro4.expose
class FactorialCalculator:
    def factorial(self, n):
        if n < 0:
            raise ValueError("El número debe ser no negativo.")
        elif n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)


def start_server():
    # Iniciar el Nameserver
    Pyro4.naming.startNS()

    # Crear el daemon y registrar el objeto
    daemon = Pyro4.Daemon()
    uri = daemon.register(FactorialCalculator)

    # Registrar el objeto en el Nameserver
    ns = Pyro4.locateNS()
    ns.register("factorial.calculator", uri)

    print("El servidor está corriendo. Accede a través de 'factorial.calculator'")

    # Ejecutar el servidor
    daemon.requestLoop()


if __name__ == "__main__":
    start_server()
