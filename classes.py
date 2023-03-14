class Veiculo():
    def __init__(self, placa, modelo, ano, cor, valorDiaria):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.valorDiaria = valorDiaria

class Esportivo(Veiculo):
    def __init__(self, velocidade):
        self.velocidade = velocidade

        Veiculo().__init__(self, placa, modelo, ano, cor, valorDiaria)

class Reserva:
    def __init__(self, codigo, dataInicio, dataFim):
        self.codigo = codigo
        self.dataInicio = dataInicio
        self.dataFim = dataFim

class Pessoa():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

class Cliente(Pessoa):
    def __init__(self, id):
        self.id = id

    Pessoa(). __init__(self, nome, endereco)

class Funcionario(Pessoa):
    def __init__(self, cpf, idade, dataContratacao, salario, qtdAluguel, status):
        self.cpf = cpf
        self.idade = idade
        self.dataContratacao = dataContratacao
        self.salario = salario
        self.qtdAluguel = qtdAluguel
        self.status = status

    Pessoa(). __init__(self, nome, endereco)
    
