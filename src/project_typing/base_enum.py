"""Enum base para outros"""
from enum import Enum
class BaseEnum(Enum):
    """Enum customizado para retornar o nome humanificado do ENUM"""
    def __str__(self):
        return self.value
