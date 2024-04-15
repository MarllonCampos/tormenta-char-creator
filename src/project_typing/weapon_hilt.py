"""Enum de empunhadura"""
from .base_enum import BaseEnum


class WeaponHilt(BaseEnum):
    """Enum de empunhadura da arma"""
    LEVE = "leve"
    SINGULAR = "singular"
    DUPLA = "dupla"


    def __str__(self):
        return self.value
