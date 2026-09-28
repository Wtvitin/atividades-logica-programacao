"""Exercício 3: maior valor entre três números inteiros."""


def encontrar_maior(a, b, c):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior


def main():
    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input("Digite o segundo número inteiro: "))
    c = int(input("Digite o terceiro número inteiro: "))

    print(f"O maior valor é: {encontrar_maior(a, b, c)}")


if __name__ == "__main__":
    main()
