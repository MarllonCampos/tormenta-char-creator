"""Arco Curto"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType, WeaponRange, WeaponProficiency, WeaponHilt


class ArcoCurto(BaseWeapon):
    """Representação da Arco Curto no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.type = WeaponType.PERFURACAO
        self.weight = 1
        self.damage = "1d6"
        self.range = WeaponRange.MEDIO
        self.weapon_threat = "x3"
        self.price = 30
        self.name = "Arco Curto"
        self.proficiency = WeaponProficiency.SIMPLES
        self.is_melee = False
        self.hilt = WeaponHilt.DUPLA
        # TODO -> Criar uma classe de Flechas que extende ammunition
        # self.ammunition = "Flechas"
