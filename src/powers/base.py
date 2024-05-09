"""Classe Base para Poderes"""
class BasePower():
    """Classe padrão para extender para os próximos poderes"""
    def __init__(self)-> None:
        self.name: str = __class__.__name__
        self.description: str = ""
        self.pre_requisite = {}

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return (
            f"{class_name} -> [\n\tname: {self.name},"
        )
        