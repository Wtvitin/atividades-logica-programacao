"""Atividade prática: gerar uma nota aleatória e verificar a situação do aluno."""

import random


def gerar_nota_aleatoria():
    """Retorna uma nota de 0,0 a 10,0 com uma casa decimal."""
    return round(random.uniform(0.0, 10.0), 1)


def verificar_situacao(nota):
    """Retorna a situação do aluno conforme a nota mínima 6,0."""
    if nota >= 6.0:
        return "Aprovado"
    return "Reprovado"


def main():
    nota = gerar_nota_aleatoria()
    situacao = verificar_situacao(nota)
    print(f"Nota gerada: {nota:.1f}")
    print(f"Situação do aluno: {situacao}")


if __name__ == "__main__":
    main()
