"""Classe Base para os tamanhos"""


class BaseSize():
    """Uma classe padrão para extender para os próximos tamanhos."""
    def __init__(self) -> None:
        self.name: str | None = None
        self.natural_reach: float | None = None
        self.ocuppied_space: float | None = None
        self.furtive_modifier: float | None = None
        self.maneuver_modifier: float | None = None
