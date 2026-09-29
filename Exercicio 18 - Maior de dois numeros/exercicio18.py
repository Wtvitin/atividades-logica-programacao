"""Exercício 18 — maior de dois números."""


def maior_valor(primeiro, segundo):
    if primeiro == segundo:
        return "VALORES IGUAIS"
    return primeiro if primeiro > segundo else segundo


if __name__ == "__main__":
    primeiro = float(input("Primeiro valor: ").replace(",", "."))
    segundo = float(input("Segundo valor: ").replace(",", "."))
    print(maior_valor(primeiro, segundo))
