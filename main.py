"""
    CLIENTES podem solicitar a abertura de uma CONTA para um GERENTE;
    GERENTE podem abrir contas;
    Cada CONTA terá um GERENTE;
    CLIENTES podem VER o seu SALDO em CONTA;
    CLIENTES podem DEPOSITAR dinheiro em sua CONTA;
    CLIENTES podem RETIRAR dinheiro de sua CONTA;
    CLIENTES podem TRANSFERIR dinheiro entre CONTAS
        - Caso o cliente não tenha SALDO suficiente para a TRANSFERENCIA ele terá um aviso informando sobre o valor
        faltante, caso ele opte por continuar as seguintes regras serão aplicadas:
            - O limite maximo disponivel no cheque especial é de 500,00 reais;
            - Será aplicado uma taxa 0,2% sobre o total
"""


class Cliente:

    def __init__(self, nome, idade, cpf, rg, endereco, telefone, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.conta = None
        self.cheque_especial = 500.0

    def solicitar_abertura_de_conta(self, gerente, numero, senha, tipo, saldo):
        conta = gerente.abrir_conta(numero, senha, tipo, saldo)
        conta.gerente = gerente
        self.conta = conta

    def verificar_saldo(self):
        self.conta.saldo = self.conta.saldo - 0.05
        print(f'seu saldo é: {self.conta.saldo:.2f}')

    def depositar(self, valor):
        self.conta.saldo = self.conta.saldo + valor
        print(f'Seu saldo final é de: R${self.conta.saldo:.2f}')

    def retirar(self, valor):
        self.conta.saldo = self.conta.saldo - valor
        print(f'Seu saldo final é de: R${self.conta.saldo:.2f}')

    def transferir(self, valor, cliente):
        if self.conta.saldo >= valor + 0.10:
            self.conta.saldo = self.conta.saldo - 0.10
            self.conta.saldo = self.conta.saldo - valor
            cliente.conta.saldo = cliente.conta.saldo + valor
            print(f'Seu saldo final é de: R${self.conta.saldo:.2f}')
        else:
            if self.cheque_especial >= self.conta.saldo - (valor + 0.10):
                resposta = input(f'Saldo insuficiente, será utilizado {(self.conta.saldo - (valor + 0.10)):.2f} do seu cheque especial, deseja continuar? \n')
                if resposta == 'sim':
                    self.cheque_especial = self.cheque_especial - self.conta.saldo - (valor + 0.10)


# saldo = 300
# cs = 500
# valor = 350

# saldo - valor
# cs - valor_negativo


class Gerente:

    def __init__(self, nome, idade, tempo_de_empresa, salario, cpf, rg):
        self.nome = nome
        self.idade = idade
        self.tempo_de_empresa = tempo_de_empresa
        self.salario = salario
        self.cpf = cpf
        self.rg = rg

    def abrir_conta(self, numero, senha, tipo, saldo):
        if saldo >= 25:
            conta = Conta(numero, senha, tipo, saldo)
            print(f'Conta da numero {conta.numero} aberta com sucesso!')
            print(f'Saldo inicial é: R${conta.saldo}')
            return conta
        else:
            print('Erro: Necessário deposito de ao menos R$ 25,00 para a abertura de conta.')


class Conta:

    def __init__(self, numero, senha, tipo, saldo):
        self.numero = numero
        self.senha = senha
        self.tipo = tipo
        self.saldo = saldo
        self.gerente = None


gerente_gessica = Gerente('Gessica', 31, 1, 5000, 99999, 99999)
cliente_gabriel = Cliente('gabriel', 29, '02802399047', '1090306513', 'rua donald', '51997186774',
                          'gabstoffel@gmail.com')
cliente_megui = Cliente('Megui', 22, '99999', '888888', 'rua donald', '51245875', 'meguisbs@gmail.com')

cliente_gabriel.solicitar_abertura_de_conta(gerente_gessica, 2, 2222, 'CP', 25.0)
cliente_megui.solicitar_abertura_de_conta(gerente_gessica, 3, 3232, 'CS', 25.0)

cliente_megui.verificar_saldo()

cliente_gabriel.depositar(100)
cliente_gabriel.retirar(22)
cliente_gabriel.transferir(25.0, cliente_megui)
cliente_megui.verificar_saldo()
