"""Exercício 31 — divisibilidade por 3 e por 5."""


def classificar(numero):
    por_3 = numero % 3 == 0
    por_5 = numero % 5 == 0
    if por_3 and por_5:
        return "DIVISÍVEL POR 3 E 5"
    if por_3:
        return "DIVISÍVEL APENAS POR 3"
    if por_5:
        return "DIVISÍVEL APENAS POR 5"
    return "NÃO DIVISÍVEL POR 3 NEM 5"


if __name__ == "__main__":
    numero = int(input("Número inteiro: "))
    print(classificar(numero))
