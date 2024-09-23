'''Sistema Bancário'''

# v3: Modelando o Sistema Bancário em POO
#
# ✅ 1. <<interface>> Transacao(ABC)
# @abstractmethod
# registrar(conta: Conta)
#
# ✅ 2. class Deposito(Transacao)
# propriedades:
# numero: int -> str
# valor: float -> str
# saldo: float -> str
# data: Datetime -> str
# hora: Datetime -> str
# tipo: str
# métodos:
# registrar(conta: Conta)
#
# ✅ 3. class Saque(Transacao)
# propriedades:
# numero: int -> str
# valor: float -> str
# saldo: float -> str
# data: Datetime -> str
# hora: Datetime -> str
# tipo: str
# métodos:
# registrar(conta: Conta)
#
# ✅ 4. class Historico
# propriedades:
# transacoes: list[Transacao,]
# métodos:
# adicionar_transacao(transacao: Transacao)
#
# ✅ 5. class Cliente
# propriedades:
# endereco: str
# contas: list[Conta]
# métodos:
# realizar_transacao(conta: Conta, transacao: Transacao)
# adicionar_conta(conta: Conta)
#
# ✅ 6. class PessoaFisica(Cliente)
# propriedades:
# _cpf: str
# _nome: str
# _data_nascimento: date
#
# ✅ 7. class Conta
# propriedades:
# agencia: str
# saldo: float
# numero: int
# cliente: Cliente
# historico: Historico
# numero_transacao: int
# métodos:
# saldo(): float
# @classmethod: nova_conta(cls): Conta
# sacar(valor: float): bool
# depositar(valor: float): bool
#
# 8. class ContaCorrente(Conta):
# propriedades:
# limite: float
# limite_saques: int
# métodos:
# sacar(valor: float): bool -- overrides parent
#
# 9. Lógica
#
# Note: Previous version tasks below ⬇️


# pylint: disable-msg=C0103
# The above comment tells pylint not to flag variables for incorrect formatting
# (By default pylint assumes all variables are constants and expects
# them to be UPPER_CASE)


# ~~ Imports ~~ #

from __future__ import annotations
import datetime
from abc import ABC, abstractmethod
import random
from textwrap import dedent


# ~~ Classes ~~ #

class Transacao(ABC):
    """
    Abstract class para implementar através Deposito() e Saque()
    Propriedades: valor, data
    Métodos: registrar()
    """
    @property
    @abstractmethod
    def valor(self):  # pylint: disable=C0116
        pass

    @property
    @abstractmethod
    def data(self):  # pylint: disable=C0116
        pass

    @abstractmethod
    def registrar(self):  # pylint: disable=C0116
        pass


class Deposito(Transacao):  # pylint: disable=R0903
    """
    Herda de Transacao.
    Objeto que vai ser adicionado à lista 'transacoes' do histórico.
    Usado para registrar() sucesso ou falha da operação.
    """
    def __init__(self, valor) -> None:
        self._numero = str(conta_ativa.numero_transacao).rjust(3, "0")
        self._valor = valor
        self.saldo = conta_ativa.saldo + valor
        agora = datetime.datetime.now()
        self._data = agora.strftime("%d/%m/%Y")
        self.hora = agora.strftime("%H:%M")
        self.tipo = "DEPOSITO"

    @property
    def numero(self):  # pylint: disable=C0116
        return self._numero

    @property
    def valor(self):
        return self._valor

    @property
    def data(self):
        return self._data

    def registrar(self):
        sucesso = conta_ativa.depositar(self.valor)

        if sucesso:
            conta_ativa.historico.adicionar_transacao(self)
            print(f"\nVocê depositou R${self._valor:.2f}.")
            print(f"Saldo atual: R${self.saldo:.2f}")
        else:
            print("\nNão foi possível completar o depósito.")


