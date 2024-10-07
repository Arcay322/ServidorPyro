import Pyro4


def main():
    # Conectar al servidor
    calculator = Pyro4.Proxy("PYRONAME:factorial.calculator")

    # Solicitar un número al usuario
    number = int(input("Ingresa un número para calcular su factorial: "))

    # Calcular y mostrar el resultado
    try:
        result = calculator.factorial(number)
        print(f"El factorial de {number} es: {result}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
