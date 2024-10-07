import Pyro4

class FactorialCalculator(object):
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

# Crea un nombre para el objeto en el servidor de nombres
daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(FactorialCalculator)
ns.register("example.factorial", uri)

# Especifica el puerto (puedes cambiar esto si lo deseas)
port = 7777
daemon.start(port=port)

print(f"Servidor listo en el puerto {port}.")
daemon.requestLoop()