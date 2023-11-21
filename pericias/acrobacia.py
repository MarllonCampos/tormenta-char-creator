from pericias.periciapadrao import PericiaPadrao
from enum_atributos import AtributosPadrao


class Acrobacia(PericiaPadrao):
    def __init__(self):
        super().__init__()
        self.nome = __class__.__name__
        self.armor_penalty = True
        self.default_attribute = AtributosPadrao.DES
