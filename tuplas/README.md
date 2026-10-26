# Atividades — Tuplas em Python

As seções numeradas do arquivo de referência foram organizadas em exercícios independentes, cada um com seu próprio código e resultado esperado.

| Nº | Atividade | Código |
|---|---|---|
| 01 | Criando tuplas | [exercicio01.py](exercicio01.py) |
| 02 | Acessando elementos | [exercicio02.py](exercicio02.py) |
| 03 | Tuplas são imutáveis | [exercicio03.py](exercicio03.py) |

## Exercício 01 — Criando tuplas

**Objetivo:** criar tuplas vazias, unitárias, numéricas, textuais, mistas e sem parênteses.

**Resultados esperados:**
```text
Tupla vazia: ()
Tupla com um elemento: (42,)
Tupla de números: (1, 2, 3, 4, 5)
Tupla de strings: ('Python', 'é', 'incrível')
Tupla mista: ('João', 25, 8.5, True)
Tupla sem parênteses: (5, 10, 15)
```

## Exercício 02 — Acessando elementos

**Objetivo:** consultar posições de uma tupla com índices positivos e negativos.

**Resultados esperados:**
```text
Tupla: ('a', 'b', 'c', 'd', 'e')

Primeiro elemento: a
Último elemento: e
Índice 2: c
Índice -2: d
```

## Exercício 03 — Tuplas são imutáveis

**Objetivo:** comprovar que tuplas não permitem substituir elementos nem usar o método `append()`.

**Resolução:** o código cria a tupla `(1, 2, 3)` e tenta realizar duas operações inválidas, ambas tratadas com `try/except` para que o programa continue normalmente.

| Tentativa | Resultado esperado | Motivo |
|---|---|---|
| `tupla[0] = 99` | `TypeError` | Atribuição a um elemento de tupla não é permitida |
| `tupla.append(4)` | `AttributeError` | Tuplas não possuem o método `append` |

A tupla original permanece `(1, 2, 3)`. Esses erros são **esperados e tratados**, não falhas da resolução.

## Como executar

A partir da raiz do repositório:

```bash
python tuplas/exercicio01.py
python tuplas/exercicio02.py
python tuplas/exercicio03.py
```

> Resultados esperados por leitura do código. A execução real ainda precisa ser confirmada.

**Referência:** [OdaGab/Python — tuplas.py](https://github.com/OdaGab/Python/blob/main/tuplas.py), seções 1 e 2. O arquivo original utilizado permanece na raiz como `tuplas.py`.
