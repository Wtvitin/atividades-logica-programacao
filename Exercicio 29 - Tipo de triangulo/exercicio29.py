"""Exercício 29 — classificar o triângulo após verificar sua existência."""


def classificar(a, b, c):
    if min(a, b, c) <= 0 or a >= b + c or b >= a + c or c >= a + b:
        return "NÃO FORMA TRIÂNGULO"
    if a == b == c:
        return "EQUILÁTERO"
    if a == b or a == c or b == c:
        return "ISÓSCELES"
    return "ESCALENO"


if __name__ == "__main__":
    a = float(input("Lado A: ").replace(",", "."))
    b = float(input("Lado B: ").replace(",", "."))
    c = float(input("Lado C: ").replace(",", "."))
    print(classificar(a, b, c))