class Saque(Transacao):  # pylint: disable=R0903
    """
    Herda de Transacao.
    Objeto que vai ser adicionado à lista 'transacoes' do histórico.
    Usado para registrar() sucesso ou falha da operação.
    """
    def __init__(self, valor) -> None:
        self.numero = str(conta_ativa.numero_transacao).rjust(3, "0")
        self._valor = valor
        self.saldo = conta_ativa.saldo - valor
        agora = datetime.datetime.now()
        self._data = agora.strftime("%d/%m/%Y")
        self.hora = agora.strftime("%H:%M")
        self.tipo = "SAQUE"

    @property
    def valor(self):
        return self._valor

    @property
    def data(self):
        return self._data

    def registrar(self):
        sucesso = conta_ativa.sacar(self.valor)

        if sucesso:
            conta_ativa.historico.adicionar_transacao(self)
            print(f"\nVocê sacou R${self._valor:.2f}.")
            print(f"Saldo atual: R${self.saldo:.2f}")
        else:
            print("\nNão foi possível completar o saque.")


class Historico:
    """
    Armazena lista de transações e print string de transações
    formatado como tabela
    """

    DISPLAY_WIDTH = 100
    COLUMN_ONE = 5
    EVEN_COLUMNS = int((DISPLAY_WIDTH - COLUMN_ONE) / 5) - 1

    def __init__(self) -> None:
        self.transacoes: list[Transacao] = []
        self.historico_transacoes = self.centrar(
            "Nenhuma transação realizada", width=Historico.DISPLAY_WIDTH)
        self.saldo_atual = "R$0.00"

    def centrar(self, string: str, width=EVEN_COLUMNS) -> str:
        return string.center(width)

    def adicionar_transacao(self, transacao):
        """
        Atualiza histórico de transações toda vez que uma transação ocorre
        """
        self.transacoes.append(transacao)

        numero_transacao = self.centrar(
            transacao.numero, width=Historico.COLUMN_ONE)
        data = "|" + self.centrar(transacao.data)
        hora = "|" + self.centrar(transacao.hora)
        tipo = "|" + self.centrar(transacao.tipo)
        valor = (
            "|"
            + self.centrar("R$" + str(f'{transacao.valor:.2f}'))
            )
        saldo = "|" + self.centrar("R$" + str(f'{transacao.saldo:.2f}'))
        self.saldo_atual = "R$" + str(f'{transacao.saldo:.2f}')
        str_transacao = (numero_transacao
                         + data
                         + hora
                         + tipo
                         + valor
                         + saldo)

        if len(self.transacoes) == 1:
            self.historico_transacoes = ""
        if len(self.transacoes) > 1:
            self.historico_transacoes += "\n"
        self.historico_transacoes += str_transacao

    def __str__(self):
        DOUBLE_LINE = "=" * self.DISPLAY_WIDTH
        SINGLE_LINE = '-' * self.DISPLAY_WIDTH
        COLUMN_DIVS = (" " * self.COLUMN_ONE + "|"
                       + (" " * self.EVEN_COLUMNS + "|") * 4)

        detalhes_conta_linha1 = self.centrar(f"Titular: {cliente.nome}",
                                             width=Historico.DISPLAY_WIDTH)
        detalhes_conta_linha2 = self.centrar(
            (f"Agência: {conta_ativa.agencia}, Conta: {conta_ativa.numero}"),
            width=Historico.DISPLAY_WIDTH)
        detalhes_conta = f"""{detalhes_conta_linha1}
{detalhes_conta_linha2}"""
        column_titles = (
            self.centrar("#", width=Historico.COLUMN_ONE)
            + "|" + self.centrar("Data")
            + "|" + self.centrar("Hora")
            + "|" + self.centrar("Operação")
            + "|" + self.centrar("Valor")
            + "|" + self.centrar("Saldo")
        )
        historico = f'''
{DOUBLE_LINE}

{detalhes_conta}

{DOUBLE_LINE}
{self.centrar("Histórico", width=Historico.DISPLAY_WIDTH)}
{DOUBLE_LINE}
{column_titles}
{SINGLE_LINE}
{COLUMN_DIVS}
{self.historico_transacoes}
{COLUMN_DIVS}
{DOUBLE_LINE}
{self.centrar(f"Saldo atual: {self.saldo_atual}",
              width=Historico.DISPLAY_WIDTH)}
{DOUBLE_LINE}
'''
        return historico


