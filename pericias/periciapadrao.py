
from enum_atributos import AtributosPadrao


class PericiaPadrao():

    DEFAULT_EXPERTISES = [("Acrobacia", "acrobacia"),
                          ("Adestramento", "adestramento"),
                          ("Atletismo", "atletismo"),
                          ("Atuação", "atuacao"),
                          ("Cavalgar", "cavalgar"),
                          ("Conhecimento", "conhecimento"),
                          ("Cura", "cura"),
                          ("Diplomacia", "diplomacia"),
                          ("Enganação", "enganacao"),
                          ("Fortitude", "fortitude"),
                          ("Furtividade", "furtividade"),
                          ("Guerra", "guerra"),
                          ("Iniciativa", "iniciativa"),
                          ("Intimidação", "intimidacao"),
                          ("Intuição", "intuicao"),
                          ("Investigação", "investigacao"),
                          ("Jogatina", "jogatina"),
                          ("Ladinagem", "ladinagem"),
                          ("Luta", "luta"),
                          ("Misticismo", "misticismo"),
                          ("Nobreza,", "nobreza"),
                          ("Ofício", "oficio"),
                          ("Percepção", "percepcao"),
                          ("Pilotagem,", "pilotagem"),
                          ("Pontaria", "pontaria"),
                          ("Reflexos", "reflexos"),
                          ("Religião", "religiao"),
                          ("Sobrevivência", "sobrevivencia"),
                          ("Vontade", "vontade")]

    def __init__(self):
        self._total: int = 0
        self._others: int = 0
        self._armor_penalty: bool = False
        self._trained: bool = None
        self._trained_value: int = 0
        self._only_trained: bool = False
        self._default_attribute: AtributosPadrao = ""
        self._attribute_value: int = 0
        self._half_level_bonus: int = 0
        self._name = __class__.__name__

    @property
    def total(self):
        return self._total

    @property
    def nome(self):
        return self._name

    @nome.setter
    def nome(self, value):
        self._name = value

    @property
    def others(self):
        return self._others

    @others.setter
    def others(self, value):
        self._others = value

    @property
    def armor_penalty(self):
        return self._armor_penalty

    @armor_penalty.setter
    def armor_penalty(self, value):
        self._armor_penalty = value

    @property
    def trained(self):
        return self._trained

    @trained.setter
    def trained(self, value):
        self._trained = value

    @property
    def default_attribute(self):
        return self._default_attribute

    @default_attribute.setter
    def default_attribute(self, value):
        self._default_attribute = value

    @property
    def attribute_value(self):
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, value):
        self._attribute_value = value

    @property
    def trained_value(self):
        return self._trained_value

    @trained_value.setter
    def trained_value(self, value):
        self._trained_value = value

    @property
    def half_level_bonus(self):
        return self._half_level_bonus

    @half_level_bonus.setter
    def half_level_bonus(self, value):
        self._half_level_bonus = value

    @property
    def only_trained(self):
        return self._only_trained

    @only_trained.setter
    def only_trained(self, value):
        self._only_trained = value

    def update_total(self):
        total = self.half_level_bonus + \
            self.attribute_value + self.others

        if not self.trained:
            self._total = total
            return
        self._total = total + self.trained_value

    def increase_others(self, value):
        self.others = int(self.others)+int(value)
        self.update_total()

    def return_object(self):
        return {
            "total": self._total,
            "level": self.half_level_bonus,
            "atributo": self.attribute_value,
            "treino": self.trained_value,
            "outros": self.others
        }
