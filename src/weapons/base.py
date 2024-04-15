"""Classe Base para Armas"""
from typing import List
from enum import Enum
from src.project_typing import WeaponHilt, WeaponProficiency, WeaponRange, WeaponType

class BaseWeapon:
    """Uma classe padrão para extender para as próximas armas."""
    def __init__(self):
        self.type: WeaponType | List[WeaponType] = "" # Corte / Perfuração / Impacto
        self.weight: float = "" # 1 - 10
        self.damage: str | List[str]  = "" # 1d3 - 4d12
        self.range: WeaponRange | List[WeaponRange] = "" # Pessoal / Curto / Médio / Longo
        self.weapon_threat: str | int | List[str|int] = "" # x2 - 14
        self.price: float = "" # 0 - 1000000
        self.name: str = "" # Adaga
        self.proficiency: WeaponProficiency = "" # Simples / Marcial / Exótica / Fogo
        self.is_melee: bool = None # Corpo / Distancia
        self.hilt: WeaponHilt = ""
        self.ammunition: None | Ammunition = None if self.is_melee else Ammunition

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
        return [self.hilt,self.proficiency,self.range,self.type]
        
class Ammunition: # TODO -> Criar um arquivo e especificar essa Classe como um Item
    def __init__(self) -> None:
        pass
