class Veiculo:
    def __init__(self, placa, modelo, ano, cor, valorDiaria):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.valorDiaria = valorDiaria

class Esportivo(Veiculo):
    def __init__(self, velocidade, listaMelhorias):
        self.velocidade = velocidade
        self.listaMelhorias = listaMelhorias

        super().__init__(self, placa, modelo, ano, cor, valorDiaria)

class Utilitario(Veiculo):
    def __init__(self, qtdPassageiros, tamBagageiro, rendimento):
        self.qtdPassageiros = qtdPassageiros
        self.tamBagageiro = tamBagageiro
        self.rendimento = rendimento

        super().__init__(self, placa, modelo, ano, cor, valorDiaria)

class Reserva:
    def __init__(self, codigo, dataInicio, dataFim):
        self.codigo = codigo
        self.dataInicio = dataInicio
        self.dataFim = dataFim

class Pessoa():
    def __init__(self, nome, cpf, idade, endereco, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

class Cliente(Pessoa):
    def __init__(self, id, numCnh, foto, anoValidadeCnh):
        self.id = id
        self.numCnh = numCnh
        self.foto = foto
        self.anoValidadeCnh = anoValidadeCnh

    Pessoa(). __init__(self, nome, cpf, idade, endereco, telefone, email)

class Funcionario(Pessoa):
    def __init__(self, dataContratacao, salario, qtdAluguel, status):
        self.dataContratacao = dataContratacao
        self.salario = salario
        self.qtdAluguel = qtdAluguel
        self.status = status

    Pessoa(). __init__(self, nome, cpf, idade, endereco, telefone, email)
    
class Promocao:
    def __init__(self, titulo, descricao, dt_validade):
        self.titulo = titulo
        self.descricao = descricao
        self.dt_validade = dt_validade