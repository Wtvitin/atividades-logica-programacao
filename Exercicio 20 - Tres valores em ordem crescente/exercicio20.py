"""Exercício 20 — ordenar três inteiros em ordem crescente."""


def ordenar(valores):
    return sorted(valores)


if __name__ == "__main__":
    valores = [int(input(f"Valor {i}: ")) for i in range(1, 4)]
    print("Ordem crescente:", *ordenar(valores))
