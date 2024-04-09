"""Arco Longo"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class ArcoLongo(BaseWeapon):
    """Representação da Arco Longo no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.MARCIAL
        self.is_melee = False
        self.hilt = WeaponHilt.DUPLA
        self.name = "Arco Longo"
        self.price = 100
        self.damage = "1d8"
        self.weapon_threat = "x3"
        self.range = WeaponRange.MEDIO
        self.type =  WeaponType.PERFURACAO
        self.weight = 2
        # TODO -> Criar uma classe de Flechas que extende ammunition
        # self.ammunition = "Flechas"
