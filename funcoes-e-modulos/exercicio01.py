"""Exercício 1: raiz quadrada e arredondamento com o módulo math."""

import math


def main():
    numero = float(input("Digite um número decimal positivo: ").replace(",", "."))
    if numero <= 0:
        print("Digite um número maior que zero.")
        return

    print(f"Raiz quadrada: {math.sqrt(numero):.2f}")
    print(f"Arredondado para cima: {math.ceil(numero)}")
    print(f"Arredondado para baixo: {math.floor(numero)}")


if __name__ == "__main__":
    main()
