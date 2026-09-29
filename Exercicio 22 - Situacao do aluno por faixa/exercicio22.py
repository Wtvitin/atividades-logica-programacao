"""Exercício 22 — situação do aluno por faixa de média."""


def avaliar(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media < 5:
        situacao = "REPROVADO"
    elif media < 7:
        situacao = "RECUPERAÇÃO"
    else:
        situacao = "APROVADO"
    return media, situacao


if __name__ == "__main__":
    nota1 = float(input("Nota 1: ").replace(",", "."))
    nota2 = float(input("Nota 2: ").replace(",", "."))
    media, situacao = avaliar(nota1, nota2)
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao}")
