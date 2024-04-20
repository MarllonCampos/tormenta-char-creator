"""Classe Base para raças"""
from typing import List
from src.project_typing import Attributes
from src.sizes import BaseSize, Medio



class BaseRace():
    """Uma classe padrão para extender para as próximas raças."""
    def __init__(self):
        self.increase_attribute: List[Attributes] | None = None
        self.reduce_attributes: List[Attributes] | None = None
        self.cant_choose_attributes: List[Attributes] | None = None
        self.any_attribute: int | None = None
        self.size: BaseSize = Medio()
        self.exclude_methods = ["all_abilities","methods_filter"]

    def methods_filter(self,attribute: str):
        """Filtra os metodos para encontrar apenas as habilidades da raça"""
        attribute_isnt_builtin = not attribute.startswith("__")
        attribute_is_abilities = attribute not in self.exclude_methods
        validate_not_builtin_or_actual_method = attribute_isnt_builtin and attribute_is_abilities
        is_callabe = callable(getattr(self, attribute))
        return is_callabe and validate_not_builtin_or_actual_method

    def all_abilities(self):
        """Devolve todos as habilidades da raça"""
        return [attribute for attribute in dir(self) if self.methods_filter(attribute)]
