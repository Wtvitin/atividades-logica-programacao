"""Exercício 27 — IMC e faixas didáticas da apostila."""


def classificar_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero")
    imc = peso / (altura * altura)
    if imc < 18.5:
        faixa = "ABAIXO DA FAIXA"
    elif imc < 25:
        faixa = "FAIXA NORMAL"
    elif imc < 30:
        faixa = "ACIMA DA FAIXA"
    else:
        faixa = "FAIXA ELEVADA"
    return imc, faixa


if __name__ == "__main__":
    peso = float(input("Peso (kg): ").replace(",", "."))
    altura = float(input("Altura (m): ").replace(",", "."))
    try:
        imc, faixa = classificar_imc(peso, altura)
        print(f"IMC: {imc:.2f}")
        print(f"Classificação: {faixa}")
    except ValueError as erro:
        print(erro)
