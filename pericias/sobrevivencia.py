from pericias.periciapadrao import PericiaPadrao

from enum_atributos import AtributosPadrao


class Sobrevivencia(PericiaPadrao):
    def __init__(self):
        super().__init__()
        self.nome = __class__.__name__
        self.default_attribute = AtributosPadrao.SAB