class Cliente:
    """
    Objeto para armazenar dados de clientes, incluindo
    a lista de contas ativas para cada cliente
    """
    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.contas: list[Conta] = []

    def realizar_transacao(self, transacao):
        transacao.registrar()

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def __str__(self) -> str:
        return f"""{self.__class__.__name__}: {', '.join(
            [f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"""


class PessoaFisica(Cliente):
    """Herda de Cliente. Adiciona cpf, nome, e data de nascimento."""
    def __init__(self, cpf, nome, data_nascimento, endereco) -> None:
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        """getter"""
        return self._cpf

    @property
    def nome(self):
        """getter"""
        return self._nome


class Conta:
    """
    Armazena dados de conta, incluindo Histórico.
    Executa Saques e Depósitos.
    """
    def __init__(self) -> None:
        self._agencia = str(random.randint(1, 9999)).rjust(4, '0')
        self._saldo = 0.00
        self._numero = (str(random.randint(1, 99999)).rjust(5, '0')
                        + '-' + str(random.randint(0, 9)))
        self._cliente = cliente
        self.historico = Historico()
        self.numero_transacao = 1

    @classmethod
    def nova_conta(cls) -> Conta:
        """Gera nova instancia de Conta"""
        return cls()

    @property
    def saldo(self) -> float:
        """getter"""
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo = value

    @property
    def numero(self):
        """getter"""
        return self._numero

    @property
    def agencia(self):
        """getter"""
        return self._agencia

    def sacar(self, valor) -> bool:
        """
        Checa contra regaras de saque, ajustar saldo, crie objeto Saque,
        e atualizar historico.
        Devolve boolean para indicar sucesso ou falha
        """
        if valor <= 0:
            return False
        if valor > self.saldo:
            return False
        self.saldo -= valor
        self.numero_transacao += 1
        return True

    def depositar(self, valor) -> bool:
        """
        Checa contra regaras de depósito, ajustar saldo, crie objeto Deposito,
        e atualizar historico.
        Devolve boolean para indicar sucesso ou falha
        """
        if valor <= 0:
            return False
        self.saldo += valor
        self.numero_transacao += 1
        return True

    def __str__(self) -> str:
        return f"""{self.__class__.__name__}: {', '.join(
            [f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"""


class ContaCorrente(Conta):
    """
    Herda de Conta, adiciona limite de valor de saque,
    e limite de saques diários.
    Overrides Conta.sacar()
    """
    def __init__(self, limite=500, limite_saques=3) -> None:
        super().__init__()
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor) -> bool:
        hoje = datetime.date.today().strftime("%d/%m/%Y")
        if self.historico.transacoes[-1].data != hoje:
            self._limite_saques = 3
        if valor <= 0:
            return False
        if valor > self.saldo:
            return False
        if valor > self._limite:
            return False
        if self._limite_saques <= 0:
            return False
        self.saldo -= valor
        self.numero_transacao += 1
        self._limite_saques -= 1
        return True


# --------------------------------------------------


def limpa_tela():
    """Clears screen with newlines"""
    print("\n" * 10)


def pausa():
    """Pausa, espera "enter" do usuário"""
    input('Aperta "enter" para continuar.\n')


# --------------------------------------------------


def menu1() -> int:
    """
    0. Sair.
    1. Login com CPF.
    2. Cria usuário novo.
    """
    limpa_tela()
    menu = '''
        Por favor, faça a sua escolha digitando um número
        da menu embaixo, e em seguida pressiona "enter":

        [1] Entrar
        [2] Criar usuário novo

        [0] Sair

        => '''

    selecao = int(input(dedent(menu)))

    return selecao


def login():
    """login com CPF"""
    limpa_tela()
    cpf = input("CPF (somente números): ")
    for c in clientes:
        if c.cpf == cpf:
            return c
    print("\nUsuário não encontrado.\n")
    pausa()
    return None


