# Sistema Bancário

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

---

Desafio: Criar um sistema bancário  
Programa: DIO - NTT Data Science Bootcamp

## Sumário

Um simples sistema bancário com opções de depositar, sacar, mostrar extrato e sair do programa. Usuários não podem sacar mais do que tem na conta, sacar mais do que R$500 por vez ou sacar mais do que 3 vezes por dia.

## Habilidades aprimorados / Conceitos firmados

### Manipulação de strings

Para deixar o extrato do jeito que eu queria, eu fiz muito uso de concatenação, f-string literals e `center()`.

### Outros

- Commentando código com claridade
- Nomes claros para variáveis
- While loops e conditional statements
- Português
- README's

## Deu certo

O extrato ficou legal:

```
===================================================

                      Extrato

===================================================

---------------Histórico de Operações--------------
--#----------Operação----------------Saldo---------
     |                      |
 001 |      R$10000.00      |      R$10000.00
 002 |      -R$500.00       |      R$9500.00
 003 |      -R$123.43       |      R$9376.57
 004 |       R$200.00       |      R$9576.57
 005 |      -R$450.00       |      R$9126.57
 006 |       R$100.00       |      R$9226.57
     |                      |
===================================================
```

## Não deu certo

tentei usar `textwrap.dedent()` para melhorar a legibilidade, i.e.

```
...
    dedent(print(f'''
        Você depositou {valor_depositar:.2f}.
        O seu saldo é {saldo:.2f}.
    '''))
```

em vez de

```
...
    print(f'''Você depositou {valor_depositar:.2f}.
O seu saldo é {saldo:.2f}.''')
```

mas não deu certo porque estava removendo todo o "leading whitespace" incluíndo o padding que eu precisava para o alinhamento do extrato.  
Nota: Talvez funcionaria de eu defini o padding explicitamente em vez de usar `center()`.

## Para melhorar

- Adiciona um banco de dados para manter um registro de usuários, saldos e transações
- Adiciona login (usuários, senhas, etc.)

---

---

---

# Banking System

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

---

Challenge: Create a banking system
Program: DIO - NTT Data Science Bootcamp

## Summary

A simple banking system with options to deposit, withdraw, display transaction history and exit the program. Users cannot withdraw more than they have in their account, withdraw more than R$500 at one time, or make more than 3 withdrawals in one day.

## Skills improved / Concepts reinforced

### String manipulation

To get the transaction history looking how I wanted it I used a lot of concatenation, f-string literals and `center()`

### Others

- Clearly commenting code
- Clear variable names
- While loops and conditional statements
- Portuguese
- README's

## Worked well

The transaction history looks good:

```
===================================================

                      Extrato

===================================================

---------------Histórico de Operações--------------
--#----------Operação----------------Saldo---------
     |                      |
 001 |      R$10000.00      |      R$10000.00
 002 |      -R$500.00       |      R$9500.00
 003 |      -R$123.43       |      R$9376.57
 004 |       R$200.00       |      R$9576.57
 005 |      -R$450.00       |      R$9126.57
 006 |       R$100.00       |      R$9226.57
     |                      |
===================================================
```

## Didn't work out

I tried to use `textwrap.dedent()` to improve legibility, i.e.

```
...
    dedent(print(f'''
        Você depositou {valor_depositar:.2f}.
        O seu saldo é {saldo:.2f}.
    '''))
```

instead of

```
...
    print(f'''Você depositou {valor_depositar:.2f}.
O seu saldo é {saldo:.2f}.''')
```

but it didn't work because it was removing all the leading whitespace, includingg the padding that I needed to align the transaction history.  
Note: Might work if I hardcoded the padding instead of using `center()`.

## Potential improvements

- Add a database to maintain a registry of users, blanaces and transactions.
- Add login (users, passwords, etc.)
