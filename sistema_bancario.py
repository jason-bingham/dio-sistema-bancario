'''Sistema Bancário, v1'''

# pylint: disable-msg=C0103
# The above comment tells pylint not to flag variables for incorrect formatting
# (By default pylint assumes all variables are constants and expects them to be UPPER_CASE)

menu = '''
Por favor, faça a sua escolha digitando um número
da menu embaixo, e em seguida pressiona "enter":

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> '''

LIMITE_VALOR_SACADO_DIARIO = 500
LIMITE_NUMERO_SAQUES_DIARIOS = 3

# For extrato:
DISPLAY_WIDTH = 51
HALF_DISPLAY_WIDTH = int(DISPLAY_WIDTH / 2)
COLUMN_ONE = 5
COLUMN_TWO_THREE = 22
DOUBLE_LINE = "".center(DISPLAY_WIDTH, "=")
SINGLE_LINE = "".center(DISPLAY_WIDTH, "-")
COLUMN_DIVS = " " * COLUMN_ONE + "|" + " " * COLUMN_TWO_THREE + "|"

saldo = 0.00
valor_sacado_hoje = 0.00
numero_saques_hoje = 0

id_operacao = 0

historico = f'''{"Não foram realizadas movimentações.".center(DISPLAY_WIDTH, ".")}'''

def imprime_extrato(saldo_atual, historico_atual):
    """Imprime extrato com saldo e historico atualizados."""
    print(f'''
{DOUBLE_LINE}
            
{"Extrato".center(DISPLAY_WIDTH)}

{DOUBLE_LINE}

{"Histórico de Operações".center(DISPLAY_WIDTH, "-")}
{"#".center(COLUMN_ONE, "-") + "-"}{"Operação".center(COLUMN_TWO_THREE, "-") + "-"}{"Saldo".center(COLUMN_TWO_THREE, "-")}
{COLUMN_DIVS}
{historico_atual}
{COLUMN_DIVS}
{DOUBLE_LINE}
{f"Saldo atual: $R{str(f'{saldo_atual:.2f}')}".center(DISPLAY_WIDTH)}
{DOUBLE_LINE}
    ''')

def clear_screen():
    """Clears screen with newlines"""
    print("\n" * 70)

def formatar_valor(valor, e_saque = False):
    """Adiciona 'R$' e centrar valores para extrato"""
    if e_saque:
        return f"-R${f'{valor:.2f}'}".center(COLUMN_TWO_THREE)
    return f"R${f'{valor:.2f}'}".center(COLUMN_TWO_THREE)

while True:
    clear_screen()
    opcao = int(input(menu))

    id_operacao_formatado = ""

    if opcao == 0:
        # sair
        clear_screen()
        print("Obrigado por usar os nossos serviços!")
        break

    if opcao == 1:
        # deposito
        clear_screen()

        # conditional formatting for first line of history
        if id_operacao == 0:
            historico = ""
        else:
            id_operacao_formatado = "\n"

        # solicit deposit amount
        valor_depositar = float(input('''Quanto gostaria depositar? '''))

        # update values
        id_operacao += 1
        saldo += valor_depositar

        # format data for transaction history print-out
        id_operacao_formatado += f'{str(id_operacao).rjust(3, "0").center(5, " ")}'
        valor_depositado_formatado = formatar_valor(valor_depositar)
        saldo_formatado = formatar_valor(saldo)

        # update transaction history
        historico += f"{id_operacao_formatado}|{valor_depositado_formatado}|{saldo_formatado}"

        # print success message
        print(f'''Você depositou {valor_depositar:.2f}.
O seu saldo é {saldo:.2f}.''')

        # pauses program so user has time to review feedback
        input("Continua? ")

    elif opcao == 2:
        # saque
        clear_screen()

        # conditional formatting for first line of history
        if id_operacao == 0:
            historico = ""
        else:
            id_operacao_formatado = "\n"

        # solicit withdarawl amount
        valor_sacar = float(input('''Quanto gostaria sacar hoje? '''))

        # tests
        if valor_sacar > 500:
            print("Saque máximo: R$500.00")
            input("Continua? ")
        elif valor_sacar > saldo: #########
            print("Saldo insufficiente.")
            input("Continua? ")
        elif numero_saques_hoje >= 3:
            print("Número de saques diários permitido excedido.")
            input("Continua? ")
        else:
            # update values
            numero_saques_hoje += 1
            id_operacao += 1
            saldo -= valor_sacar

            # format data for transaction history print-out
            id_operacao_formatado += f'{str(id_operacao).rjust(3, "0").center(5, " ")}'
            valor_sacado_formatado = formatar_valor(valor_sacar, True)
            saldo_formatado = formatar_valor(saldo)

            # update transaction history
            historico += f"{id_operacao_formatado}|{valor_sacado_formatado}|{saldo_formatado}"

            # print success message
            print(f'''Você sacou {valor_sacar:.2f}.
O seu saldo é {saldo:.2f}.''')

            # pauses program so user has time to review feedback
            input("Continua? ")

    elif opcao == 3:
        # extrato
        clear_screen()
        imprime_extrato(saldo, historico)
        input("Continua? ")

    else:
        # erro de digitação
        clear_screen()
        print("Input inválida. Por favor selecione novamente a operação desejada. ")
        input("Continua? ")
