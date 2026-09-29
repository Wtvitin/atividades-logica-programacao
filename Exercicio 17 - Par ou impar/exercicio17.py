"""Exercício 17 — par ou ímpar."""


def classificar(numero):
    return "PAR" if numero % 2 == 0 else "ÍMPAR"


if __name__ == "__main__":
    numero = int(input("Digite um número inteiro: "))
    print(classificar(numero))
