"""Classe de Loja"""
from enum import Enum
from typing import List
import tabulate
from src.weapons import ALL_WEAPONS
from src.weapons.base import BaseWeapon


class StoreWeapons:
    """Uma classe padrão para poder mostrar as armas que existem e seus preços"""

    def __init__(self) -> None:
        self.filtered_weapons: List[BaseWeapon] = []

    def _filter_weapons(self, weapon_attributes: List[Enum] = None):
        """Filtra de todas as armas as que atendem aos requisitos"""
        if weapon_attributes is None:
            self.filtered_weapons = ALL_WEAPONS
            return

        if not isinstance(weapon_attributes, list):
            weapon_attributes = [weapon_attributes]

        for weapon in ALL_WEAPONS:
            if any(attr in weapon.weapon_attributes() for attr in weapon_attributes):
                self.filtered_weapons.append(weapon)

    def _format_list_in_string(self, list_values) -> str:
        if not isinstance(list_values, list):
            return str(list_values)
        return '/'.join(str(value) for value in list_values)

    def showcase(self, weapon_attributes: List[Enum] = None ) -> List[BaseWeapon]:
        """Função que mostra todas as armas possíveis podendo ser filtradas """
        self.filtered_weapons.clear()
        self._filter_weapons(weapon_attributes)

        headers = ["Nome", "Preço", "Dano",
            "Crítico", "Alcance", "Tipo", "Espaços"]
        data = []
        for weapon in self.filtered_weapons:
            price = f"T${weapon.price}"
            damage = self._format_list_in_string(weapon.damage)
            critical = '/'.join(str(threat) for threat in weapon.weapon_threat) if isinstance(
                weapon.weapon_threat, list) else str(weapon.weapon_threat)
            weapon_range = '/'.join(str(range) for range in weapon.range) if isinstance(
                weapon.range, list) else str(weapon.range)
            weapon_type = '/'.join(str(type) for type in weapon.type) if isinstance(
                weapon.type, list) else str(weapon.type)
            weight = weapon.weight
            name = weapon.name
            data.append([name, price, damage, critical,
                        weapon_range, weapon_type, weight])
            # print(f"{weapon.name:>20} {price_formatted:^14} {damage_formatted:^6} {threat_formatted}",end="")
            # print(f"{weapon.range:} {weapon.type:} {weapon.weight:}")
        table = tabulate.tabulate(
            data, headers=headers, tablefmt="rounded_grid", stralign="center")
        print(table)

