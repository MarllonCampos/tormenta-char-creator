"""Enum de proficiencia"""
from .base_enum import BaseEnum


class WeaponProficiency(BaseEnum):
    """Enum de proficiencia necessária da arma"""
    SIMPLES  = "simples"
    MARCIAL = "marcial"
    EXOTICA = "exotica"
    FOGO = "fogo"

