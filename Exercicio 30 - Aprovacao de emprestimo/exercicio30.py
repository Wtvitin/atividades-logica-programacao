"""Exercício 30 — prestação e limite de 30% do salário."""


def avaliar_emprestimo(imovel, salario, anos):
    if anos <= 0:
        raise ValueError("O prazo deve ser maior que zero")
    prestacao = imovel / (anos * 12)
    limite = salario * 0.30
    return prestacao, limite, "APROVADO" if prestacao <= limite else "NEGADO"


if __name__ == "__main__":
    imovel = float(input("Valor do imóvel: R$ ").replace(",", "."))
    salario = float(input("Salário mensal: R$ ").replace(",", "."))
    anos = int(input("Prazo (anos): "))
    try:
        prestacao, limite, situacao = avaliar_emprestimo(imovel, salario, anos)
        print(f"Prestação: R$ {prestacao:.2f}")
        print(f"Limite: R$ {limite:.2f}")
        print(f"Resultado: {situacao}")
    except ValueError as erro:
        print(erro)
