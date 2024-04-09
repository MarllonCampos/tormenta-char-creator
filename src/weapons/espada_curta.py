"""Espada Curta"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class EspadaCurta(BaseWeapon):
    """Representação da espada curta no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.type = WeaponType.PERFURACAO
        self.weight = 1
        self.damage = "1d6"
        self.range = WeaponRange.PESSOAL
        self.weapon_threat = 19
        self.price = 10
        self.name = "Espada curta"
        self.proficiency = WeaponProficiency.SIMPLES
        self.is_melee = True
        self.hilt = WeaponHilt.LEVE
