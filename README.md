# Sistema Bancário v2

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

---

Desafio: Aprimorar sistema bancário com datetime e funções novas
Programa: DIO - NTT Data Science Bootcamp

## Melhorias implementados

    1. ✅ Criar função deposita().
    2. ✅ Criar função saque().
    3. ✅ Mudar função de extrato para receber saldo como argumento posicional
    e extrato como argumento nomeado.
        NOTE: def f(pos1, pos2, /, pos_or_kw, *, kwd1, kwd2)
    4. ✅ Adiciona data e hora no extrato das transações
    5. ✅ Estabalece max. 3 saques por dia, verificado com datetime
    6. ✅ Criar função: cria_usuário()
        O programa deve armanezar os usuarios em uma lista, um usuario é composto por: nome,
        data de nascimento, CPF e endereço. O endereço é uma string com o formato: logradouro,
        nro - bairro - cidade/sigla estado. Deve ser armazenado somente os numeros do cpf.
        Não podemos cadastrar 2 usuarios com o mesmo cpf.
    7. ✅ Criar função: cria_conta()
        O programa deve armazenar contas em uma lista, uma conta e composta por: agencia,
        número da conta e usuario. O numero da conta e sequential, iniciando em 1.
        O número da agencia e fixo: "0001". O usuario pode ter mais de uma conta,
        mas uma conta pertence a somente um usuário.
    8. ✅ Criar "testes" para verificar funções acima
        NOTE: Só criei funções para imprimir usuarios e contas, não testes de verdade.

## Habilidades aprimorados / Conceitos firmados

- Datetime module
- Funções
- Listas, dicionários e acessando dados

## Deu certo

O extrato ficou melhor ainda:

```
====================================================================================================

                                              Extrato

====================================================================================================

---------------------------------------Histórico de Operações---------------------------------------
--#----------Data---------------Hora-------------Operação------------Valor--------------Saldo-------
     |                  |                  |                  |                  |
 001 |    09/09/2024    |      11:22       |     DEPOSITO     |    R$1000.00     |    R$1000.00
 002 |    09/09/2024    |      11:22       |     DEPOSITO     |     R$100.00     |    R$1100.00
 003 |    09/09/2024    |      11:22       |      SAQUE       |    -R$200.00     |     R$900.00
 004 |    09/09/2024    |      11:23       |      SAQUE       |    -R$123.54     |     R$776.46
 005 |    09/09/2024    |      11:23       |     DEPOSITO     |     R$240.00     |    R$1016.46
 006 |    09/09/2024    |      11:23       |      SAQUE       |    -R$100.00     |     R$916.46
     |                  |                  |                  |                  |
====================================================================================================
                                       Saldo atual: R$916.46
====================================================================================================
```

## Para melhorar

- Liga transações e extratos com usuários/contas específicos
- Implementar Classes

---

---

---

# Banking System v2

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

---

Challenge: Improve banking system with datetime and new functions
Program: DIO - NTT Data Science Bootcamp

## Improvements implemented

    1. ✅ Create function deposita(). [deposit]
    2. ✅ Create function saque(). [withdrawal]
    3. ✅ Change imprimir_extrato() [print transaction history] function to receive balance as a positional argument
        and transaction history as keyword argument.
        NOTE: def f(pos1, pos2, /, pos_or_kw, *, kwd1, kwd2)
    4. ✅ Add date and time to transaction history
    5. ✅ Establish max. 3 withdrawals per day, verified with datetime
    6. ✅ Create function: cria_usuário() [create user]
    7. ✅ Create function: cria_conta() [create account]
    8. ✅ Create "tests" to verify above function
        NOTE: I just created functions that print all the users and accounts, not real tests.

## Skills improved / Concepts reinforced

- Datetime module
- Functions
- Lists, dictionaries and accessing data

## Worked well

The transaction history looks even better:

```
====================================================================================================

                                              Extrato

====================================================================================================

---------------------------------------Histórico de Operações---------------------------------------
--#----------Data---------------Hora-------------Operação------------Valor--------------Saldo-------
     |                  |                  |                  |                  |
 001 |    09/09/2024    |      11:22       |     DEPOSITO     |    R$1000.00     |    R$1000.00
 002 |    09/09/2024    |      11:22       |     DEPOSITO     |     R$100.00     |    R$1100.00
 003 |    09/09/2024    |      11:22       |      SAQUE       |    -R$200.00     |     R$900.00
 004 |    09/09/2024    |      11:23       |      SAQUE       |    -R$123.54     |     R$776.46
 005 |    09/09/2024    |      11:23       |     DEPOSITO     |     R$240.00     |    R$1016.46
 006 |    09/09/2024    |      11:23       |      SAQUE       |    -R$100.00     |     R$916.46
     |                  |                  |                  |                  |
====================================================================================================
                                       Saldo atual: R$916.46
====================================================================================================
```

## Potential improvements

- Link transactios and histories to specific users/accounts
- Implement Classes

---

---

---

---

---

# Sistema Bancário v1

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

# Banking System v1

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

- Add a database to maintain a registry of users, balances and transactions.
- Add login (users, passwords, etc.)
