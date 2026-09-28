"""Exercício 5: hipotenusa pelo Teorema de Pitágoras."""

# 1. Imports
import math


# 2. Funções
def calcular_hipotenusa(cateto_a, cateto_b):
    return math.sqrt(cateto_a ** 2 + cateto_b ** 2)


# 3. Código principal
if __name__ == "__main__":
    cateto_a = float(input("Digite o primeiro cateto: ").replace(",", "."))
    cateto_b = float(input("Digite o segundo cateto: ").replace(",", "."))

    if cateto_a <= 0 or cateto_b <= 0:
        print("Os catetos devem ser maiores que zero.")
    else:
        hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)
        print(f"Hipotenusa: {hipotenusa:.2f}")
