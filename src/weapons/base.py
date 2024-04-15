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
            f"{class_name} -> [name: {self.name}, type: {self.type}, "
            f"damage: {self.damage}, range: {self.range},"
            f"weapon_threat: {self.weapon_threat}, price: {self.price},"
            f"weight: {self.weight}, proficiency: {self.proficiency},"
            f"is_melee: {self.is_melee}]"
        )

    def weapon_attributes(self) -> list[Enum]:
        """Função que mostra todos os atributos especificos da arma"""
        return [self.hilt, self.proficiency, self.range, self.type]


# TODO -> Criar um arquivo e especificar essa Classe como um Item
class Ammunition:
    """Classe base para munições"""
    def __init__(self) -> None:
        pass
