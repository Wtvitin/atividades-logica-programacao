"""Exercício 24 — ano bissexto."""


def bissexto(ano):
    return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)


if __name__ == "__main__":
    ano = int(input("Ano: "))
    print("BISSEXTO" if bissexto(ano) else "NÃO BISSEXTO")
