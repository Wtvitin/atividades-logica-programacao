"""Exercício 25 — preço conforme a forma de pagamento."""


def calcular(preco, opcao):
    fatores = {1: 0.90, 2: 0.95, 3: 1.00, 4: 1.08}
    if opcao not in fatores:
        raise ValueError("Opção inválida")
    return preco * fatores[opcao]


if __name__ == "__main__":
    preco = float(input("Preço do produto: R$ ").replace(",", "."))
    print("1 - Dinheiro ou Pix | 2 - Débito | 3 - Crédito à vista | 4 - Crédito parcelado")
    opcao = int(input("Opção: "))
    try:
        print(f"Valor final: R$ {calcular(preco, opcao):.2f}")
    except ValueError as erro:
        print(erro)
