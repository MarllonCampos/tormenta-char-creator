"""Machado Anão"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType, WeaponRange, WeaponProficiency, WeaponHilt


class MachadoAnao(BaseWeapon):
    """Representação da Machado Anão no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.EXOTICA
        self.is_melee = True
        self.hilt = WeaponHilt.SINGULAR
        self.name = "Machado Anão"
        self.price = 30
        self.damage = "1d10"
        self.weapon_threat = "x3"
        self.range = WeaponRange.PESSOAL
        self.type =  WeaponType.CORTE
        self.weight = 1
