"""Lança Montada"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class LancaMontada(BaseWeapon):
    """Representação da Lança Montada no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.MARCIAL
        self.is_melee = True
        self.hilt = WeaponHilt.DUPLA
        self.name = "Lança Montada"
        self.price = 10
        self.damage = "1d8"
        self.weapon_threat = "x3"
        self.range = WeaponRange.PESSOAL
        self.type =  WeaponType.PERFURACAO
        self.weight = 2
