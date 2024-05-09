"""Poder Estilo de Duas Armas"""
from src.powers.base import BasePower
from src.project_typing.attributes import Attributes
from src.skills import Luta


class EstiloDuasArmas(BasePower):
    """Representação do poder Estilo de Duas Armas no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Estilo de Duas Armas"
        self.description = "Se estiver empunhando duas armas (e pelo menos uma delas for leve) e fizer a ação agredir, você pode fazer dois ataques, um com cada arma. Se fizer isso, sofre –2 em todos os testes de ataque até o seu próximo turno. Se possuir Ambidestria, em vez disso não sofre penalidade para usá-lo"
        self.pre_requisite = {
          "skills": [Luta()],
          "attributes": {
            Attributes.DES: 2
          }
        }
