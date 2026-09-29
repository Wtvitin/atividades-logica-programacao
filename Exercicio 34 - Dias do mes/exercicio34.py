"""Exercício 34 — número de dias do mês, considerando ano bissexto."""


def dias_do_mes(mes, ano):
    if mes < 1 or mes > 12:
        return "MÊS INVÁLIDO"
    if mes == 2:
        bissexto = ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)
        return "29 dias" if bissexto else "28 dias"
    if mes in (4, 6, 9, 11):
        return "30 dias"
    return "31 dias"


if __name__ == "__main__":
    mes = int(input("Número do mês: "))
    ano = int(input("Ano: "))
    print(dias_do_mes(mes, ano))
