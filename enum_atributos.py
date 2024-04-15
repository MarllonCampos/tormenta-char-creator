from enum import Enum


class AtributosPadrao(Enum):
    def __str__(self):
        return str(self.value)
    INT = "INT"
    CON = "CON"
    FOR = "FOR"
    DES = "DES"
    SAB = "SAB"
    CAR = "CAR"
