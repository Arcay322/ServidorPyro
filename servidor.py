import Pyro4

@Pyro4.expose
class CalculadoraFactorial:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

def iniciar_servidor():
    Pyro4.config.HOST = "0.0.0.0"  # Exponer el servidor en todas las interfaces
    daemon = Pyro4.Daemon(host=Pyro4.config.HOST)
    uri = daemon.register(CalculadoraFactorial)
    print(f"Servidor Pyro4 listo en la URI: {uri}")
    daemon.requestLoop()

if __name__ == "__main__":
    iniciar_servidor()
