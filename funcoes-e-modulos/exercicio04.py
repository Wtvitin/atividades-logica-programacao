"""Exercício 4: demonstração de escopo local e global."""

x = 10  # Variável global


def alterar_valor():
    x = 5  # Variável local, existente apenas nesta função
    print(f"Valor dentro da função: {x}")


if __name__ == "__main__":
    alterar_valor()
    print(f"Valor fora da função: {x}")

# Resposta a:
# Valor dentro da função: 5
# Valor fora da função: 10
#
# Resposta b:
# O x = 5 é local à função alterar_valor. Ele não modifica o x = 10
# definido no escopo global; por isso, fora da função, x continua 10.
