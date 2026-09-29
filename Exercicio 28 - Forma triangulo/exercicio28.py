"""Exercício 28 — verificar se três lados formam um triângulo."""


def forma_triangulo(a, b, c):
    return (a > 0 and b > 0 and c > 0
            and a < b + c and b < a + c and c < a + b)


if __name__ == "__main__":
    a = float(input("Lado A: ").replace(",", "."))
    b = float(input("Lado B: ").replace(",", "."))
    c = float(input("Lado C: ").replace(",", "."))
    print("FORMAM" if forma_triangulo(a, b, c) else "NÃO FORMAM")
