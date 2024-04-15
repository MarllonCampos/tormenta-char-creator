"""Enum de alcance"""
from .base_enum import BaseEnum


class WeaponRange(BaseEnum):
    """Enum de alcance da arma"""
    PESSOAL = "pessoal"
    CURTO = "curto"
    MEDIO = "medio"
    LONGO = "longo"

