"""Exercício 2: cálculo da área de um círculo."""

import math


def calcular_area_circulo(raio):
    return math.pi * raio ** 2


def main():
    raio = float(input("Digite o raio do círculo: ").replace(",", "."))
    if raio < 0:
        print("O raio não pode ser negativo.")
        return

    area = calcular_area_circulo(raio)
    print(f"Área do círculo: {area:.2f}")


if __name__ == "__main__":
    main()
