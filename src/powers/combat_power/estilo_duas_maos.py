"""Poder Estilo de Duas Mãos"""
from src.powers.base import BasePower
from src.project_typing.attributes import Attributes
from src.skills import Luta


class EstiloDuasMaos(BasePower):
    """Representação do poder Estilo de Duas Mãos no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Estilo de Duas Mãos"
        self.description = "Se estiver usando uma arma corpo a corpo com as duas mãos, você recebe +5 nas rolagens de dano. Este poder não pode ser usado com armas leves."
        self.pre_requisite = {
          "skills": [Luta()],
          "attributes": {
            Attributes.FOR: 2
          }
        }
