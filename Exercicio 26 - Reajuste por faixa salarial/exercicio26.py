"""Exercício 26 — reajuste por faixa salarial."""


def reajustar(salario):
    if salario <= 1500:
        percentual = 15
    elif salario <= 3000:
        percentual = 10
    else:
        percentual = 5
    aumento = salario * percentual / 100
    return percentual, aumento, salario + aumento


if __name__ == "__main__":
    salario = float(input("Salário atual: R$ ").replace(",", "."))
    percentual, aumento, novo_salario = reajustar(salario)
    print(f"Percentual: {percentual}%")
    print(f"Aumento: R$ {aumento:.2f}")
    print(f"Novo salário: R$ {novo_salario:.2f}")
