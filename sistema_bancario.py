'''Sistema Bancário'''

# v1: Funcionamento básico, com opcões de depositar, sacar, exhibir extrato e sair
# v2: Aumentar compartamentalização com funções. 
    # 1. ✅ Criar função deposita().
    # 2. ✅ Criar função saque().
    # 3. ✅ Mudar função de extrato para receber saldo como argumento posicional
    # e extrato como argumento nomeado.
        # NOTE: def f(pos1, pos2, /, pos_or_kw, *, kwd1, kwd2)
    # 4. ✅ Adiciona data e hora no extrato das transações
    # 5. ✅ Estabalece max. 3 saques por dia, verificado com datetime
    # 6. ✅ Criar função: cria_usuário()
        # O programa deve armanezar os usuarios em uma lista, um usuario é composto por: nome,
        # data de nascimento, CPF e endereço. O endereço é uma string com o formato: logradouro,
        # nro - bairro - cidade/sigla estado. Deve ser armazenado somente os numeros do cpf.
        # Não podemos cadastrar 2 usuarios com o mesmo cpf.
    # 7. ✅ Criar função: cria_conta()
        # O programa deve armazenar contas em uma lista, uma conta e composta por: agencia,
        # número da conta e usuario. O numero da conta e sequential, iniciando em 1.
        # O número da agencia e fixo: "0001". O usuario pode ter mais de uma conta,
        # mas uma conta pertence a somente um usuário.
    # 8. ✅ Criar "testes" para verificar funções acima
        # NOTE: Só criei funções para imprimir usuarios e contas, não testes de verdade.

# pylint: disable-msg=C0103
# The above comment tells pylint not to flag variables for incorrect formatting
# (By default pylint assumes all variables are constants and expects them to be UPPER_CASE)

menu = '''
Por favor, faça a sua escolha digitando um número
da menu embaixo, e em seguida pressiona "enter":

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuário
[5] Nova Conta
[0] Sair

=> '''

import datetime

LIMITE_VALOR_SACADO_DIARIO = 500
LIMITE_SAQUES_DIARIOS = 3

# Para extrato:
DISPLAY_WIDTH = 100
HALF_DISPLAY_WIDTH = int(DISPLAY_WIDTH / 2)
COLUMN_ONE = 5
EVEN_COLUMNS = int((DISPLAY_WIDTH - 5) / 5)
DOUBLE_LINE = "".center(DISPLAY_WIDTH, "=")
SINGLE_LINE = "".center(DISPLAY_WIDTH, "-")
COLUMN_DIVS = " " * COLUMN_ONE + "|" + (" " * (EVEN_COLUMNS - 1) + "|") * 4

# Para contas:
AGENCIA = "0001"
contas = []

usuarios = []

saldo = 0.00
valor_sacado_hoje = 0.00
numero_saques_hoje = 0
data_controle = datetime.date.today()

id_operacao = 0

extrato_sem_movimentacao = f'''{"Não foram realizadas movimentações.".center(DISPLAY_WIDTH, ".")}'''
extrato = ""
newline = "\n"

def imprime_extrato(saldo_atual, /, *, extrato_atual):
    """Imprime extrato com saldo e extrato atualizados."""
    print(f'''
{DOUBLE_LINE}
            
{"Extrato".center(DISPLAY_WIDTH)}

{DOUBLE_LINE}

{"Histórico de Operações".center(DISPLAY_WIDTH, "-")}
{"#".center(COLUMN_ONE, "-")}{"Data".center(EVEN_COLUMNS, "-")}{"Hora".center(EVEN_COLUMNS, "-")}\
{"Operação".center(EVEN_COLUMNS, "-")}{"Valor".center(EVEN_COLUMNS, "-")}{"Saldo".center(EVEN_COLUMNS, "-")}
{COLUMN_DIVS}
{extrato_sem_movimentacao if id_operacao == 0 else extrato_atual}
{COLUMN_DIVS}
{DOUBLE_LINE}
{f"Saldo atual: R${str(f'{saldo_atual:.2f}')}".center(DISPLAY_WIDTH)}
{DOUBLE_LINE}
    ''')

def clear_screen():
    """Clears screen with newlines"""
    print("\n" * 15)

def pausa():
    """Pausa, espera "enter" do usuário"""
    input('Aperta "enter" para continuar.')

