"""Exercício 16 — positivo, negativo ou zero."""


def classificar(numero):
    if numero > 0:
        return "POSITIVO"
    if numero < 0:
        return "NEGATIVO"
    return "ZERO"


if __name__ == "__main__":
    numero = float(input("Digite um número: ").replace(",", "."))
    print(classificar(numero))
