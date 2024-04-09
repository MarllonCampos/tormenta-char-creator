"""Machado de Guerra"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class MachadoGuerra(BaseWeapon):
    """Representação da Machado de Guerra no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.MARCIAL
        self.is_melee = True
        self.hilt = WeaponHilt.DUPLA
        self.name = "Machado de Guerra"
        self.price = 20
        self.damage = "1d12"
        self.weapon_threat = "x3"
        self.range = WeaponRange.PESSOAL
        self.type =  WeaponType.CORTE
        self.weight = 2
