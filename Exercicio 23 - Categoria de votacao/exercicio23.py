"""Exercício 23 — categoria de votação conforme a tabela didática."""


def categoria(idade):
    if idade < 16:
        return "NÃO PODE VOTAR"
    if idade < 18 or idade >= 70:
        return "VOTO OPCIONAL"
    return "VOTO OBRIGATÓRIO"


if __name__ == "__main__":
    idade = int(input("Idade: "))
    print(categoria(idade))
