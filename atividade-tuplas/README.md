# Atividade — Tuplas em Python

## Objetivo

Compreender o conceito de **tuplas** e praticar sua criação e o acesso aos elementos por índices em Python.

## Código-fonte

O arquivo [`tuplas.py`](../tuplas.py) contém os exemplos da atividade, correspondentes às **linhas 1 a 64** do [material de referência de OdaGab](https://github.com/OdaGab/Python/blob/main/tuplas.py).

## Parte 1 — Criação de tuplas

| Exemplo | Código | Resultado esperado |
|---|---|---|
| Tupla vazia | `()` | `()` |
| Um elemento | `(42,)` | `(42,)` |
| Números | `(1, 2, 3, 4, 5)` | `(1, 2, 3, 4, 5)` |
| Textos | `("Python", "é", "incrível")` | `('Python', 'é', 'incrível')` |
| Tipos mistos | `("João", 25, 8.5, True)` | `('João', 25, 8.5, True)` |
| Sem parênteses | `5, 10, 15` | `(5, 10, 15)` |

**Explicação:** tuplas são sequências ordenadas e imutáveis. Uma tupla de um único elemento precisa da vírgula, como em `(42,)`. Também é possível criá-las sem parênteses.

## Parte 2 — Acesso por índices

A tupla utilizada é `("a", "b", "c", "d", "e")`.

| Expressão | Resultado esperado | Explicação |
|---|---|---|
| `tupla[0]` | `a` | Primeiro elemento |
| `tupla[-1]` | `e` | Último elemento |
| `tupla[2]` | `c` | Terceiro elemento, pois os índices começam em zero |
| `tupla[-2]` | `d` | Penúltimo elemento |

## Como executar

Na raiz do repositório, com Python 3 instalado:

```bash
python tuplas.py
```

## Conclusão

A atividade demonstra como declarar tuplas de diferentes formatos e acessar seus valores com índices positivos e negativos. Diferentemente de uma lista, uma tupla não permite substituir diretamente seus elementos após a criação.

> **Verificação:** as tabelas apresentam os resultados esperados para o código fornecido. Não são evidência de uma execução real no terminal.
