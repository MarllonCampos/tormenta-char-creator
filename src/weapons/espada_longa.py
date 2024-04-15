"""Espada Longa"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType, WeaponRange, WeaponProficiency
from src.project_typing import WeaponHilt


class EspadaLonga(BaseWeapon):
    """Representação da Espada Longa no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.MARCIAL
        self.is_melee = True
        self.hilt = WeaponHilt.SINGULAR
        self.name = "Espada Longa"
        self.price = 15
        self.damage = "1d8"
        self.weapon_threat = 19
        self.range = WeaponRange.PESSOAL
        self.type = WeaponType.CORTE
        self.weight = 1
