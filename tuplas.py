# Tuplas em Python

print("="*60)
print("TUPLAS EM PYTHON")
print("="*60 + "\n")

# Explicação
print("O QUE É UMA TUPLA?\n")
print("""
Uma tupla é uma sequência de elementos imutável (não pode ser modificada).

Características:
✓ Imutável (não pode ser modificada)
✓ Ordenada (mantém ordem)
✓ Acessa por índice (como listas)
✓ Pode conter diferentes tipos
✓ Usa parênteses: ()

Sintaxe: tupla = (elemento1, elemento2, elemento3)
""")

print("="*60 + "\n")

# 1. Criando tuplas
print("1. CRIANDO TUPLAS:\n")

# Tupla vazia
tupla_vazia = ()
print(f"Tupla vazia: {tupla_vazia}")

# Tupla com um elemento (precisa de vírgula!)
tupla_um = (42,)
print(f"Tupla com um elemento: {tupla_um}")

# Tupla com vários elementos
tupla_numeros = (1, 2, 3, 4, 5)
print(f"Tupla de números: {tupla_numeros}")

# Tupla com strings
tupla_palavras = ("Python", "é", "incrível")
print(f"Tupla de strings: {tupla_palavras}")

# Tupla mista
tupla_mista = ("João", 25, 8.5, True)
print(f"Tupla mista: {tupla_mista}")

# Sem parênteses (ainda é tupla!)
tupla_implícita = 5, 10, 15
print(f"Tupla sem parênteses: {tupla_implícita}\n")

print("="*60 + "\n")