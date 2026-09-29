"""Exercício 33 — dia da semana para números de 1 a 7."""


def dia_da_semana(numero):
    dias = {
        1: "SEGUNDA-FEIRA", 2: "TERÇA-FEIRA", 3: "QUARTA-FEIRA",
        4: "QUINTA-FEIRA", 5: "SEXTA-FEIRA", 6: "SÁBADO", 7: "DOMINGO",
    }
    return dias.get(numero, "OPÇÃO INVÁLIDA")


if __name__ == "__main__":
    numero = int(input("Número de 1 a 7: "))
    print(dia_da_semana(numero))
