"""Exercício 21 — aprovado ou reprovado (média mínima 7,0)."""


def avaliar(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media, "APROVADO" if media >= 7 else "REPROVADO"


if __name__ == "__main__":
    nota1 = float(input("Nota 1: ").replace(",", "."))
    nota2 = float(input("Nota 2: ").replace(",", "."))
    media, situacao = avaliar(nota1, nota2)
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao}")
