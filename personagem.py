from atributos import Atributos, DEFAULT_ATTRIBUTE_CHOICES

from races.racas import Racas
from classes import Classes
import inquirer
from inquirer import errors
from utils import cls

# from classes import Classes
# from origens import Origens
# from divindades import Divindades


class Personagem:
    def __init__(self):
        self.pontos_vida = 0
        self.pontos_mana = 0
        self.deslocamento = ""
        self.nome = ""
        self.defesa = 10
        self.pericias = []
        self.poderes = []
        self.equipamentos = []
        self.magias = []
        self.habilidades = []
        self._atributos = Atributos()
        self._raca = Racas()

        self.add_attributes_from_race()
        self.remove_attribute_from_race()
        self.choose_attribute_from_race()
        # self.classe = Classes()
        # self.origem = Origens()
        # self.divindade = Divindades()

        print(self.atributos)
        # print(self.atributos)
        # print(self._raca.raceSize)

    @property
    def raca(self):
        return self._raca.race

    @property
    def atributos(self):
        return self._atributos.attributes

    def add_attributes_from_race(self):
        if (self.raca.attributes is not None):
            for attribute in self.raca.attributes:
                self._atributos.change_attribute(attribute=attribute, mod=1)

    def remove_attribute_from_race(self):
        if (self.raca.remove_attributes is not None):
            for attribute in self.raca.remove_attributes:
                self._atributos.change_attribute(attribute=attribute, mod=-1)

    def __validate_max_attribute_choices(self, answers, current):
        if (len(current) > self.raca.any_attribute):
            reason = f"Você selecionou mais atributos doque permitido [{self.raca.any_attribute}], remova o excedente"  # noqa
            raise errors.ValidationError(
                "", reason=reason)
        return True

    def choose_attribute_from_race(self):
        if (self.raca.any_attribute is not None):
            cls()
            print("Reveja seus atributos")
            print(self.atributos)
            choices = self.raca.any_attribute_choices()
            questions = [
                inquirer.Checkbox("atributos",
                                  message=f"Escolha {self.raca.any_attribute} atributos para aumentar em 1",  # noqa
                                  choices=choices,
                                  carousel=True,
                                  validate=self.__validate_max_attribute_choices  # noqa
                                  )
            ]
            answer = inquirer.prompt(questions)
            attributes = answer['atributos']
            for attribute in attributes:
                self._atributos.change_attribute(attribute=attribute, mod=1)
