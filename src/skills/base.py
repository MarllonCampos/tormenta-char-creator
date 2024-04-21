"""Classe Base para as perícias"""
from src.project_typing.attributes import Attributes
class BaseSkill():
    """Uma classe padrão para extender para as próximas perícias."""
    def __init__(self) -> None:
        self.name: str = ""
        self.key_attribute: Attributes = None
        self.only_trained: bool = False
        self.armor_penalty: bool = False
        self.description: str = ""
