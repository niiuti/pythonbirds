class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    israel = Pessoa(nome='Israel')
    alvaro = Pessoa(israel, nome='Alvaro')
    print(Pessoa.comprimentar(alvaro))
    print(id(alvaro))
    print(alvaro.comprimentar())
    print(alvaro.nome)
    print(alvaro.idade)
    for filho in alvaro.filhos:
        print(filho.nome)
    alvaro.sobrenome = 'Rennan'
    del alvaro.filhos
    print(alvaro.__dict__)
    print(israel.__dict__)