def cria_usuario():
    usuario = {"nome": None, "data_nascimento": None, "cpf": None, "endereco": None}
    usuario['nome'] = input("Nome completo: ")
    usuario['data_nascimento'] = input("Data de nascimento: ")
    usuario['cpf'] = input("CPF (somente números): ")
    for u in usuarios:
        if usuario['cpf'] == u['cpf']:
            print("Usuário com esse CPF já cadastrado.")
            pausa()
            return usuarios
    usuario['endereco'] = input("Endereço no formato 'logradouro, nro - bairro - cidade/sigla estado': ")
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")
    pausa()
    return usuarios

def achar_usuario_por_cpf():
    cpf_procurado = input("CPF (somente números): ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf_procurado:
            return usuario
    return None

def cria_conta():
    usuario = achar_usuario_por_cpf()
    if usuario is None:
        print("Usuário não encontrado.")
        pausa()
        return contas
    numero_conta_nova = 1
    for c in contas:
        if c["usuario"] == usuario:
            numero_conta_nova += 1
    conta = {"agencia": AGENCIA, "numero_conta": numero_conta_nova, "usuario": usuario,}
    contas.append(conta)
    print("Conta criado com sucesso!")
    pausa()
    return contas

def formatar_valor(valor, e_saque = False):
    """Adiciona 'R$' e devolve como str"""
    if e_saque:
        return f"-R${f'{valor:.2f}'}"
    return f"R${f'{valor:.2f}'}"

def centrar(string):
    """Centrar string em coluna"""
    return string.center(EVEN_COLUMNS - 1)

def solicitar_valor(operacao):
    """Solicita valor que o usuário quer depositar ou sacar"""
    if operacao == 1:
        valor = float(input('''Quanto gostaria depositar? '''))
        return valor
    elif operacao == 2:
        valor = float(input('''Quanto gostaria sacar? '''))
        return valor
    else:
        print("Erro")

def get_datetime_atual():
    """Devolve data e hora atual como strings"""
    agora = datetime.datetime.now()
    data = agora.strftime("%d/%m/%Y")
    hora = agora.strftime("%H:%M")
    return(data, hora)

def checar_dia_novo(data_in, saques_hoje):
    if datetime.date.today() != data_in:
        saques_hoje = 0
        return (datetime.date.today(), saques_hoje)
    return (data_in, saques_hoje)


def deposita(valor, saldo_in, id_operacao_in, extrato_in):
    """
    1. Verifique se valor de depósito é válido.
    2. Atualizar valores de saldo, e id de operação
    3. Formatar strings para extrato e atualizar extrato
    4. Devolver novo saldo, id, e extrato

    Args:
        valor (float): valor usuário quer depositar
        saldo_in (float): saldo diponível antes de operação
        id_operacao_in (int): número da última operação executada
        extrato_in (str): extrato sem operação atual
    
    Returns:
        saldo_out (float): saldo pós-transação
        id_operacao_out (int): id da operação atual
        extrato_out (str): extrato atualizada
    """

    # tests
    if valor <= 0:
        print("Valor selecionada inválida")
        pausa()
        return(saldo_in, id_operacao_in, extrato_in)

    # update values
    id_operacao_out = id_operacao_in + 1
    saldo_out = saldo_in + valor

    # Marca data e hora
    data, hora = get_datetime_atual()

    # format data for transaction history print-out
    id_operacao_formatado = f'{newline if id_operacao_out != 1 else ""}\
{str(id_operacao_out).rjust(3, "0").center(5, " ")}'
    data = centrar(data)
    hora = centrar(hora)
    operacao = centrar("DEPOSITO")
    valor_depositado_formatado = centrar(formatar_valor(valor))
    saldo_formatado = centrar(formatar_valor(saldo_out))

    # update transaction history
    extrato_out = extrato_in + f"\
{id_operacao_formatado}|{data}|{hora}|{operacao}|{valor_depositado_formatado}|{saldo_formatado}"

    # print success message
    print(f'''Você depositou R${valor:.2f}.
O seu saldo é R${saldo_out:.2f}.''')
    pausa()

    return (saldo_out, id_operacao_out, extrato_out,)


def saque(valor, saldo_in, id_operacao_in, extrato_in, saques_hoje):
    """
    1. Verifique se valor de saque é válido.
        a. Max. R$500
        b. >= R$0
        c. Saldo suficiente
        d. Max. 3 saques por dia
    2. Atualizar valores de saldo, id de operação, e número de saques feito hoje
    3. Formatar strings para extrato e atualizar extrato
    4. Devolver novo saldo, id, extrato e número de saques hoje

    Args:
        valor (float): valor usuário quer depositar
        saldo_in (float): saldo diponível antes de operação
        id_operacao_in (int): número da última operação executada
        extrato_in (str): extrato sem operação atual
        saques_hoje (int): número de saques já feito hoje
    
    Returns:
        saldo_out (float): saldo pós-transação
        id_operacao_out (int): id da operação atual
        extrato_out (str): extrato atualizada
        saques_hoje (int): número de saques feito incluíndo a operação atual
    """

    # tests
    if valor > LIMITE_VALOR_SACADO_DIARIO:
        print("Saque máximo: R$500.00.")
        pausa()
        return (saldo_in, id_operacao_in, extrato_in, saques_hoje)
    if valor <= 0:
        print("Valor selecionada inválida.")
        pausa()
        return (saldo_in, id_operacao_in, extrato_in, saques_hoje)
    if valor > saldo:
        print("Saldo insufficiente.")
        pausa()
        return (saldo_in, id_operacao_in, extrato_in, saques_hoje)
    if saques_hoje >= LIMITE_SAQUES_DIARIOS:
        print("Número de saques diários permitido excedido.")
        pausa()
        return (saldo_in, id_operacao_in, extrato_in, saques_hoje)

    # Marca data e hora
    data, hora = get_datetime_atual()

    # update values
    id_operacao_out = id_operacao_in + 1
    saldo_out = saldo_in - valor
    saques_hoje += 1

    # format data for transaction history print-out
    id_operacao_formatado = f'{newline if id_operacao_out != 1 else ""}\
{str(id_operacao_out).rjust(3, "0").center(5, " ")}'
    data = centrar(data)
    hora = centrar(hora)
    operacao = centrar("SAQUE")
    valor_sacado_formatado = centrar(formatar_valor(valor, True))
    saldo_formatado = centrar(formatar_valor(saldo_out))

    # update transaction history
    extrato_out = extrato_in + f"{id_operacao_formatado}|{data}|{hora}|{operacao}|{valor_sacado_formatado}|{saldo_formatado}"

    # print success message
    print(f'''Você sacou R${valor:.2f}.
O seu saldo é R${saldo_out:.2f}.''')
    pausa()

    return (saldo_out, id_operacao_out, extrato_out, saques_hoje)

def print_usuario():
    print(usuarios)

def print_contas():
    print(contas)

while True:
    clear_screen()
    data_controle, numero_saques_hoje = checar_dia_novo(data_controle, numero_saques_hoje)
    opcao = int(input(menu))

    if opcao == 0:
        # sair
        clear_screen()
        print("Obrigado por usar os nossos serviços!")
        break

    if opcao == 1:
        # deposito
        clear_screen()

        # solicit deposit amount
        valor_depositar = solicitar_valor(opcao)

        # executar depósito
        saldo, id_operacao, extrato = deposita(
            valor_depositar,
            saldo,
            id_operacao,
            extrato)

    elif opcao == 2:
        # saque
        clear_screen()

        # solicit deposit amount
        valor_sacar = solicitar_valor(opcao)

        # executar saque
        saldo, id_operacao, extrato, numero_saques_hoje = saque(
            valor_sacar,
            saldo,
            id_operacao,
            extrato,
            numero_saques_hoje)

    elif opcao == 3:
        # extrato
        clear_screen()
        imprime_extrato(saldo, extrato_atual=extrato)
        pausa()

    elif opcao == 4:
        # Novo usuário
        clear_screen()
        usuarios = cria_usuario()

    elif opcao == 5:
        # Nova conta
        clear_screen()
        contas = cria_conta()

    elif opcao == 6:
        # opção segredo para testes
        clear_screen()
        print_usuario()

    elif opcao == 7:
        # opção segredo para testes
        clear_screen()
        print_contas()

    else:
        # erro de digitação
        clear_screen()
        print("Input inválida. Por favor selecione novamente a operação desejada. ")
        pausa()