# Funções e módulos em Python

Cinco exercícios da lista **Funções & Módulos** e uma atividade prática do material didático sobre funções. Execute cada arquivo com Python 3, por exemplo:

```bash
python funcoes-e-modulos/exercicio01.py
```

| # | Tema | Código | Exemplo |
|:-:|---|---|---|
| 01 | Arredondamento e raiz quadrada | [exercicio01.py](exercicio01.py) | Entrada `9,7` → raiz `3.11`, teto `10`, piso `9` |
| 02 | Área de círculo | [exercicio02.py](exercicio02.py) | Raio `2` → área `12.57` |
| 03 | Maior de três | [exercicio03.py](exercicio03.py) | `4`, `9`, `7` → `9` |
| 04 | Escopo de variáveis | [exercicio04.py](exercicio04.py) | Dentro `5`, fora `10` |
| 05 | Hipotenusa | [exercicio05.py](exercicio05.py) | Catetos `3` e `4` → `5.00` |
| 06 | Nota aleatória e situação do aluno | [exercicio06.py](exercicio06.py) | Nota `6.0` → `Aprovado`; nota `5.9` → `Reprovado` |

No exercício 4, **a)** a saída exata é:

```text
Valor dentro da função: 5
Valor fora da função: 10
```

**b)** A atribuição `x = 5` cria uma variável local em `alterar_valor`. A variável global `x = 10` continua com o mesmo valor fora da função.

Os exercícios 1, 2 e 5 aceitam ponto ou vírgula como separador decimal. Execute um arquivo por vez no terminal.

A atividade 06 gera uma nota aleatória entre 0,0 e 10,0, arredondada para uma casa decimal. A partir de 6,0, o aluno está aprovado. Execute com `python funcoes-e-modulos/exercicio06.py`.
