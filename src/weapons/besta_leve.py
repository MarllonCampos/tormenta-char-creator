"""Besta Leve"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class BestaLeve(BaseWeapon):
    """Representação da Besta Leve no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.type = WeaponType.PERFURACAO
        self.weight = 1
        self.damage = "1d8"
        self.range = WeaponRange.MEDIO
        self.weapon_threat = 19
        self.price = 35
        self.name = "Besta Leve"
        self.proficiency = WeaponProficiency.SIMPLES
        self.is_melee = False
        self.hilt = WeaponHilt.SINGULAR
        # TODO -> Criar uma classe de virote que extende ammunition
        # self.ammunition = "Virote"
