"""Exercício 19 — maior e menor de três números."""


def extremos(valores):
    return max(valores), min(valores)


if __name__ == "__main__":
    valores = [float(input(f"Valor {i}: ").replace(",", ".")) for i in range(1, 4)]
    maior, menor = extremos(valores)
    print(f"Maior: {maior:g}")
    print(f"Menor: {menor:g}")
