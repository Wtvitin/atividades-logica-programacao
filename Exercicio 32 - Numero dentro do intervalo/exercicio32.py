"""Exercício 32 — intervalo fechado de 10 a 20."""


def classificar(numero):
    return "DENTRO" if 10 <= numero <= 20 else "FORA"


if __name__ == "__main__":
    numero = float(input("Digite um número: ").replace(",", "."))
    print(classificar(numero))
