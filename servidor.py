import Pyro4

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
    Pyro4.Daemon.serveSimple(
        {
            FactorialCalculator: "factorial.calculator"
        },
        ns=True
    )

if __name__ == "__main__":
    start_server()
