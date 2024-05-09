"""Classe Base para Armas"""
from typing import List, Union
from enum import Enum
from src.project_typing import WeaponHilt, WeaponProficiency
from src.project_typing import WeaponRange, WeaponType


class BaseWeapon:
    """Uma classe padrão para extender para as próximas armas."""
    def __init__(self):
        # Corte / Perfuração / Impacto
        self.type: WeaponType | List[WeaponType] = ""
        self.weight: float = ""  # 1 - 10
        self.damage: str | List[str] = ""  # 1d3 - 4d12

        # Pessoal / Curto / Médio / Longo
        self.range: WeaponRange | List[WeaponRange] = ""

        # x2 - 14
        self.weapon_threat: str | int | List[Union[str | int]] = ""
        self.price: float = ""  # 0 - 1000000
        self.name: str = ""  # Adaga

        # Simples / Marcial / Exótica / Fogo
        self.proficiency: WeaponProficiency = ""
        self.is_melee: bool = None  # Corpo / Distancia
        self.hilt: WeaponHilt = ""
        self.ammunition: None | Ammunition = None if self.is_melee else Ammunition  # noqa: E501

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return (
            f"{class_name} -> [\n\tname: {self.name}, \n\ttype: {self.type},\n"
            f"\tdamage: {self.damage}, \n\trange: {self.range},\n"
            f"\tweapon_threat: {self.weapon_threat}, \n\tprice: {self.price},\n"
            f"\tweight: {self.weight}, \n\tproficiency: {self.proficiency},\n"
            f"\tis_melee: {self.is_melee}\n]"
        )

    def weapon_attributes(self) -> list[Enum]:
        """Função que mostra todos os atributos especificos da arma"""
        return [self.hilt, self.proficiency, self.range, self.type]


# TODO -> Criar um arquivo e especificar essa Classe como um Item
class Ammunition:
    """Classe base para munições"""
    def __init__(self) -> None:
        pass