def cliente_novo() -> PessoaFisica:
    """Cria cliente novo e devolve como PessoaFisica(Cliente)"""
    limpa_tela()
    nome = input("Nome completo: ")
    cpf = input("CPF (somente números): ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input(
        "Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    return PessoaFisica(cpf, nome, data_nascimento, endereco)


def sair():
    """sai"""
    limpa_tela()
    print("Obrigado por usar os nossos serviços!\n")


def menu2() -> int:
    """
    0. Voltar para menu anterior.
    1. Criar conta nova.
    2-n. Entrar em uma das contas existentes.
    """
    limpa_tela()
    if len(cliente.contas) == 0:
        menu = f'''
            Bem-vindo, {cliente.nome}.
            Por favor, faça a sua escolha digitando um número
            da menu embaixo, e em seguida pressiona "enter":

            [1] Criar conta nova

            [0] Voltar para o menu anterior

            => '''
    else:
        contas_existentes = ""
        for conta in cliente.contas:
            contas_existentes += (
                f"[{cliente.contas.index(conta) + 2}] "
                f"Agência: {conta.agencia}, Conta: {conta.numero}\n""")
        menu = f'''\
Bem-vindo, {cliente.nome}.
Por favor, faça a sua escolha digitando um número
da menu embaixo, e em seguida pressiona "enter":

[1] Criar conta nova

Entrar conta -
{contas_existentes}

[0] Voltar para o menu anterior

=> '''

    selecao = int(input(dedent(menu)))

    return selecao


def menu3() -> int:
    """
    0. Voltar para menu anterior.
    1. Depositar.
    2. Sacar.
    3. Exibir extrato.
    """
    limpa_tela()
    menu = f'''
        Bem-vindo, {cliente.nome}.
        Agência: {conta_ativa.agencia}
        Conta: {conta_ativa.numero}

        Por favor, faça a sua escolha digitando um número
        da menu embaixo, e em seguida pressiona "enter":

        [1] Depositar
        [2] Sacar
        [3] Exibir extrato

        [0] Voltar para o menu anterior

        => '''

    selecao = int(input(dedent(menu)))

    return selecao


def depositar():
    """
    1. Pede valor
    2. Cria objeto Deposito
    3. Mandar para Cliente.realizar_transacao
    """
    valor = float(input("Quanto gostaria depositar? "))
    transacao = Deposito(valor)
    cliente.realizar_transacao(transacao)


def sacar():
    """
    1. Pede valor
    2. Cria objeto Saque
    3. Mandar para Cliente.realizar_transacao
    """
    valor = float(input("Quanto gostaria sacar? "))
    transacao = Saque(valor)
    cliente.realizar_transacao(transacao)


# --------------------------------------------------

clientes: list[Cliente] = []
cliente: PessoaFisica = None
conta_ativa: Conta = None

# --------------------------------------------------


while True:
    limpa_tela()

    # login to account or exit
    selecao_menu1 = menu1()

    if selecao_menu1 == 0:
        limpa_tela()
        print("Obrigado por usar os nossos serviços!\n")
        break

    # entrar
    if selecao_menu1 == 1:
        cliente = login()

        if cliente is None:
            continue

    # cliente novo
    elif selecao_menu1 == 2:
        cliente = cliente_novo()
        clientes.append(cliente)

    while cliente is not None:
        # Escolha criar uma conta, entra em uma conta existente, ou voltar
        selecao_menu2 = menu2()

        if selecao_menu2 == 0:
            limpa_tela()
            cliente = None
            continue

        if selecao_menu2 == 1:
            cliente.adicionar_conta(ContaCorrente.nova_conta())

        if selecao_menu2 >= 2:
            conta_ativa = cliente.contas[selecao_menu2 - 2]

        while conta_ativa is not None:
            # choose transaction, historico, ou voltar
            selecao_menu3 = menu3()

            if selecao_menu3 == 0:
                limpa_tela()
                conta_ativa = None
                continue

            if selecao_menu3 == 1:
                # depósito
                limpa_tela()
                depositar()
                pausa()

            elif selecao_menu3 == 2:
                # saque
                limpa_tela()
                sacar()
                pausa()

            elif selecao_menu3 == 3:
                # extrato
                limpa_tela()
                print(conta_ativa.historico)
                pausa()

            else:
                # erro de digitação
                limpa_tela()
                print("Input inválida. Por favor tente novamente. ")
                pausa()
