"""Exercício 35 — meia-entrada sem acumular descontos."""


def valor_ingresso(idade, estudante):
    meia = idade < 12 or estudante.upper() == "SIM" or idade >= 60
    return 15.0 if meia else 30.0


if __name__ == "__main__":
    idade = int(input("Idade: "))
    estudante = input("Estudante? (SIM/NÃO): ").strip()
    print(f"Valor do ingresso: R$ {valor_ingresso(idade, estudante):.2f}")
