def check_type(value, el_type):
    if type(value) is not el_type:
        raise TypeError(f'A {el_type} was expected but got {type(value)}')


class Pergunta():

    def __init__(self, **kwargs):
        self.questao = kwargs.get("questao")
        self.alternativas = kwargs.get("alternativas")
        self.resposta = kwargs.get("resposta")

    def print_questao(self):
        print(self.questao.capitalize())

    def print_alternativas(self):
        for i, opt in enumerate(self.alternativas):
            print(f'{i + 1} - {opt}')

    @property
    def questao(self):
        return self._questao

    @questao.setter
    def questao(self, value):
        check_type(value, str)
        self._questao = value

    @property
    def alternativas(self):
        return self._alternativas

    @alternativas.setter
    def alternativas(self, value):
        check_type(value, list)
        self._alternativas = value

    @property
    def resposta(self):
        return self._resposta

    @resposta.setter
    def resposta(self, value):
        check_type(value, int)
        self._resposta = value
